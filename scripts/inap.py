import re
from textwrap import dedent
from time import sleep
from functools import lru_cache
import sys

from munch import Munch
from unidecode import unidecode

from os import makedirs
from os.path import dirname

from .core.util import clean_url, read, url_key, write
from .core.web import FF, Web

re_sp = re.compile(r"\s+")
re_test = re.compile(r"\bTest\b|Simulacro de examen", re.IGNORECASE)
re_tema = re.compile(r"^\s*Tema\s+\d+\s*[\.:\-\s]*(.+)|SIMULACRO DE EXAMEN", re.IGNORECASE)
re_ley = re.compile(r"(Reglamento \(?UE\)?|Ley Org[aá]nica|Real Decreto|RD|Ley|Decreto|Reglamento|LO) (\d+/\d+)", re.IGNORECASE)

def parse_ley(pre, num):
    ori = str(pre)
    pre = pre.lower()
    pre = unidecode(pre)
    if pre in ("reglamento ue", "reglamento (ue)"):
        return "Reglamento (UE)"
    if pre in ("lo", "ley organica"):
        return "Ley Orgánica"
    if pre in ("real decreto", "rd"):
        return "Real Decreto"
    if pre == "ley":
        if num == "3/2018":
            return "Ley Orgánica"
    if pre == "reglamento":
        if num == "910/2014":
            return "Reglamento (UE)"
    if pre in ("ley", "reglamento"):
        return pre.title()
    return ori

def get_session(cfg):
    f = FF()
    f.get("https://cas.inap.es/cas/login")
    f.val("username", cfg.username)
    f.val("password", cfg.password)
    f.click("//form[@id='fm1']/*/input[contains(@class,'btn-submit')]")
    sleep(1)
    f.get(cfg.curso)
    sleep(1)
    w = Web()
    w.s = f.get_session()
    f.close()
    return w

def rlp(s, *args):
    for a, b in zip(args[0::2], args[1::2]):
        s = s.replace(a, b)
    return s

