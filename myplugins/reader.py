import os
import re

import bs4
from pelican import signals
from pelican.utils import SafeDatetime, pelican_open
from munch import Munch, DefaultMunch

#from pelican.readers import MarkdownReader as MarkReader
from .yamlmetadata import YAMLMetadataReader as MarkReader
from .util import run
from datetime import date, datetime

# https://github.com/pR0Ps/pelican-yaml-metadata

re_tags = tuple(
    (t, re.compile(r"\b" + t + r"\b", re.IGNORECASE)) for t in
    ("tag1", "tag2")
)
re_normalize = tuple(
    (t, re.compile(r"^(" + r + r")$", re.IGNORECASE)) for t, r in (
        ("literal", r"re"),
    )
)
re_tags = tuple()
re_normalize = tuple()

def get_date(file):
    dates = run("git", "log", "--format=%ai", file)
    dates = dates.strip().split("\n")
    if len(dates)==0:
        return DefaultMunch(create=None, update=None)
    print(file, dates)
    dates=list(map(lambda x:datetime.strptime(x, '%Y-%m-%d %H:%M:%S %z'), dates))
    return Munch(
        created=dates[-1],
        updated=dates[0]
    )


def get_tag_normalized(tag):
    for t, r in re_normalize:
        if r.match(tag):
            return t
    return tag


def get_tags(content):
    tags = set()
    for tag, match in re_tags:
        if match.search(content):
            tags.add(tag)
    return tags


def clean_tags(remove_tags, *args):
    tags = set()
    for tag in args:
        tag = get_tag_normalized(tag)
        if tag not in remove_tags:
            tags.add(tag)
    return sorted(tags)


def to_date(s):
    d = SafeDatetime.fromtimestamp(s)
    #d = d.replace(hour=0, minute=0, second=0, microsecond=0)
    return d


class MyReader(MarkReader):
    enabled = True
    file_extensions = ['md']

    def read(self, filename, *args, **kargv):
        output, metadata = super().read(filename)
        '''
        if None in (metadata.get('date'), metadata.get('modified')):
            dt = get_date(filename)
            if dt.created and metadata.get('date') is None:
                metadata['date']=dt.created
            if dt.updated and metadata.get('modified') is None:
                metadata['modified']=dt.updated
        '''
        fl_stat = os.stat(filename)
        if metadata.get('date') is None:
            metadata['date'] = to_date(fl_stat.st_ctime)
        if metadata.get('modified') is None:
            metadata['modified'] = to_date(fl_stat.st_mtime)
        if self.settings.get("PUBLISH_ALL") is True and not metadata.get("harddraft"):
            metadata['status'] = 'published'
        if 'version' not in metadata:
            metadata['version'] = {}
        fileroot = filename.rsplit(".", 1)[0]+"."
        filebase = os.path.basename(fileroot)
        for t in ("epub", "pdf"):
            if os.path.isfile(fileroot+t):
                metadata['version'][t.upper()] = filebase+t

        html = bs4.BeautifulSoup(output, "lxml")
        content = str(metadata['title']) + "\n" + html.get_text()
        tags = get_tags(content)
        remove_tags = set()
        for t in metadata.get("tags", []):
            if t.name.startswith("!"):
                remove_tags.add(t.name[1:])
            else:
                tags.add(t.name.lower())

        if len(tags) > 0:
            tags = clean_tags(remove_tags, *tags)
            metadata["tags"] = self.process_metadata("tags", ", ".join(tags))
        else:
            metadata["tags"] = []

        return output, metadata


def add_reader(readers):
    for ext in MyReader.file_extensions:
        readers.reader_classes[ext] = MyReader


def register():
    signals.readers_init.connect(add_reader)
