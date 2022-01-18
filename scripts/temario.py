
import re
from textwrap import dedent

import bs4
import requests
import roman

from .core.util import write
from .core.web import Web

sp = re.compile("\s+")
re_tema = re.compile(r"^(\d+)\. (.+)$")

LAST_BOE="BOE-A-2021-8892"

def mkRE(s):
    if isinstance(s, str):
        return re.compile(s)
    return s


class TTema:

    def __init__(self, tema):
        n, t = re_tema.findall(tema)[0]
        self.num = int(n)
        self.titulo = t
        self.puntos = t.split(". ")
        self.puntos[-1] = self.puntos[-1][:-1]


class TBloque:

    def __init__(self, num, titulo, tipo):
        self.num = num
        self.titulo = titulo
        self.tipo = tipo
        self.temas = []

    def add(self, tema):
        n = tema.split(".")[0]
        if n.strip().isdigit():
            self.temas.append(TTema(tema))


class CrawlTemario:
    def __init__(self, salida, title="Temario GSI", boe="BOE-A-2021-8892", libre="XII", interna="XIII", re_anexo=r"^ANEXO ([XVICMDL]+)$", re_bloque=r"^([XVICMDL]+)\. (.+)$"):
        self.boe = boe
        self.anx_libre = libre
        self.anx_interna = interna
        self.re_bloque = mkRE(re_bloque)
        self.re_anexo = mkRE(re_anexo)
        self.salida = salida
        self.title = title
        self.w = Web()

    @property
    def url(self):
        return "https://boe.es/diario_boe/txt.php?id=" + self.boe

    def get_bloques(self, get_anexo):
        temario = []
        self.w.get(self.url)
        ps = self.w.soup.findAll(["p", "h1", "h2", "h3", "h4", "h5", "h6"])

        flag = 0
        blq = None

        tipBloque = None
        for p in ps:
            txt = sp.sub(" ", p.get_text()).strip()
            anexo = self.re_anexo.match(txt)

            if anexo:
                if flag > 0:
                    return temario
                if anexo.group(1) == get_anexo:
                    flag = 1
                continue

            if flag == 0:
                continue

            if txt in ("A. Temas generales", "B. Temas específicos"):
                tipBloque = txt

            bloque = self.re_bloque.match(txt)
            if bloque:
                num = roman.fromRoman(bloque.group(1))
                txt = bloque.group(2)
                blq = TBloque(num, txt, tipo=tipBloque)
                temario.append(blq)
                continue

            if blq == None:
                continue

            blq.add(txt)
        return temario

    def save(self, anexo, file="%s.md", global_i=False, status='published', pdf_code=None):
        title = str(self.title)
        if None not in (self.anx_libre, self.anx_interna):
            if anexo == self.anx_libre:
                title = title + " (libre)"
                file = file % "libre"
            elif anexo == self.anx_interna:
                title = title + " (interna)"
                file = file % "interna"
        MD = [dedent('''
        ---
        title: '{title}'
        Status: {status}
        summary: '[{boe}]({url}) - Anexo {anexo}'
        pdf_code: {pdf_code}
        ---

        '''.format(title=title, url=self.url, boe=self.boe, anexo=anexo, status=status, pdf_code=pdf_code)).strip().replace("\npdf_code: None", "")
        ]

        count = 0
        lastTipBloque = None
        for blq in self.get_bloques(get_anexo=anexo):
            if blq.tipo is not None and blq.tipo != lastTipBloque:
                MD.append("\n# "+blq.tipo+"\n")
                lastTipBloque = blq.tipo
            if blq.tipo:
                MD.append("\n## "+blq.titulo+"\n")
            else:
                MD.append("\n# "+blq.titulo+"\n")
            for i, tema in enumerate(blq.temas):
                count = count + 1
                if global_i:
                    MD.append("{0}. {1}".format(count, tema.titulo))
                else:
                    MD.append("{0}. {1}".format(i+1, tema.titulo))

        MD = "\n".join(MD)
        MD = re.sub(r"\n\n\n+", r"\n\n", MD)
        if self.boe == LAST_BOE:
            write(self.salida + file, MD)
        else:
            write(self.salida + self.boe + "/" + file, MD)


if __name__ == "__main__":
    c = CrawlTemario("content/posts/temario/")
    c.save(c.anx_libre, pdf_code='GSI')
    c.save(c.anx_interna, pdf_code='GSI')

    c = CrawlTemario("content/posts/temario/", boe="BOE-A-2019-9062", libre="IX", interna="X", re_bloque=r"^Bloque ([XVICMDL]+)\. (.+)$")
    c.save(c.anx_libre, status='hidden')
    c.save(c.anx_interna, status='hidden')

    c = CrawlTemario("content/posts/temario/", title="Temario CSSTIC", boe="BOE-A-2022-573", libre="II", interna=None)
    c.save(c.anx_libre, file="csstic.md", global_i=True, status='hidden', pdf_code='A2')
