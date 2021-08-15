import posixpath
from os import walk
from os.path import join, relpath
from urllib.parse import urljoin, urlparse

import bs4
from joblib import Parallel, delayed
from pelican import signals
from .core.util import relurl


class ModHtml:
    def __init__(self, settings, filename, soup=None):
        self.settings = settings
        self.soup = soup
        self.is_changed = False
        self.filename = filename
        self.siteurl = self.settings.get('SITEURL', None)
        if self.siteurl and not self.siteurl.endswith("/"):
            self.siteurl = self.siteurl + "/"
        if self.soup is None:
            with open(self.filename, encoding='utf-8') as f:
                self.soup = bs4.BeautifulSoup(f, "lxml")

    @property
    def rel_file(self):
        return relpath(self.filename, self.settings['OUTPUT_PATH'])

    @property
    def domain(self):
        site_url = self.settings.get('SITEURL', None)
        if site_url is None:
            return None
        return urlparse(site_url).netloc

    def get_href(self, *tags):
        if len(tags) == 0:
            tags = ["link", "a", "script", "img", "iframe", "frame"]
        for a in self.soup.findAll(tags):
            attr = "href" if a.name in ("a", "link") else "src"
            href = a.attrs.get(attr)
            if href is not None:
                yield a, attr, href

    def move_script(self):
        head = self.soup.find("head")
        for script in self.soup.select("body script"):
            head.append(script)
            self.is_changed = True
        for script in self.soup.select("body link[href]"):
            head.append(script)
            self.is_changed = True

    def set_target(self):
        if self.domain is None:
            return
        for a, attr, href in self.get_href("a"):
            if "target" not in a.attrs:
                a_dom = urlparse(href).netloc
                if len(a_dom) > 0 and a_dom != self.domain:
                    a.attrs["target"] = "_blank"
                    self.is_changed = True

    def rel_url(self):
        for a, attr, href in self.get_href():
            slp = href.split("://", 1)
            if len(slp) == 2 and slp[0].lower() in ("http", "https"):
                new_url = relurl(self.rel_file, href, root=self.siteurl)
                if new_url is not None:
                    a.attrs[attr] = new_url
                    self.is_changed = True


    def fix_href(self):
        for a, attr, href in self.get_href("a"):
            if href.endswith("//"):
                a.attrs[attr] = href.rstrip("/") + "/"
                self.is_changed = True


def parallel_mod_html(pelican_object):
    html_files = []
    for dirpath, _, filenames in walk(pelican_object.settings['OUTPUT_PATH']):
        html_files += [join(dirpath, name)
                       for name in filenames if name.endswith('.html') or name.endswith('.htm')]

    Parallel(n_jobs=-1)(delayed(mod_html)(pelican_object, filepath)
                        for filepath in html_files)


def mod_html(pelican_object, filename):
    mod = ModHtml(pelican_object.settings, filename)
    mod.move_script()
    mod.fix_href()
    mod.set_target()
    mod.rel_url()

    if mod.is_changed:
        with open(filename, "w", encoding='utf-8') as f:
            f.write(str(mod.soup))


def register():
    signals.finalized.connect(parallel_mod_html)
