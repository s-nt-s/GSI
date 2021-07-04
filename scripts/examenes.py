import re
from munch import Munch
import json
from textwrap import dedent
from .core.util import write
from .core.web import Web

import urllib3
urllib3.disable_warnings()

re_sp = re.compile(r"\s+")
re_conv = re.compile(r"^.*/([^\-/]+)-([12]\d{3})-[^\-/]+-(libre|interna)$")

def get_text(n):
    if n is None:
        return None
    txt = n.get_text()
    txt = re_sp.sub(" ", txt)
    return txt.strip()

OPOS={k.lower():v for v, k in (
("A1", "Cuerpo Superior de Sistemas y Tecnologías de la Información de la Administración del Estado"),
("A2", "Cuerpo de Gestión de Sistemas e Informática de la Administración del Estado"),
("C1", "Cuerpo de Técnicos Auxiliares de Informática de la Administración del Estado")
)}

class CrawlExamenes:
    def __init__(self, salida, root="https://sede.inap.gob.es/procesos-selectivos"):
        self.w = Web(verify=False)
        self.root = root
        self.salida = salida
        self.opos = self.get_opos()

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
                codigo=url.rsplit("/", 1)[-1].upper()
                opos[grupo]=Munch(
                    codigo=codigo,
                    grupo=grupo,
                    titulo=titulo,
                    url=url,
                    convocatorias=self.get_convocatorias(grupo, url)
                )
        opos={k:v for k,v in sorted(opos.items(), key=lambda x:x[0])}
        return opos

    def get_convocatorias(self, grupo, url):
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
                examenes=self.get_examenes(grupo, ingreso, url),
                tipo=ingreso[0].upper()
            ))
        conv = sorted(conv, key=lambda x:(x.year, x.ingreso))
        return conv

    def get_examenes(self, grupo, ingreso, url):
        exa = []
        self.w.get(url)
        url_ej={}
        lst_ej=None
        for n in self.w.soup.select("div.journal-content-article *"):
            if n.name == "a":
                if lst_ej is not None:
                    url_ej[n.attrs["href"]] = lst_ej
                continue
            txt = get_text(n)
            txt = txt.lower().strip(".")
            txt = txt.split()
            if len(txt)==2:
                if txt[1]=="ejercicio":
                    lst_ej = [None, 'primer', 'segundo', 'tercer', 'cuarto'].index(txt[0])
                    continue
                if txt[0]=="ejercicio" and txt[1] in ("único", "ùnico"):
                    lst_ej = 1
                    continue

        links = list(self.w.soup.select("div.journal-content-article a"))
        for a in links:
            url = a.attrs["href"].strip()
            txt = get_text(a).lower().rstrip(".")
            tipo = None
            ejercicio = url_ej.get(url)
            if ejercicio is None:
                continue
            if ("cuestionario" in txt) or grupo=="C1" or ejercicio == 1:
                tipo = "test"
            elif grupo == "A2":
                if ((ejercicio==2 and ingreso=="interna") or (ejercicio==3 and ingreso=="libre")):
                    tipo = "supuesto"
            elif grupo == "A1":
                pass
            if txt in ("cuestionario", "enunciado del ejercicio", "cuestionario ejercicio único", "texto del ejercicio", "enunciado del cuarto ejercicio y anexos"):
                exa.append(Munch(
                    ejercicio=ejercicio,
                    url=url,
                    tipo=tipo,
                    solucion=None,
                ))
            elif txt in ("modelo a", "modelo b"):
                li = a.find_parent("li").find_parent("li")
                li = get_text(li)
                li = li.lower()
                if li.startswith("plantillas definitivas de respuestas"):
                    if txt == "modelo a":
                        exa.append(Munch(
                            ejercicio=ejercicio,
                            url=None,
                            tipo="test",
                            solucion=None,
                            modelo=Munch(a=url)
                        ))
                    else:
                        b = txt.split()[1]
                        exa[-1].modelo[b] = url
            elif txt in ("plantilla definitiva de respuestas", "plantilla definitiva"):
                li = a.find_parent("li")
                li = get_text(li)
                if li and "examen extraordinario" in li:
                    if len(exa)>0 and exa[-1].ejercicio==url_ej[url]:
                        exa[-1].ejercicio += 0.1
                    exa.append(Munch(
                        ejercicio=ejercicio+0.2,
                        url=url,
                        tipo="test",
                        solucion=url,
                    ))
                elif len(exa)==0 or not exa[-1].tipo=="test":
                    exa.append(Munch(
                        ejercicio=url_ej[url],
                        url=url,
                        tipo="test",
                        solucion=url,
                    ))
                else:
                    exa[-1].solucion = url
        exa = sorted(exa, key=lambda x:x.ejercicio)
        return exa

    def save(self):
        SH=[dedent('''
        #!/bin/bash
        function dwn() {
            mkdir -p "${1%/*}"
            wget -q --no-check-certificate -O "$1" $2
            if [ $? -eq 0 ]; then
                echo "[OK] $1"
            else
                echo "[KO] $1 $2"
            fi
        }
        function mrg() {
            PR=$(echo "$1" | sed 's|R|P|')
            if [ -f "$PR" ]; then
                TD=$(echo "$1" | sed 's|R||')
                if [ ! -f "$TD" ]; then
                    pdfunite "$PR" "$1" "$TD" 2>/dev/null
                    if [ $? -eq 0 ]; then
                        rm "$1"
                        rm "$PR"
                        echo "[MV] ${TD#*/} = $(basename $1) + $(basename $PR)"
                    fi
                fi
            fi
        }
        function dup() {
            OT=$(echo "$1" | sed 's|L|I|')
            if [ -f "$OT" ]; then
                cmp "$1" "$OT" > /dev/null
                if [ $? -eq 0 ]; then
                    FL=$(echo "$1" | sed 's|L||')
                    mv "$1" "$FL"
                    rm "$OT"
                    echo "[MV] ${FL#*/} = $(basename $1) = $(basename $OT)"
                fi
            fi
        }
        mkdir -p examenes
        cd examenes
        ''').strip()]
        MD=[dedent('''
        ---
        title: Examenes de convocatorias anteriores
        summary: Examenes de [convocatorias TAI/GSI/CSSTIC]({inap}) anteriores.
        ---
        '''.format(inap=self.root)).strip()]
        for grupo, data in self.get_opos().items():
            MD.append("\n# [{codigo} {titulo}]({url})\n".format(**dict(data)))
            SH.append("\n# {grupo} {codigo}\n".format(**dict(data)))
            for conv in data.convocatorias:
                MD.append("* {grupo} [{year} - {ingreso}]({url})".format(grupo=data.codigo, **dict(conv)))
                for exa in conv.examenes:
                    mam_fl="{grupo}/{year}-{ejercicio}{tipo}".format(grupo=data.grupo, ejercicio=exa.ejercicio, **dict(conv))
                    dwn_sh="dwn "+mam_fl
                    if exa.get("modelo") is not None:
                        modelos = ", ".join(("[modelo {} + solución]({})".format(k.upper(), v) for k,v in sorted(exa.modelo.items())))
                        MD.append("    * Ejercicio {ejercicio}: ".format(**dict(exa))+modelos)
                        for m, u in sorted(exa.modelo.items()):
                            SH.append(dwn_sh+"_{modelo}.pdf '{url}'".format(url=u, modelo=m))
                        continue
                    if exa.solucion is None:
                        MD.append("    * [Ejercicio {ejercicio}]({url})".format(**dict(exa)))
                        SH.append(dwn_sh+".pdf '{url}'".format(**dict(exa)))
                    elif exa.solucion == exa.url:
                        MD.append("    * [Ejercicio {ejercicio} + solución]({url})".format(**dict(exa)))
                        SH.append(dwn_sh+".pdf '{url}'".format(**dict(exa)))
                    else:
                        MD.append("    * [Ejercicio {ejercicio}]({url}) + [solución]({solucion})".format(**dict(exa)))
                        SH.append(dwn_sh+"P.pdf '{url}'".format(**dict(exa)))
                        SH.append(dwn_sh+"R.pdf '{solucion}'".format(**dict(exa)))
        SH.append(dedent('''
            find . -name '*L*' -type f -print0 |
            while IFS= read -r -d '' FL; do
              dup "$FL"
            done
            find . -name '*R*' -type f -print0 |
            while IFS= read -r -d '' FL; do
              mrg "$FL"
            done
        '''))
        MD.append("\n[Script para descargar](examenes.sh)")
        write(self.salida+"examenes.md", "\n".join(MD))
        write(self.salida+"examenes.sh", "\n".join(SH))

if __name__ == "__main__":
    c = CrawlExamenes("content/posts/ejercicios/")
    c.save()