class CrawlInap:
    def __init__(self, salida):
        self.cfg = read("config/inap.yml")
        self.salida = salida
        self.w = get_session(self.cfg)
        self.w.get(self.cfg.curso)

        self.CURSO = re_sp.sub(" ", self.w.soup.find("h1").get_text()).strip().capitalize()
        self.CURSO = rlp(self.CURSO, ".- oep", " - OEP", "gestion", "gestión", "informatica", "informática")
        self.CODIGO = re_sp.sub(" ", self.w.soup.select("li.breadcrumb-item a")[-1].get_text()).strip()

    def get_urls(self, slc, text=None):
        urls = self.w.soup.select(slc)
        r = []
        done = set()
        s = []
        for i in urls:
            url = i.attrs["href"]
            if url in done:
                continue
            txt = re_sp.sub(" ", i.get_text()).strip()
            if text is None or text.search(txt):
                done.add(url)
                if txt == "Documentación común para resolución Supuestos 7 y 8 Carpeta":
                    s.append((txt, url))
                else:
                    r.append((txt, url))
        return r+s

    def get_text_nodes(self, tag, rg):
        main = self.w.soup.select_one("#region-main")
        for p in main.findAll(tag):
            txt = p.get_text().strip()
            txt = re_sp.sub(" ", txt)
            mtc = rg.match(txt)
            if mtc:
                if mtc.group(1):
                    txt = mtc.group(1)
                yield txt.strip()

    def get_supuestos(self):
        pass

    def get_bloques(self, descargar=False):
        def getB(s):
            for i, b in enumerate(["BLOQUE IV", "BLOQUE III", "BLOQUE II", "BLOQUE I"]):
                if b in s:
                    return 4-i
            if s == "SIMULACRO DE EXAMEN":
                return 5
            return None

        blq = 0
        URLS = self.get_urls("div.content h3.section-title a")
        for bloque, url in URLS:
            print("")
            print(bloque)
            print(url)
            blq = getB(bloque)
            if blq is None:
                continue
            titulo = bloque.rsplit("-", 1)[-1]
            titulo = titulo.strip()
            titulo = titulo.capitalize()

            self.w.get(url)
            TEST = self.get_urls("div.content a.aalink", text=re_test)
            if TEST:
                TEMAS = list(self.get_text_nodes("p", re_tema))
                b = Munch(
                    bloque=blq,
                    titulo=titulo,
                    url=url,
                    tipo="Tests",
                    temas=[],
                    supuestos=[],
                )
                print(len(TEMAS), "temas", len(TEST), "test")
                while len(TEMAS)<len(TEST):
                    TEMAS.append(TEST[len(TEMAS)-1][0])
                for (i, ((_, href), txt)) in enumerate(zip(TEST, TEMAS)):
                    print(" ", "%2d" % (i+1), txt)
                    t = Munch(
                        tema=i+1,
                        titulo=txt,
                        url=href,
                        feedback={},
                        leyes={},
                        done=0,
                    )
                    b.temas.append(t)
                    self.w.get(href)
                    revs = [a.attrs["href"] for a in self.w.soup.findAll("a", text="Revisión")]
                    t.done = len(revs)
                    for rev in revs:
                        self.w.get(rev)
                        for a in self.w.soup.select("div.feedback a"):
                            href = a.attrs["href"]
                            t.feedback[href] = t.feedback.get(href, 0) + 1
                        main = self.w.soup.select_one("section.region-main-content")
                        main = re_sp.sub(" ", main.get_text())
                        for pre, num in re_ley.findall(main):
                            ley = parse_ley(pre, num) + ' ' +num
                            if ley not in ("Real Decreto 211/2019", ):
                                t.leyes[ley] = t.leyes.get(ley, 0) + 1
                yield b
            else:
                b = Munch(
                    bloque=blq,
                    titulo=titulo,
                    url=url,
                    tipo="Supuestos",
                    temas=[],
                    supuestos=[],
                )
                SUPUESTOS = self.get_urls("div.single-section ul.section.img-text div.activityinstance a")
                for i, (txt, href) in enumerate(SUPUESTOS):
                    print(" ", "%2d" % (i+1), txt)
                    t = Munch(
                        supuesto=i+1,
                        titulo=txt,
                        url=href,
                        archivos=[]
                    )
                    b.supuestos.append(t)
                    self.w.get(href)
                    for txt, href in self.get_urls("div[role='main'] a"):
                        if href != "#":
                            t.archivos.append(Munch(titulo=txt, url=href))
                    if descargar:
                        for fl in t.archivos:
                            trg = "debug/inap/B{}/{}/{}".format(b.bloque, t.titulo, fl.titulo)
                            makedirs(dirname(trg), exist_ok=True)
                            r = self.w.s.get(fl.url)
                            with open(trg, "wb") as f:
                                f.write(r.content)
                yield b


    def save(self, descargar=False):
        feedback = {}
        leyes = {}
        MD = []
        def dict_add(d1, d2):
            for k, v in d2.items():
                d1[k] = d1.get(k, 0) + v
        lastTipo = None
        for b in self.get_bloques(descargar=descargar):
            if b.tipo is not lastTipo:
                MD.append("\n# "+b.tipo+"\n")
                lastTipo = b.tipo
            MD.append("{bloque}. [{titulo}]({url})".format(**dict(b)))
            for t in b.temas:
                MD.append("    {tema}. [{titulo}]({url}) <small>[{done}]</small>".format(**dict(t)))
                dict_add(feedback, t.feedback)
                dict_add(leyes, t.leyes)
            for t in b.supuestos:
                MD.append("    {supuesto}. [Supuesto {supuesto}]({url})".format(**dict(t)))
                for index, a in enumerate(t.archivos):
                    MD.append("        {i}. [{titulo}]({url})".format(i=index+1, **dict(a)))

        leyes = sorted(leyes.items(), key=lambda x:(-x[1], x[0]))
        if leyes:
            MD.append("\n# Leyes mencionadas en algunos de los tests:\n")
            for a, count in leyes:
                MD.append("* {} x {}".format(count, a))
        feedback = sorted(feedback.items(), key=lambda x:(-x[1], url_key(x[0])))
        if feedback:
            MD.append(
                "\n# URLs referenciadas en las soluciones de algunos de los tests:\n")
            for a, count in feedback:
                if "_" in a:
                    MD.append('* {2} x <a href="{1}">{0}</a>'.format(clean_url(a), a, count))
                else:
                    MD.append("* {2} x [{0}]({1})".format(clean_url(a), a, count))

        MD = "\n".join(MD).strip()
        MD = dedent('''
        ---
        title: {cod} {cur}
        summary: Curso INAP [{cod} {cur}]({url}).
        ---

        ''').lstrip().format(cod=self.CODIGO, cur=self.CURSO, url=self.cfg.curso)+MD

        write(self.salida+self.CODIGO+".md", MD)


if __name__ == "__main__":
    c = CrawlInap("content/posts/ejercicios/10-")
    c.save(descargar="dwn" in sys.argv)
