#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from textwrap import dedent

import bs4
import requests
import roman

from core.util import get_html, get_tpt, html_to_pdf, write

sp = re.compile("\s+")

BOE = "https://boe.es/diario_boe/txt.php?id=BOE-A-2019-9062"
ANX_LIBRE = "IX"
ANX_INTERNA = "X"
salida = "docs/"

re_anexo = re.compile(r"^ANEXO ([XVICMDL]+)$")
re_bloque = re.compile(r"^Bloque ([XVICMDL]+)\. (.+)$")
re_tema = re.compile(r"^(\d+)\. (.+)$")


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


def get_soup(url):
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = bs4.BeautifulSoup(response.text, "lxml")
    return soup


def get_bloques(url, get_anexo):
    temario = []
    ps = get_soup(BOE).findAll(["p", "h1", "h2", "h3", "h4", "h5", "h6"])

    flag = 0
    blq = None

    for p in ps:
        txt = sp.sub(" ", p.get_text()).strip()
        anexo = re_anexo.match(txt)

        if anexo:
            if flag > 0:
                return temario
            if anexo.group(1) == get_anexo:
                flag = 1
            continue

        if flag == 0:
            continue

        bloque = re_bloque.match(txt)
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


def get_h(soup, level, txt):
    h = soup.new_tag("h" + str(level))
    h.string = txt
    return h


def save(anexo):
    title = "Temario GSI"
    file = "temario/%s.md"
    if anexo == ANX_LIBRE:
        title = title + " (libre)"
        file = file % "libre"
    elif anexo == ANX_INTERNA:
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
    '''.format(title=title, url=BOE, boe=BOE.split("=")[-1], anexo=anexo)).strip()
    ]
    for blq in get_bloques(BOE, get_anexo=anexo):
        MD.append("\n# "+blq.titulo+"\n")
        for i, tema in enumerate(blq.temas):
            MD.append("0. {1}".format(i+1, tema.titulo))

    write(salida + file, "\n".join(MD))


save(ANX_LIBRE)
save(ANX_INTERNA)
