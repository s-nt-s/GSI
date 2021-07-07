from os import walk
from os.path import join, relpath
from urllib.parse import urlparse, urljoin

import bs4
from joblib import Parallel, delayed
from pelican import signals

import posixpath

def relurl(base, target):
    fake_root = "http://fakeroot.com/"
    s_base = urljoin(fake_root, base)
    s_targ = urljoin(fake_root, target)
    p_base = urlparse(s_base)
    p_targ = urlparse(s_targ)
    p_root = urlparse(fake_root)
    if p_base.netloc != p_targ.netloc:
        return None
    if p_base.netloc != p_root.netloc:
        return None
    base_dir = '.'+posixpath.dirname(p_base.path)
    targ_pat = '.'+p_targ.path
    relpath = posixpath.relpath(target, start=base_dir)
    if relpath == target:
        return None
    return relpath

def get_href(html, *tags):
    if len(tags)==0:
        tags = ["link", "a", "script", "img", "iframe", "frame"]
    for a in html.findAll(tags):
        attr = "href" if a.name in ("a", "link") else "src"
        href = a.attrs.get(attr)
        if href is not None:
            yield a, attr, href

def parallel_mod_html(pelican_object):
    html_files = []
    for dirpath, _, filenames in walk(pelican_object.settings['OUTPUT_PATH']):
        html_files += [join(dirpath, name)
                       for name in filenames if name.endswith('.html') or name.endswith('.htm')]

    Parallel(n_jobs=-1)(delayed(mod_html)(pelican_object, filepath) for filepath in html_files)

def set_target(html, SITEURL, DOMAIN):
    if DOMAIN is None:
        return False
    ok = False
    for a, attr, href in get_href(html, "a"):
        if "target" not in a.attrs:
            a_dom = urlparse(href).netloc
            if len(a_dom) > 0 and a_dom != DOMAIN:
                a.attrs["target"] = "_blank"
                ok = True
    return ok

def move_script(html):
    ok = False
    head = html.find("head")
    for script in html.select("body script"):
        head.append(script)
        ok = True
    for script in html.select("body link[href]"):
        head.append(script)
        ok = True
    return ok

def rel_url(html, rel_file):
    ok = False
    for a, attr, href in get_href(html):
        slp = href.split("://", 1)
        if len(slp)==2 and slp[0].lower() in ("http", "https"):
            new_url = relurl(rel_file, href)
            if new_url is not None:
                a.attrs[attr] = new_url
                ok = True
    return ok

def fix_href(html):
    ok = False
    for a, attr, href in get_href(html, "a"):
        if href.endswith("//"):
            a.attrs[attr] = href.rstrip("/") + "/"
            ok = True
    return ok

def mod_html(pelican_object, filename):
    rel_file = relpath(filename, pelican_object.settings['OUTPUT_PATH'])
    SITEURL = pelican_object.settings.get('SITEURL', None)
    DOMAIN = urlparse(SITEURL).netloc if SITEURL else None

    with open(filename, encoding='utf-8') as f:
        html = bs4.BeautifulSoup(f, "lxml")

    ok = True in (
        move_script(html),
        fix_href(html),
        set_target(html, SITEURL, DOMAIN),
        rel_url(html, rel_file)
    )

    if ok:
        with open(filename, "w", encoding='utf-8') as f:
            f.write(str(html))


def register():
    signals.finalized.connect(parallel_mod_html)
