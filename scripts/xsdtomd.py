from xmlschema import XMLSchema
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

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
xsddiagram = dname + "/../tools/xsddiagram.sh"

re_comment = re.compile(r"\s*<!--.*?-->\s*", re.DOTALL)

def run_cmd(*args):
    return subprocess.run(args)

def run_xsddiagram(*args):
    arg = [str(a) for a in args]
    args = [xsddiagram] + arg
    output = subprocess.check_output(args)
    output = output.decode('utf-8')
    output = output.strip()
    comand = output.split("\n")[0]
    print(comand)
    return comand

def read_csv(*args, cols=None):
    rows = []
    vals = {}
    for file in args:
        with open(file, "r") as f:
            for row in DictReader(f, delimiter='\t'):
                for k, v in row.items():
                    if k not in vals:
                        vals[k]=set()
                    vals[k].add(v)
                rows.append(row)
    del_col = set()
    for col, val in vals.items():
        val = tuple(val)
        if (cols is not None and col not in cols) or (len(val)==1 and val[0] in ("", None)):
            del_col.add(col)
    r = []
    for row in rows:
        row = {k:v for k,v in row.items() if k not in del_col}
        if row:
            r.append(row)
    return r

class XSD:
    def __init__(self, salida):
        self.s = Web()
        self.salida = salida

    @lru_cache(maxsize=None)
    def get_content(self, url):
        r = self.s.get(url)
        text = re_comment.sub("\n", r.text)
        text = text.strip()
        return text

    @lru_cache(maxsize=None)
    def get_elements(self, url):
        xml = self.get_content(url)
        schema = XMLSchema(xml, base_url=url, validation='skip')
        names = set(str(e) for e in schema.elements)
        return tuple(sorted(names))

    def save(self, url):
        elms = self.get_elements(url)
        if len(elms)==0:
            print(url, "no tiene elementos")
            return
        name = url.rsplit("/", 1)[-1]
        name = name.rsplit(".", 1)[0]
        img = self.salida+name+"/"
        makedirs(img, exist_ok=True)

        cmds = []
        for e in elms:
            levels = 6
            if (name, e) == ("IndiceContenidoExpedienteEni", "IndiceContenido"):
                levels = 4
            elif (name, e) == ("IndiceExpedienteEni", "indice"):
                levels = 5
            elif (name, e) == ("expedienteEni", "expediente"):
                pass
            cmd = run_xsddiagram(e, img, url) # levels
            cmds.append(cmd)
        title = str(name)
        if len(elms)==1:
            title = elms[0]+ " ({})".format(title)
        MD = [dedent('''
        ---
        title: {title}
        summary: "Fuente: [{curl}]({url})"
        ---
        ''').format(title=title, curl=clean_url(url), url=url).strip()+"\n"]
        if len(elms)>1:
            for e in elms:
                MD.append("* [{0}](#{0})".format(e))

        TXTS=[]
        for e, cmd in zip(elms, cmds):
            cmd = cmd.replace("$ ", "")
            cmd = re.sub(r"content/posts/xsd/(\S+?/)([^/\s]+)", r'<a href="\1\2">\2</a>', cmd)
            #cmd = re.sub(r"(https?://\S+)", r'<a href="\1">\1</a>', cmd)
            cmd = cmd.replace("xsddiagram", '<a href="http://regis.cosnier.free.fr/?page=XSDDiagram">xsddiagram</a>')
            MD.append('''<div class="widthscroll" id="{}">\n<pre><code>{}</code></pre>\n</div>'''.format(e, cmd))
            MD.append("\n![Diagrama de {1} ({0}.xsd)]({0}/{1}.png)\n".format(name, e))
            TXTS.append(img+"/"+e+".txt")

        rows = read_csv(*TXTS, cols=('NAME', 'COMMENT'))
        rows = [r for r in row if r.get('COMMENT')]
        if rows:
            head = rows[0].keys()
            MD.append("| " + " | ".join(head) + " |")
            MD.append((("|:----")*len(head))+"|")
            for row in rows:
                row = row.values()
                MD.append("| " + " | ".join(row) + " |")
            MD.append("\nTabla 1: Comentarios de los elementos de {}.xsd".format(name))

        MD.append("")
        MD.append("```console\ncurl -L {}\n```".format(url))
        MD.append("```xml\n{}\n```".format(self.get_content(url)))

        write(self.salida+name+".md", "\n".join(MD), encoding='utf-8-sig')

if __name__ == "__main__":
    s = Web()
    xsd = XSD("content/posts/xsd/")
    xsd.s.get("https://administracionelectronica.gob.es/pae_Home/pae_Estrategias/pae_Interoperabilidad_Inicio/pae_Normas_tecnicas_de_interoperabilidad.html#EXPEDIENTEELECTRONICO")
    urls = set()
    for url in xsd.s.soup.findAll("a"):
        url = url.attrs.get("href")
        if url is not None and url.endswith(".xsd"):
            urls.add(url)
    for url in sorted(urls):
        xsd.save(url)
