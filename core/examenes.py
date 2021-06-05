from .web import Web

import re
from munch import Munch
import json
from textwrap import dedent
from .util import write

import urllib3
urllib3.disable_warnings()

re_sp = re.compile(r"\s+")
re_conv = re.compile(r"^.*/([^\-/]+)-([12]\d{3})-[^\-/]+-(libre|interna)$")

def get_text(n):
    txt = n.get_text()
    txt = re_sp.sub(" ", txt)
    return txt.strip()

OPOS={k.lower():v for v, k in (
("A1", "Cuerpo Superior de Sistemas y Tecnologías de la Información de la Administración del Estado"),
("A2", "Cuerpo de Gestión de Sistemas e Informática de la Administración del Estado"),
("C1", "Cuerpo de Técnicos Auxiliares de Informática de la Administración del Estado")
)}

class CrawlExamenes:
    def __init__(self, root="https://sede.inap.gob.es/procesos-selectivos", salida="docs/"):
        self.w = Web(verify=False)
        self.root = root
        self.salida = salida

    def get_opos(self):
        opos = {}
        self.w.get(self.root)
        links = list(self.w.soup.select("div.nav-menu a"))
        for a in links:
            titulo = get_text(a)
            key = titulo.lower()
            grupo = OPOS.get(key)
            if grupo:
                url = a.attrs["href"]
                opos[grupo]=Munch(
                    codigo=url.rsplit("/", 1)[-1].upper(),
                    grupo=grupo,
                    titulo=titulo,
                    url=url,
                    convocatorias=self.get_convocatorias(url)
                )
        opos={k:v for k,v in sorted(opos.items(), key=lambda x:x[0])}
        return opos

    def get_convocatorias(self, url):
        conv = []
        self.w.get(url)
        links = list(self.w.soup.select("div.journal-content-article a"))
        for a in links:
            url = a.attrs["href"].strip()
            m = re_conv.match(url)
            if m is None:
                continue
            cod, year, ingreso = m.groups()
            conv.append(Munch(
                year=int(year),
                ingreso=ingreso,
                url=url,
                examenes=self.get_examenes(url)
            ))
        return conv

    def get_examenes(self, url):
        exa = []
        self.w.get(url)
        links = list(self.w.soup.select("div.journal-content-article a"))
        i = 0
        for a in links:
            url = a.attrs["href"].strip()
            txt = get_text(a).lower()
            if txt in ("cuestionario", "enunciado del ejercicio"):
                i = i +1
                exa.append(Munch(
                    ejercicio=i,
                    url=url,
                    test=(txt == "cuestionario"),
                    solucion=None,
                ))
            elif txt in ("plantilla definitiva de respuestas", ):
                if len(exa)==0 or not exa[-1].test:
                    i = i +1
                    exa.append(Munch(
                        ejercicio=i,
                        url=url,
                        test=True,
                        solucion=url,
                    ))
                else:
                    exa[-1].solucion = url

        return exa

    def save(self):
        MD=[dedent('''
        ---
        title: Examenes de convocatorias anteriores
        ---
        <div class="alert">
            <a href="{inap}" target="_blank">Convocatorias</a>
        </div>
        '''.format(inap=self.root))+"\n"]
        for grupo, data in self.get_opos().items():
            MD.append("\n# [{codigo} {titulo}]({url})\n".format(**dict(data)))
            for conv in sorted(data.convocatorias, key=lambda x:(x.year, x.ingreso)):
                MD.append("* [{year} - {ingreso}]({url})".format(**dict(conv)))
                for exa in sorted(conv.examenes, key=lambda x:x.ejercicio):
                    MD.append("    * [Ejerecicio {ejercicio}]({url})".format(**dict(exa)))
                    if exa.solucion and exa.solucion != exa.url:
                        MD[-1] == MD[-1] + " + [solucion]({})".format(exa.solucion)

        write(self.salida+"examenes.md", "\n".join(MD))

if __name__ == "__main__":
    c = CrawlExamenes()
    c.save()
    #print(json.dumps(c.get_opos(), indent=2))
