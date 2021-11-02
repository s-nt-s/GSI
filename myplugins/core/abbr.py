from munch import DefaultMunch, Munch
from functools import lru_cache
from pathlib import Path
import re
from copy import deepcopy
from .util import get_dom
from .boe import BOE

re_isboe = re.compile(r"https?://www\.boe\.es/buscar/.*\?id=BOE.*")
re_az = re.compile(r"\w")
re_hasta = re.compile(r"^Hasta \d+ fue .*")

def readlines(*files):
    last_line = None
    for file in files:
        with open(file, "r") as f:
            for l in f.readlines():
                l = l.strip()
                if not(len(l) == 0 and last_line == ""):
                    yield l
                last_line = l
    if last_line not in ("", None):
        yield ""

class Abbr():
    def __init__(self, text=None, file=None, title=None, **kvargs):
        self.text = text
        self.file = file
        self.urls = []
        self.titles = []
        self._re = None
        self._class = "abbr"
        self._title = None
        if title is not None:
            self.titles.append(title)

    @property
    def d(self):
        d = deepcopy(self.__dict__)
        d['html_class'] = self.html_class
        d['md_class'] = " ".join('.'+c for c in self.html_class.split())
        d['url'] = self.url
        d['title'] = self.title
        return d

    @staticmethod
    def load(file):
        r = []
        if isinstance(file, str):
            file = Path(file)
        if file.is_dir():
            for f in sorted(file.glob("*.txt")):
                r.extend(Abbr.load(f))
            return r
        abbr = Abbr()
        abbr.file = file
        for l in readlines(file):
            if len(l) == 0:
                r.append(abbr)
                abbr = Abbr()
                abbr.file = file
                continue
            spl = l.split("://", 1)
            if l.startswith("{filename}") or (len(spl) == 2 and spl[0].lower() in ("http", "https")):
                abbr.add_url(l)
                continue
            if len(abbr.urls)==0 and abbr.text is None:
                abbr.text = l
                continue
            abbr.titles.append(l)

        for abbr in list(r):
            if abbr.titles:
                abbr._title = abbr.titles[0]
            if abbr.boe:
                if abbr.boe.nula:
                    abbr._class = abbr._class+" "+abbr.boe.nula
                    abbr.titles[0] = abbr.boe.nula.title()+": "+abbr.titles[0]
                abbr.titles[0] = abbr.titles[0]+" ("+abbr.boe.title+")"
                if abbr.text is None:
                    abbr._re = abbr.boe.re.pattern
                else:
                    n_abbr = deepcopy(abbr)
                    n_abbr.text = None
                    n_abbr._re = abbr.boe.re.pattern
                    r.append(n_abbr)
        return r

    def add_url(self, url, insert=None):
        if isinstance(url, str):
            url = DefaultMunch(url=url, attrs="")
            spl = url.url.split(None, 1)
            if len(spl)==2:
                url.url = spl[0]
                url.attrs = spl[1]
        if insert is not None:
            self.urls.insert(insert, url)
        else:
            self.urls.append(url)

    def get_limits(self, text):
        a, z = ("(", ")")
        if r"\b" in text:
            return a, z
        aux = str(text)
        for i in "([])?":
            aux = aux.replace(i, "")
        if re_az.match(aux[0]):
            a = r"\b"+a
        if re_az.match(aux[-1]):
            z = z+r"(?=\b|[⁰¹²³⁴⁵⁶⁷⁸⁹])"
        return a, z

    @property
    @lru_cache(maxsize=None)
    def boe(self):
        for url in self.urls:
            if re_isboe.match(url.url):
                return BOE(url.url)
        return None

    @property
    def url(self):
        if len(self.urls)==0:
            return None
        return self.urls[0]

    @property
    def title(self):
        if len(self.titles)==0:
            return None
        return self.titles[0]

    @property
    @lru_cache(maxsize=None)
    def html_class(self):
        r = set()
        for c in self._class.split():
            r.add(c)
        if self.title and re_hasta.search(self.title):
            r.add("antiguo")
        if self.file:
            cls = self.file.name
            cls = cls.rsplit(".", 1)[0]
            cls = cls.split("-", 1)[-1]
            for c in cls.split():
                r.add(c)
        r = " ".join(sorted(r))
        return r

    @property
    @lru_cache(maxsize=None)
    def re(self):
        if self._re is not None:
            return re.compile(self._re)
        if self.text is not None and len(self.text) > 3 and self.text[0:2] in ("r'", "i'"):
            flag = self.text[0]
            text = self.text[2:]
            a, z = self.get_limits(text)
            re_rule = a+text+z
            if flag == 'i':
                return re.compile(re_rule, re.IGNORECASE)
            return re.compile(re_rule)
        a, z = self.get_limits(self.text)
        if len(self.text) > 5 and self.text.upper() != self.text:
            lw = self.text[0].lower()
            up = self.text[0].upper()
            if lw != up:
                return re.compile(a+r"["+lw+up+r"]" + re.escape(self.text[1:]) + z)
        return re.compile(a + re.escape(self.text) + z)

    def get_new_text(self):
        if self.title is not None and len(self.title) > 3 and self.title[0:2] in ("s'",):
            return self.title[2]
        if self.url:
            if self.title:
                #return '<a class="{html_class}" href="{url.url}" title="{title}">\\1</a>'.format(**self.d)
                return '[\\1]({url.url} "{title}"){{: {md_class} {url.attrs}}}'.format(**self.d)
            #return '<a class="{html_class}" href="{url.url}">\\1</a>'.format(**self.d)
            return '[\\1]({url.url}){{: {md_class} {url.attrs}}}'.format(**self.d)
        return '<abbr class="{html_class}" title="{title}">\\1</abbr>'.format(**self.d)

    @property
    @lru_cache(maxsize=None)
    def new_text(self):
        txt = self.get_new_text()
        for url in self.urls[1:]:
            dom = get_dom(url.url)
            txt=txt + '<sup class="extra_url"><a href="{url.url}" {url.attrs}>{dom}</a></sup>'.format(url=url, dom=dom[0])
        return txt

if __name__ == "__main__":
    from glob import glob
    from os.path import basename
    from textwrap import dedent
    def sort_abbr(a):
        if a.boe:
            s = a.boe.id
            s = s.split("-")
            s = (int(i) if i.isdigit() else i for i in s)
            return tuple(s)
        return tuple()

    abbrs = Abbr.load("config/abbr/02-ley.txt")
    abbrs = sorted(abbrs, key=sort_abbr, reverse=True)

    print(dedent('''
    ---
    title: Lesgilación
    ---

    Listado de Leyes referenciados en algún sitio de esta web.

    | ID | Rango | Nombre |
    |----|-------|--------|
    ''').strip())
    done = set()
    for a in abbrs:
        if a.url.url in done:
            continue
        done.add(a.url.url)
        if a.boe:
            b = a.boe
            print("| {boe} | {rango} | {title} | ".format(boe=b.id, rango=b.title, title=a._title))
        else:
            print("|  |  | {title} | ".format(title=a.titles[0]))
