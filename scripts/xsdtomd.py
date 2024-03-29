from xmlschema import XMLSchema, XsdElement, XsdType
from bs4 import BeautifulSoup
import requests
from functools import lru_cache
from .core.web import Web
from .core.util import write, clean_url, read
from textwrap import dedent
import re
import subprocess
from os import makedirs
import os
from csv import DictReader
import sys
from munch import Munch

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
xsddiagram = dname + "/../tools/xsddiagram.sh"

re_comment = re.compile(r"\s*<!--.*?-->\s*", re.DOTALL)

web = Web()

def run_cmd(*args):
    return subprocess.run(args)

def run_out(*args):
    output = subprocess.check_output(args)
    output = output.decode(sys.stdout.encoding)
    output = output.strip()
    return output

def run_xsddiagram(*args):
    arg = [str(a) for a in args if a is not None]
    args = [xsddiagram] + arg
    output = run_out(*args)
    cmd = [c.strip() for c in output.split("\n") if c.strip()]
    cmd = [c for c in cmd if c.startswith("$ ")]
    cmd = "\n".join(cmd)
    print(cmd)
    return cmd


def read_csv(*args, **kargv):
    for file in args:
        with open(file, "r") as f:
            for row in DictReader(f, **kargv):
                yield row

def read_table(*args, cols=None, no_null=None):
    if no_null is None:
        no_null = tuple()
    rows = []
    vals = {}
    for row in read_csv(*args, delimiter='\t'):
        if cols:
            row = {k:v for k,v in row.items() if k in cols}
        skip = False
        for k in no_null:
            skip = skip or row.get(k) in ("", None)
        if skip:
            continue
        for k, v in row.items():
            if k not in vals:
                vals[k]=set()
            vals[k].add(v)
        rows.append(row)

    del_col = set()
    for col, val in vals.items():
        val = tuple(val)
        if len(val)==1 and val[0] in ("", None):
            del_col.add(col)

    r = []
    for row in rows:
        row = {k:v for k,v in row.items() if k not in del_col}
        if row:
            r.append(row)

    return r

class XSD:
    def __init__(self, url):
        self.url = url

    @property
    @lru_cache(maxsize=None)
    def content(self):
        r = web.get(self.url)
        text = re_comment.sub("\n", r.text)
        text = text.strip()
        return text

    @property
    @lru_cache(maxsize=None)
    def schema(self):
        schema = XMLSchema(self.content, base_url=self.url, validation='lax')
        return schema

    @property
    @lru_cache(maxsize=None)
    def elements(self):
        names = set(str(e) for e in self.schema.elements)
        return tuple(sorted(names))

    @lru_cache(maxsize=None)
    def get_level(self, e):
        pass

class CrawlXSD:
    def __init__(self, salida):
        self.salida = salida

    def save(self, url):
        xsd = XSD(url)
        if len(xsd.elements)==0:
            print(url, "no tiene elementos")
            return
        print("#", url)
        name = url.rsplit("/", 1)[-1]
        name = name.rsplit(".", 1)[0]
        name = re.sub(r"\d+-", "", name)
        img = self.salida+name+"/"
        if os.path.isdir(img):
            return
        makedirs(img, exist_ok=True)

        cmds = []
        for e in xsd.elements:
            cmd = run_xsddiagram(e, img, url)
            cmds.append(cmd)
        title = str(name)
        if len(xsd.elements)==1:
            title = xsd.elements[0]+ " ({})".format(title)
        MD = [dedent('''
        ---
        title: {title}
        summary: "Fuente: [{curl}]({url})"
        ---
        ''').format(title=title, curl=clean_url(url), url=url).strip()+"\n"]
        if len(xsd.elements)>1:
            for e in elms:
                MD.append("* [{0}](#{0})".format(e))

        TXTS=[]
        for e, cmd in zip(xsd.elements, cmds):
            cmd = cmd.replace("$ ", "")
            cmd = re.sub(r"content/posts/xsd/(\S+?/)([^/\s]+)", r'<a href="\1\2">\2</a>', cmd)
            #cmd = re.sub(r"(https?://\S+)", r'<a href="\1">\1</a>', cmd)
            cmd = cmd.replace("xsddiagram", '<a href="http://regis.cosnier.free.fr/?page=XSDDiagram">xsddiagram</a>')
            MD.append('''<div class="widthscroll" id="{}">\n<pre><code>{}</code></pre>\n</div>'''.format(e, cmd))
            MD.append("\n![Diagrama de {1} ({0}.xsd)]({0}/{1}.png)\n".format(name, e))
            TXTS.append(img+"/"+e+".txt")

        rows = read_table(*TXTS, cols=('NAME', 'COMMENT'), no_null=('COMMENT', ))
        if rows and False:
            head = rows[0].keys()
            MD.append("| " + " | ".join(head) + " |")
            MD.append((("|:----")*len(head))+"|")
            for row in rows:
                row['COMMENT']="<div><pre><code>{}</code></pre></div>".format(row['COMMENT'])
                row = row.values()
                MD.append("| " + " | ".join(row) + " |")
            MD.append("\nTabla 1: Comentarios de los elementos de {}.xsd".format(name))

        MD.append("")
        MD.append("```console\ncurl -L {}\n```".format(url))
        MD.append("```xml\n{}\n```".format(xsd.content))

        write(self.salida+name+".md", "\n".join(MD), encoding='utf-8-sig')

if __name__ == "__main__":
    xsd = CrawlXSD("content/posts/xsd/")
    web.get("https://administracionelectronica.gob.es/pae_Home/pae_Estrategias/pae_Interoperabilidad_Inicio/pae_Normas_tecnicas_de_interoperabilidad.html#EXPEDIENTEELECTRONICO")
    urls = set()
    for url in web.soup.findAll("a"):
        url = url.attrs.get("href")
        if url is not None and url.endswith(".xsd"):
            urls.add(url)
    for url in sorted(urls):
        xsd.save(url)
