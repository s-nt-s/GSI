import re
from textwrap import dedent

import urllib3
from munch import Munch
from functools import lru_cache, total_ordering

from .core.util import write
from .core.web import Web
from functools import lru_cache

urllib3.disable_warnings()

re_sp = re.compile(r"\s+")
re_conv = re.compile(r"^.*/([^\-/]+)-([12]\d{3})-[^\-/]+-(libre|interna)$")


def get_text(n):
    if n is None:
        return None
    txt = n.get_text()
    txt = re_sp.sub(" ", txt)
    return txt.strip()


OPOS = {k.lower(): v for v, k in (
    ("A1", "Cuerpo Superior de Sistemas y Tecnologías de la Información de la Administración del Estado"),
    ("A2", "Cuerpo de Gestión de Sistemas e Informática de la Administración del Estado"),
    ("C1", "Cuerpo de Técnicos Auxiliares de Informática de la Administración del Estado")
)}

W = Web(verify=False)

INAP_URL="https://sede.inap.gob.es/procesos-selectivos"
BAQU_URL="http://www.baquedano.es/todo.html"

DWNSH=dedent('''
#!/bin/bash
function dwn() {
    DR=$(dirname "$1")
    if [ ! -z "$DR" ] && [ "$DR" != "." ] && [ ! -e "$DR" ]; then
        mkdir -p "DR"
    fi
    fil="$1"
    url="$2"
    ext="${url##*.}"
    if [[ " pdf doc docx rtf " =~ " ${ext} " ]]; then
        fil="${fil}.${ext}"
    else
        fil="${fil}.pdf"
    fi
    wget -q --no-check-certificate -O "$fil" $url
    if [ $? -eq 0 ]; then
        echo "[OK] $fil"
    else
        echo "[KO] $fil $url"
    fi
}
''').strip()

@total_ordering
class MyMunch(Munch):
    def __hash__(self):
        return hash(self.key)

    def __eq__(self, o):
        return self.key == o.key

    def __lt__(self, o):
        return self.key.__lt__(o.key)

    def asdict(self):
        return dict(self)

class Examen(MyMunch):
    def __init__(self, *args, **kvargs):
        super().__init__(*args, **kvargs)
        self.bloque=None

    @property
    def key(self):
        return (self.convocatoria.oposicion.grupo, self.convocatoria.year, self.convocatoria.ingreso, self.ejercicio)

    @property
    def year(self):
        return self.convocatoria.year

    @property
    def ingreso(self):
        return self.convocatoria.ingreso

    @property
    def grupo(self):
        return self.convocatoria.oposicion.grupo

