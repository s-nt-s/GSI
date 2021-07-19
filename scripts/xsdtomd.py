from xmlschema import XMLSchema
from bs4 import BeautifulSoup
import requests
from functools import lru_cache
from .core.web import Web
from .core.util import write, clean_url
from textwrap import dedent
import re
import subprocess
from os import makedirs

re_comment = re.compile(r"\s*<!--.*?-->\s*", re.DOTALL)

def run_cmd(*args):
    print(*args)
    return subprocess.run(args)
    output = subprocess.check_output(args)
    output = output.decode('utf-8')
    return output

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

        for e in elms:
            levels = 6
            if (name, e) == ("IndiceContenidoExpedienteEni", "IndiceContenido"):
                levels = 4
            elif (name, e) == ("IndiceExpedienteEni", "indice"):
                levels = 5
            elif (name, e) == ("expedienteEni", "expediente"):
                pass
            run_cmd("xsddiagram", url, "-y", "-r", e, "-e", str(levels), "-o", img+e+".svg", "-o", img+e+".png")
        title = str(name)
        if len(elms)==1:
            title = elms[0]+ " ({})".format(title)
        MD = [dedent('''
        ---
        title: {}
        ---
        ''').format(title).strip()+"\n"]
        if len(elms)==1:
            MD.append("Esquema `{}` - [{}]({})\n".format(elms[0], clean_url(url), url))
        else:
            MD.append("Esquema [{}]({})\n".format(clean_url(url), url))
        if len(elms)>1:
            for e in elms:
                MD.append("* [{0}](#{0})".format(e))

        MD.append("```xml\n{}\n```".format(self.get_content(url)))

        for e in elms:
            MD.append("\n![{0}]({0}/{1}.png){{#{1}}}\n".format(name, e))

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
