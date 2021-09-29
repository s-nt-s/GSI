import subprocess
import sys
from urllib.parse import urlparse, urljoin
import posixpath
import unidecode
import yaml

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
    if p_targ.params:
        relpath = relpath+';'+p_targ.params
    if p_targ.query:
        relpath = relpath+'?'+p_targ.query
    if p_targ.fragment:
        relpath = relpath+'#'+p_targ.fragment
    if relpath == target:
        return None
    return relpath
