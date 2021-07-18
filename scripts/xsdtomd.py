from xmlschema import XMLSchema
import requests
from functools import lru_cache
from .core.web import Web
from .core.util import write, clean_url
from textwrap import dedent

import subprocess

def run_cmd(*args):
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
        return r.text

    @lru_cache(maxsize=None)
    def get_elements(self, url):
        schema = XMLSchema(self.get_content(url), base_url=url)
        names = set(str(e) for e in schema.elements)
        return tuple(sorted(names))

    def save(self, url):
        elms = self.get_elements(url)
        if len(elms)==0:
            print(url, "no tiene elementos")
            return
        name = url.rsplit("/", 1)[-1]
        name = name.rsplit(".", 1)[0]
        MD = [dedent('''
        ---
        title: {}
        ---
        ''').format(name).strip()+"\n"]
        MD.append("Esquema [{}]({})".format(clean_url(url), url))

        write(salida+name+".md", "\n".join(MD))



if __name__ == "__main__":
    s = Web()
    s.get("https://administracionelectronica.gob.es/pae_Home/pae_Estrategias/pae_Interoperabilidad_Inicio/pae_Normas_tecnicas_de_interoperabilidad.html#EXPEDIENTEELECTRONICO")
    for url in s.soup.findAll("a"):
        url = url.attrs.get("href")
        if url is not None and url.endswith(".xsd"):
            xsd = XSD("content/posts/xsd/")
