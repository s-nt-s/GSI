import yaml
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor
from pelican import signals
from pathlib import Path
from munch import DefaultMunch, Munch
import re

def readlines(file):
    last_line = None
    with open(file, "r") as f:
        for l in f.readlines():
            l = l.strip()
            if not(len(l)==0 and last_line==""):
                yield l
            last_line = l
    if last_line not in ("", None):
        yield ""

def readabbr(file):
    r = []
    abbr = DefaultMunch()
    for l in readlines(file):
        if len(l)==0:
            r.append(abbr)
            abbr = DefaultMunch()
            continue
        if abbr.text is None:
            abbr.text = l
            continue
        slp = l.split("://", 1)
        if len(slp)==2 and slp[0].lower() in ("http", "https"):
            abbr.url = l
            continue
        abbr.title = l
    for abbr in r:
        if abbr.url:
            if abbr.title:
                abbr.new_text = '[\\1]({url} "{title}")'.format(**dict(abbr))+'{: .abbr}'
            else:
                abbr.new_text = '[\\1]({url})'.format(**dict(abbr))
        else:
            abbr.new_text = '<abbr title="{title}">\\1</abbr>'.format(**dict(abbr))
    return r

class Replace:
    def __init__(self, delimiter, replacements, abbr):
        self.replacements = replacements
        self.delimiter = delimiter
        self.abbr = abbr
        for abbr in self.abbr:
            if abbr.re is None:
                if len(abbr.text)>3 and abbr.text[0:2] in ("r'", 'r"'):
                    abbr.re = re.compile(r"\b("+abbr.text[2:-1]+r")\b")
                else:
                    abbr.re = re.compile(r"\b(" + re.escape(abbr.text)+ r")\b")

    def rpl(self, txt):
        fake_sep = "@#~½$"
        def fake_sub(r, n, x):
            x = r.sub(n, x.group(0))
            x = fake_sep.join(list(x))
            return x
        for key, value in self.replacements.items():
            txt = txt.replace(self.delimiter + key + self.delimiter, value)
        for abbr in self.abbr:
            #txt = abbr.re.sub(abbr.new_text, txt)
            txt = abbr.re.sub(lambda x:fake_sub(abbr.re, abbr.new_text, x), txt)
        txt = txt.replace(fake_sep, "")
        return txt


class MkReplace(Preprocessor):

    def __init__(self, delimiter, replacements, abbr):
        self.replace = Replace(delimiter, replacements, abbr)

    def run(self, lines):
        for i, line in enumerate(lines):
            if line.strip() and not line.startswith("wzxhzdk"):
                if line == "---":
                    break
                lines[i]=self.replace.rpl(line)
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
    with open(config_file, 'r') as stream:
        replacements = yaml.load(stream, Loader=yaml.FullLoader)
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

    abbr = readabbr(config_file.parent / "abbr.txt")

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
