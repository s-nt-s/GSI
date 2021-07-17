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

re_sp = re.compile(r"\s+")

def readlines(file):
    last_line = None
    with open(file, "r") as f:
        for l in f.readlines():
            l = l.strip()
            if not(len(l) == 0 and last_line == ""):
                yield l
            last_line = l
    if last_line not in ("", None):
        yield ""

def readyaml(file):
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


def get_dom(url):
    dom = urlparse(url).netloc
    if dom.endswith(".wikipedia.org"):
        return "wikipedia"
    if dom.startswith("www."):
        dom = dom[4:]
    return dom


def get_title(url):
    dom = get_dom(url)
    if dom == "dpej.rae.es":
        soup = get_soup(url)
        title = soup.select_one("span.field-name-field-definicion")
        if title:
            title = re_sp.sub(" ", title.get_text()).strip()
            if title:
                return title


def readabbr(file):
    r = []
    abbr = DefaultMunch()
    for l in readlines(file):
        if len(l) == 0:
            r.append(abbr)
            abbr = DefaultMunch()
            continue
        if abbr.text is None:
            abbr.text = l
            continue
        slp = l.split("://", 1)
        if l.startswith("{filename}") or (len(slp) == 2 and slp[0].lower() in ("http", "https")):
            abbr.url = l
            continue
        abbr.title = l
    chg = False
    for abbr in r:
        if abbr.url:
            dom = get_dom(abbr.url)
            dom = dom.replace(".", "_")
            if abbr.title is None:
                abbr.title = get_title(abbr.url)
                chg = chg or (abbr.title is not None)
            if abbr.title:
                abbr.new_text = '[\\1]({url} "{title}")'.format(**dict(abbr))+'{: .abbr .'+dom+'}'
            else:
                abbr.new_text = '[\\1]({url})'.format(**dict(abbr))+'{: .'+dom+'}'
        else:
            abbr.new_text = '<abbr title="{title}">\\1</abbr>'.format(**dict(abbr))
    if chg is True:
        with open(file, "w") as f:
            for a in r:
                f.write(a.text+"\n")
                if a.url:
                    f.write(a.url+"\n")
                if a.title:
                    f.write(a.title+"\n")
                f.write("\n")
    return r


class Replace:
    def __init__(self, delimiter, replacements, abbr):
        self.replacements = replacements
        self.delimiter = delimiter
        self.abbr = abbr
        self.re_az = re.compile(r"\w")
        self.re_scape = tuple((
            re.compile(r"(\[[^\[\]]*\]\([^\(\)]+\))"),
            re.compile(r"<abbr[^>]*>[^<]*</abbr>"),
        ))
        for abbr in self.abbr:
            if abbr.re is None:
                abbr.re = self.get_re(abbr.text)

    def get_limits(self, text):
        a, z = ("(", ")")
        aux = str(text)
        for i in "([])?":
            aux = aux.replace(i, "")
        if self.re_az.match(aux[0]):
            a = r"\b"+a
        if self.re_az.match(aux[-1]):
            z = z+r"\b"
        return a, z

    def get_re(self, text):
        if len(text) > 3 and text[0:2] in ("r'", 'r"', "i'", 'i"'):
            flag = text[0]
            text = text[2:-1]
            a, z = self.get_limits(text)
            re_rule = a+text+z
            if flag == 'i':
                return re.compile(re_rule, re.IGNORECASE)
            return re.compile(re_rule)
        a, z = self.get_limits(text)
        if len(text) > 5 and text.upper() != text:
            lw = text[0].lower()
            up = text[0].upper()
            if lw != up:
                return re.compile(a+r"["+lw+up+r"]" + re.escape(text[1:]) + z)
        return re.compile(a + re.escape(text) + z)

    def rpl(self, txt):
        fake_sep = "@#~½$"

        def fake_sub(r, n, x):
            if n is None:
                x = fake_sep.join(list(x.group(0)))
            else:
                x = r.sub(n, x.group(0))
                x = fake_sep.join(list(x))
            return x
        for key, value in self.replacements.items():
            txt = txt.replace(self.delimiter + key + self.delimiter, value)
        for re_sc in self.re_scape:
            txt = re_sc.sub(lambda x:fake_sub(self.re_scape, None, x), txt)
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