class Convocatoria(MyMunch):

    @property
    @lru_cache(maxsize=None)
    def examenes(self):
        exa = []
        W.get(self.url)
        url_ej = {}
        lst_ej = None
        for n in W.soup.select("div.journal-content-article *"):
            if n.name == "a":
                if lst_ej is not None:
                    url_ej[n.attrs["href"]] = lst_ej
                continue
            txt = get_text(n)
            txt = txt.lower().strip(".")
            txt = txt.split()
            if len(txt) == 2:
                if txt[1] == "ejercicio":
                    lst_ej = [None, 'primer', 'segundo',
                              'tercer', 'cuarto'].index(txt[0])
                    continue
                if txt[0] == "ejercicio" and txt[1] in ("único", "ùnico"):
                    lst_ej = 1
                    continue

        links = list(W.soup.select("div.journal-content-article a"))
        for a in links:
            url = a.attrs["href"].strip()
            txt = get_text(a).lower().rstrip(".")
            tipo = None
            ejercicio = url_ej.get(url)
            if ejercicio is None:
                continue
            if self.oposicion.grupo == "C1" or ejercicio == 1:
                tipo = "test"
            elif self.oposicion.grupo == "A2":
                if ((ejercicio == 2 and self.ingreso == "interna") or (ejercicio == 3 and self.ingreso == "libre")):
                    tipo = "supuesto"
            elif self.oposicion.grupo == "A1":
                pass
            if tipo is None and ("cuestionario" in txt):
                tipo = "test"
            if txt in ("cuestionario primer ejercicio", "cuestionario", "enunciado del ejercicio", "cuestionario ejercicio único", "texto del ejercicio", "enunciado del cuarto ejercicio y anexos"):
                exa.append(Examen(
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
                        exa.append(Examen(
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
                    if len(exa) > 0 and exa[-1].ejercicio == url_ej[url]:
                        exa[-1].ejercicio += 0.1
                    exa.append(Examen(
                        ejercicio=ejercicio+0.2,
                        url=url,
                        tipo="test",
                        solucion=url,
                    ))
                elif len(exa) == 0 or not exa[-1].tipo == "test":
                    exa.append(Examen(
                        ejercicio=url_ej[url],
                        url=url,
                        tipo="test",
                        solucion=url,
                    ))
                else:
                    exa[-1].solucion = url
        for e in exa:
            e.convocatoria = self
        return sorted(exa)

    @property
    def key(self):
        return (self.oposicion.key, self.year, self.ingreso)


class BaqueConvocatoria(MyMunch):
    def __init__(self, *args, **kvargs):
        super().__init__(*args, **kvargs)
        for e in self.examenes:
            e.convocatoria = self
        self.examenes = sorted(self.examenes)

    @property
    def key(self):
        return (self.oposicion.key, self.year, self.ingreso)

class BaqueExamenA2(Examen):
    def __init__(self, *args, **kvargs):
        super().__init__(*args, **kvargs)
        self.solucion=None
        self.bloque = self.get_bloque()

    def asdict(self):
        d=dict(self)
        d['grupo'] = self.grupo
        d['ingreso'] = self.ingreso
        d['ejercicio'] = self.ejercicio
        d['tipo'] = self.tipo
        return d

    def get_bloque(self):
        if self.url in ("http://www.zonacondeduque.com/B_ejer_2_promo_AGE_2008.pdf", "http://www.baquedano.es/B_supu_IV_promo_AGE_2008.pdf"):
            return {
                "3": "http://www.zonacondeduque.com/B_ejer_2_promo_AGE_2008.pdf",
                "4": "http://www.baquedano.es/B_supu_IV_promo_AGE_2008.pdf"
            }
        return None

    @property
    def isExcluir(self):
        if self.url == "http://www.zonacondeduque.es/B_aclaracion_ejer_1_promo_AGE_2010.pdf":
            return True
        if self.url == "http://www.baquedano.es/B_supu_IV_promo_AGE_2008.pdf":
            # Es el bloque 4 de otro
            return True
        return False

    @property
    def grupo(self):
        return "A2"

    @property
    def ingreso(self):
        t = self.titulo.lower()
        if "libre" in t:
            return "libre"
        if "interna" in t:
            return "interna"
        if "libre" in self.url:
            return "libre"
        if "promo" in self.url:
            return "interna"
        if self.url in ("http://www.zonacondeduque.com/B_ejer_2_AGE_2006.pdf", "http://www.baquedano.es/plant_prov.pdf", "http://www.zonacondeduque.com/B_ejer_2_AGE_2005.pdf", "http://www.zonacondeduque.com/B_ejer_sol_1_AGE_2005.pdf" , "http://www.zonacondeduque.com/B_ejer_sol_1_AGE_2004.pdf", "http://www.zonacondeduque.com/B_ejer_3_AGE_2004.pdf"):
            return "libre"
        raise Exception("ingreso no encontrado en: %s - %s " % (self.year, self.titulo))

    @property
    def ejercicio(self):
        if self.url == "http://www.zonacondeduque.es/B_aclaracion_ejer_1_promo_AGE_2010.pdf":
            return 1.1
        t = self.titulo.lower()
        if "1º" in t or "primer" in t:
            return 1
        if "2º" in t or "segundo" in t:
            return 2
        if "3º" in t or "tercero" in t:
            return 3
        if "supuesto" in t:
            if self.ingreso == "interna":
                return 2
            if self.ingreso == "libre":
                return 3
        if "_1_" in self.url:
            return 1
        if "_2_" in self.url:
            return 2
        if "_3_" in self.url:
            return 3
        if " soluciones " in t:
            return 1
        raise Exception("ejercicio no encontrado en: %s - %s " % (self.year, self.titulo))

    @property
    def tipo(self):
        ej = int(self.ejercicio)
        if (ej, self.ingreso) in ((2, "interna"), (3, "libre")):
            return "supuesto"
        if ej == 1:
            return "test"
        if (ej, self.ingreso) == (2, "libre"):
            return "preguntas"
        raise Exception("tipo no encontrado en: %s - %s " % (self.year, self.titulo))

    @property
    def isSolucion(self):
        t = self.titulo.lower()
        if "solución" in t or "solucion" in t:
            return True
        if "_sol_"  in self.url:
            return True
        return False

class Oposicion(MyMunch):

    @lru_cache(maxsize=None)
    def iter_baquedano(self, url=BAQU_URL):
        arr = []
        sol = []
        W.get(url)
        for tr in W.soup.select("table.MsoNormalTable tr"):
            tds = tr.findAll("td")
            if len(tds)!=4:
                continue
            url = tr.find("a")
            if url is None:
                continue
            url = url.attrs.get("href")
            if url is None:
                continue
            tds = [get_text(td) for td in tds]
            titulo=tds[1]
            if titulo.startswith("Cuerpo de Gestión de Sistemas e Informática de la AGE"):
                exa = BaqueExamenA2(
                    url=url,
                    year=int(tds[0]),
                    titulo=titulo,
                    text_ejercicio=tds[2]
                )
                if exa.isExcluir:
                    continue
                if exa.isSolucion:
                    sol.append(exa)
                else:
                    arr.append(exa)

        def findE(arr, grupo, year, ingreso, ejercicio):
            ok = []
            k = (grupo, year, ingreso, ejercicio)
            for a in arr:
                if (a.grupo, a.year, a.ingreso, a.ejercicio) == k:
                    ok.append(a)
            return ok

        for s in sol:
            es = findE(arr, s.grupo, s.year, s.ingreso, s.ejercicio)
            if len(es)>0:
                for e in es:
                    e.solucion = s.url
            else:
                s.solucion = s.url
                arr.append(s)

        return arr

    @property
    @lru_cache(maxsize=None)
    def convocatorias(self):
        conv = []
        W.get(self.url)
        links = list(W.soup.select("div.journal-content-article a"))
        for a in links:
            url = a.attrs["href"].strip()
            m = re_conv.match(url)
            if m is None:
                continue
            cod, year, ingreso = m.groups()
            conv.append(Convocatoria(
                oposicion=self,
                year=int(year),
                ingreso=ingreso,
                url=url,
                tipo=ingreso[0].upper()
            ))
        years = set(c.year for c in conv)
        baque_examenes=[]
        for e in self.iter_baquedano():
            if not(e.year in years or e.grupo != self.grupo):
                baque_examenes.append(e)
        baque_convocatorias=set((e.year, e.ingreso) for e in baque_examenes)
        for year, ingreso in baque_convocatorias:
            bq = BaqueConvocatoria(
                oposicion=self,
                year=year,
                ingreso=ingreso,
                url=BAQU_URL,
                tipo=ingreso[0].upper(),
                examenes=list(e for e in baque_examenes if (e.year, e.ingreso)==(year, ingreso))
            )
            conv.append(bq)
        return sorted(conv)

    @property
    def key(self):
        return self.grupo

class CrawlExamenes:
    def __init__(self, salida):
        self.salida = salida

    @property
    @lru_cache(maxsize=None)
    def opos(self):
        opos = {}
        W.get(INAP_URL)
        links = list(W.soup.select("div.nav-menu a"))
        for a in links:
            titulo = get_text(a)
            key = titulo.lower()
            grupo = OPOS.get(key)
            if grupo:
                url = a.attrs["href"]
                codigo = url.rsplit("/", 1)[-1].upper()
                opos[grupo] = Oposicion(
                    codigo=codigo,
                    grupo=grupo,
                    titulo=titulo,
                    url=url
                )
        opos = {k: v for k, v in sorted(opos.items(), key=lambda x: x[0])}
        return opos

    def save(self):
        SH = [DWNSH, dedent('''
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
        MD = [dedent('''
        ---
        title: Examenes de convocatorias anteriores
        summary: Examenes de convocatorias TAI/GSI/CSSTIC anteriores (ver [sede.inap]({inap}) y [baquedano]({baqu})).
        ---
        '''.format(inap=INAP_URL, baqu=BAQU_URL)).strip()]
        for grupo, data in self.opos.items():
            MD.append("\n# [{codigo} {titulo}]({url})\n".format(**dict(data)))
            SH.append(dedent('''
            # {grupo} {codigo}
            if [ -d "{grupo}" ]; then
               echo "{grupo} ya existe, borrelo si quiere volver a descargarlo"
            else
            '''.format(**dict(data))).rstrip())
            for conv in data.convocatorias:
                MD.append("* {grupo} [{year} - {ingreso}]({url})".format(grupo=data.codigo, **dict(conv)))
                for exa in conv.examenes:
                    mam_fl="{grupo}/{year}-{ejercicio}{tipo}".format(grupo=data.grupo, ejercicio=exa.ejercicio, **dict(conv))
                    dwn_sh="dwn "+mam_fl
                    if exa.get("modelo") is not None:
                        modelos = ", ".join(("[modelo {} + solución]({})".format(k.upper(), v) for k,v in sorted(exa.modelo.items())))
                        MD.append("    * Ejercicio {ejercicio}: ".format(**exa.asdict())+modelos)
                        for m, u in sorted(exa.modelo.items()):
                            SH.append(dwn_sh+"_{modelo} '{url}'".format(url=u, modelo=m))
                        continue
                    if exa.get("bloque") is not None:
                        bloques = ", ".join(("[bloque {}]({})".format(k.upper(), v) for k,v in sorted(exa.bloque.items())))
                        MD.append("    * Ejercicio {ejercicio}: ".format(**exa.asdict())+bloques)
                        for m, u in sorted(exa.bloque.items()):
                            SH.append(dwn_sh+"_{bloque} '{url}'".format(url=u, bloque=m))
                        continue
                    if exa.solucion is None:
                        MD.append("    * [Ejercicio {ejercicio}]({url})".format(**exa.asdict()))
                        SH.append(dwn_sh+" '{url}'".format(**exa.asdict()))
                    elif exa.solucion == exa.url:
                        MD.append("    * [Ejercicio {ejercicio} + solución]({url})".format(**exa.asdict()))
                        SH.append(dwn_sh+" '{url}'".format(**exa.asdict()))
                    else:
                        MD.append("    * [Ejercicio {ejercicio}]({url}) + [solución]({solucion})".format(**exa.asdict()))
                        SH.append(dwn_sh+"P '{url}'".format(**exa.asdict()))
                        SH.append(dwn_sh+"R '{solucion}'".format(**exa.asdict()))
            SH.append("fi")
        SH.append(dedent('''
            find . -name '*L*' -type f -print0 |
            while IFS= read -r -d '' FL; do
              dup "$FL"
            done
            find . -name '*R*.pdf' -type f -print0 |
            while IFS= read -r -d '' FL; do
              mrg "$FL"
            done
        '''))
        MD.append("\n[Script para descargar](examenes.sh)")
        write(self.salida+"00-examenes.md", "\n".join(MD))
        write(self.salida+"examenes.sh", "\n".join(SH))

    def abbr_supuestos(self, abbr_file):
        SH=[DWNSH,dedent('''
        mkdir -p supuestos
        cd supuestos
        ''')]
        supuestos = []
        for grupo, data in self.opos.items():
            for conv in data.convocatorias:
                for exa in conv.examenes:
                    if grupo == 'A2' and exa.tipo == "supuesto":
                        supuestos.append(exa)
        LNS = []
        supuestos = sorted(supuestos, key=lambda x: (x.year, x.ingreso, x.ejercicio))
        for e in supuestos:
            if e.get("bloque") is not None:
                for b, u in sorted(e.bloque.items()):
                    name = "{}_A2.{}_b{}".format(e.year, e.ingreso[0:3], b)
                    LNS.append(name)
                    LNS.append(u+' download="'+name+'"')
                    LNS.append("Supuesto práctico A2 {} bloque {} (convocatoria {})".format(e.year, b, e.ingreso))
                    LNS.append("")
                    SH.append("dwn "+name+" '{}'".format(u))
                continue
            name = "{}_A2.{}".format(e.year, e.ingreso[0:3])
            LNS.append(r"r'\b"+re.escape(name))
            LNS.append(e.url+' download="'+name+'"')
            LNS.append("Supuesto práctico A2 {} (convocatoria {})".format(e.year, e.ingreso))
            LNS.append("")
            SH.append("dwn "+name+" '{}'".format(e.url))
        write(abbr_file, "\n".join(LNS))
        write(self.salida+"supuestos.sh", "\n".join(SH))

if __name__ == "__main__":
    c = CrawlExamenes("content/posts/ejercicios/")
    c.save()
    c.abbr_supuestos("config/abbr/97-supuestos.txt")
