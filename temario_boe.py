#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

import bs4
import requests
import roman

from util import get_html, get_tpt, html_to_pdf

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
    file = "temario_%s.html"
    if anexo == ANX_LIBRE:
        title = title + " (libre)"
        file = file % "libre"
    elif anexo == ANX_INTERNA:
        title = title + " (interna)"
        file = file % "interna"
    indice = get_tpt(title, rec="rec/",
                     css_screen="temario.css",  css_print="temario_print.css")

    for blq in get_bloques(BOE, get_anexo=anexo):
        indice.body.div.append(get_h(indice, 1, blq.titulo))
        ol = indice.new_tag("ol")
        indice.body.div.append(ol)
        for tema in blq.temas:
            li = indice.new_tag("li")
            li.string = tema.titulo
            ol.append(li)

    html = get_html(indice)
    with open(salida + file, "w") as file:
        file.write(html)

save(ANX_LIBRE)
save(ANX_INTERNA)
