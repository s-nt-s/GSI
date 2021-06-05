
import re
from textwrap import dedent

import bs4
import requests
import roman

from .util import write
from .web import Web

sp = re.compile("\s+")
re_tema = re.compile(r"^(\d+)\. (.+)$")

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

    def __init__(self, num, titulo):
        self.num = num
        self.titulo = titulo
        self.temas = []

    def add(self, tema):
        n = tema.split(".")[0]
        if n.strip().isdigit():
            self.temas.append(TTema(tema))


class CrawlTemario:
    def __init__(self, boe="BOE-A-2021-8892", libre="XII", interna="XIII", re_anexo=r"^ANEXO ([XVICMDL]+)$", re_bloque=r"^([XVICMDL]+)\. (.+)$", salida="docs/"):
        self.boe = boe
        self.anx_libre = libre
        self.anx_interna = interna
        self.re_bloque = mkRE(re_bloque)
        self.re_anexo = mkRE(re_anexo)
        self.salida = salida
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

            bloque = self.re_bloque.match(txt)
            if bloque:
                num = roman.fromRoman(bloque.group(1))
                txt = bloque.group(2)
                blq = TBloque(num, txt)
                temario.append(blq)
                continue

            if blq == None:
                continue

            blq.add(txt)
        return temario

    def save(self, anexo):
        title = "Temario GSI"
        file = "temario/%s.md"
        if anexo == self.anx_libre:
            title = title + " (libre)"
            file = file % "libre"
        elif anexo == self.anx_interna:
            title = title + " (interna)"
            file = file % "interna"
        MD=[dedent('''
        ---
        title: {title}
        css: [main.css]
        ---
        <div class="alert">
        <a href="{url}" target="_blank">{boe}</a> - Anexo {anexo}
        </div>
        '''.format(title=title, url=self.url, boe=self.boe, anexo=anexo)).strip()
        ]
        for blq in self.get_bloques(get_anexo=anexo):
            MD.append("\n# "+blq.titulo+"\n")
            for i, tema in enumerate(blq.temas):
                MD.append("{0}. {1}".format(i+1, tema.titulo))

        write(self.salida + file, "\n".join(MD))

if __name__ == "__main__":
    c = CrawlTemario()
    c.save(c.anx_libre)
    c.save(c.anx_interna)
