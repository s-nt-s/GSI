import re
from os import makedirs
from os.path import dirname
from pathlib import Path
from urllib.parse import urlparse

import bs4
import yaml
from markdown import markdown
from munch import Munch
from weasyprint import CSS, HTML

re_head = re.compile(r"<(h[1-6])>\s*(.*?)\s*</\1>", re.MULTILINE)


def read(file):
    file = str(file)
    ext = file.rsplit(".")[-1].lower()
    if ext in ("yml", "yaml"):
        with open(file, "r") as f:
            yml = yaml.load(f, Loader=yaml.FullLoader)
            return Munch.fromDict(yml)
    if ext in ("md", ):
        md = Munch(
            meta=None,
            md=None,
            html=None
        )
        with open(file, "r") as f:
            for l in f.readlines():
                sl = l.strip()
                if md.md is not None:
                    md.md.append(l)
                    continue
                if sl == '---':
                    if md.meta is None:
                        md.meta = []
                    else:
                        md.md = []
                    continue
                md.meta.append(l)
        md.meta = "".join(md.meta)
        md.md = "".join(md.md)
        md.html = markdown(md.md)
        md.meta = yaml.safe_load(md.meta)
        md.meta = Munch.fromDict(md.meta)
        return md

    with open(file, "r") as f:
        return f.read()


def write(file, text):
    dir = dirname(file)
    makedirs(dir, exist_ok=True)
    with open(file, "w") as f:
        f.write(text)


def rcglob(root, *args):
    ok = []
    ko = []
    root = Path(root)
    for a in args:
        if a.startswith("!"):
            ko.extend(root.rglob("*."+a[1:]))
        else:
            for i in root.rglob("*."+a):
                if i not in ko:
                    ok.append(i)
    return sorted(ok)


def clean_url(url):
    spl = url.split("://", 1)
    if len(spl) == 2:
        url = spl[1]
    if url.lower().startswith("www") and "." in url[3:5]:
        url = url.split(".", 1)[1]
    url = url.rstrip("/")
    return url


def url_key(url):
    p = urlparse(url)
    dom = p.netloc
    if dom.lower().startswith("www") and "." in url[4:6]:
        dom = dom.split(".", 1)[1]
    r = (
        tuple(reversed(dom.split("."))),
        p.path,
        p.query,
        p.fragment,
        p.scheme,
        clean_url(url)
    )
    return r
