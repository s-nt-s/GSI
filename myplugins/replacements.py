import re
from pathlib import Path
from urllib.parse import urlparse

import bs4
import requests
import yaml
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor
from munch import DefaultMunch, Munch
from pelican import signals
from os.path import join, dirname
import unidecode
from glob import glob
from .core.util import get_dom, get_class_dom
from .core.abbr import Abbr

re_sp = re.compile(r"\s+")

def readhead(file):
    head = ''
    firstLine = True
    with open(file, "r") as f:
        for l in f.readlines():
            sl = unidecode.unidecode(l.strip())
            if len(sl)==0 and firstLine:
                continue
            if firstLine and sl != '---':
                return None
            if firstLine and sl == '---':
                firstLine = False
                continue
            if not firstLine and sl == '---':
                break
            head = head + l
    if len(head.strip())==0:
        return None
    return head


def readyaml(file):
    if str(file).endswith(".md"):
        head = readhead(file)
        if head is None:
            return None
        return yaml.safe_load(head)
    with open(file, 'r') as stream:
        r = yaml.load_all(stream, Loader=yaml.FullLoader)
        r = list(r)
        if len(r) == 1:
            return r[0]
        return r


def get_soup(url):
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.content, "lxml")
    return soup

class Replace:
    def __init__(self, delimiter, replacements, abbr):
        self.replacements = replacements
        self.delimiter = delimiter
        self.abbr = abbr
        self.re_num = re.compile(r"[⁰¹²³⁴⁵⁶⁷⁸⁹]+")
        self.re_scape = tuple((
            re.compile(r"(\[[^\[\]]*\]\(\S+\))"),
            re.compile(r"<abbr[^>]*>[^<]*</abbr>"),
            re.compile(r"<a[^>]*>[^<]*</a>"),
            re.compile(r"<https?://[^>]+>"),
            re.compile(r"`[^`]+`"),
            self.re_num,
        ))

    def rpl(self, txt):
        fake_sep = "@#~½$"
        fake_rem = "x@@@BORRAME@@@x"

        def fake_sub(r, n, x):
            nw = x.group(0)
            doRm = None
            if "rm" in r.groupindex and x.group("rm") not in (None, ""):
                doRm = x.group("rm")
            if doRm:
                nw = nw.replace(x.group("rm"), fake_rem)
                r = re.compile(r.pattern.replace("(?P<rm>", "(?P<rm>"+fake_rem+"|"), r.flags)
            if n is not None:
                nw = r.sub(n, nw)
            if doRm:
                nw = nw.replace(fake_rem, "")
            nw = fake_sep.join(list(nw))
            return fake_sep+nw+fake_sep
        for key, value in self.replacements.items():
            txt = txt.replace(self.delimiter + key + self.delimiter, value)
        for abbr in self.abbr:
            if isinstance(abbr.text, str) and self.re_num.search(abbr.text):
                txt = abbr.re.sub(lambda x:fake_sub(abbr.re, abbr.new_text, x), txt)
        for re_sc in self.re_scape:
            txt = re_sc.sub(lambda x:fake_sub(re_sc, None, x), txt)
        for abbr in self.abbr:
            if not(isinstance(abbr.text, str) and self.re_num.search(abbr.text)):
                txt = abbr.re.sub(lambda x:fake_sub(abbr.re, abbr.new_text, x), txt)
        txt = txt.replace(fake_sep, "")
        return txt


class MkReplace(Preprocessor):

    def __init__(self, delimiter, replacements, abbr):
        self.replace = Replace(delimiter, replacements, abbr)

    def run(self, lines):
        for i, line in enumerate(lines):
            if line.strip() and not line.startswith("wzxhzdk"):
                lines[i] = self.replace.rpl(line)
        return lines


class ExReplace(Extension):

    def __init__(self, config, **kargv):
        self.replacements = config
        super(ExReplace, self).__init__(**kargv)

    def extendMarkdown(self, md, md_globals):
        md.preprocessors.add('replacements', MkReplace(**self.replacements), ">html_block")


def process_settings(pelican_object):
    config_file = Path(pelican_object.settings['REPLACEMENTS_CONFIG'])
    relativeURL = pelican_object.settings.get("RELATIVE_URLS", False)
    replacements = readyaml(config_file)
    if 'PELICAN_SETTINGS' in replacements:
        pSettings = replacements['PELICAN_SETTINGS']
        del replacements['PELICAN_SETTINGS']
        if isinstance(pSettings, str):
            pSettings = pSettings.strip().split()
        if isinstance(pSettings, list):
            for s in pSettings:
                if s not in replacements and s in pelican_object.settings:
                    v = pelican_object.settings[s]
                    if relativeURL and s == "SITEURL":
                        v = ""
                    replacements[s] = str(v)
    delimiter = replacements.pop('DELIMITER', '::')

    abbr = []
    for md in pelican_object.settings.get('CONTENT_MARKD', []):
        meta = readyaml("content/"+md)
        if meta is None:
            continue
        meta = meta.get('abbr')
        if meta is None:
            continue
        ab = Abbr(**meta)
        ab.add_url("{filename}/"+md, insert=0)
        abbr.append(ab)

    abbr.extend(Abbr.load(config_file.parent / "abbr"))

    return Munch(
        delimiter=delimiter,
        replacements=replacements,
        abbr=abbr
    )


def replacements_markdown_extension(pelicanobj, config):
    """Instantiates a customized Markdown extension"""
    pelicanobj.settings['MARKDOWN'].setdefault('extensions', []).append(ExReplace(config))


def replacements_init(pelicanobj):
    """Loads settings and instantiates the Python Markdown extension"""
    # Process settings
    config = process_settings(pelicanobj)

    # Configure Markdown Extension
    replacements_markdown_extension(pelicanobj, config)


def register():
    """Plugin registration"""
    signals.initialized.connect(replacements_init)
