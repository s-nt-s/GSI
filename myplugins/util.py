import subprocess
import sys
from urllib.parse import urlparse, urljoin
import posixpath

def run(*args, **kargv):
    output = subprocess.check_output(args, **kargv)
    output = output.decode(sys.stdout.encoding)
    return output


def get_dom(url):
    if url is None:
        return None
    dom = urlparse(url).netloc
    if len(dom)==0:
        return None
    if dom.endswith(".wikipedia.org"):
        return "wikipedia"
    if dom.startswith("www."):
        dom = dom[4:]
    return dom

def get_class_dom(url):
    dom = get_dom(url)
    if dom is None:
        return None
    dom = dom.replace(".", "_")
    return dom


def relurl(base, target, root=None):
    if root is None:
        root = "http://fakeroot.com/"
    s_base = urljoin(root, base)
    s_targ = urljoin(root, target)
    p_base = urlparse(s_base)
    p_targ = urlparse(s_targ)
    p_root = urlparse(root)
    if p_base.netloc != p_targ.netloc:
        return None
    if p_base.netloc != p_root.netloc:
        return None
    base_dir = '.'+posixpath.dirname(p_base.path)
    targ_pat = '.'+p_targ.path
    relpath = posixpath.relpath(targ_pat, start=base_dir)
    if relpath == target:
        return None
    return relpath
