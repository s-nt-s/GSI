#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

import bs4
import requests
from weasyprint import CSS, HTML

from util import get_html, get_tpt, html_to_pdf

salida = "docs/gsitic.wordpress.com/"
GRABY_ENDPOINT = os.environ['GRABY_ENDPOINT']

bloques = (
    (1, 'https://gsitic.wordpress.com/bloque-i/',
     'Organización del Estado y Administración electrónica'),
    (2, 'https://gsitic.wordpress.com/bloque-ii/',  'Tecnología básica'),
    (3, 'https://gsitic.wordpress.com/bloque-iii/', 'Desarrollo de sistemas'),
    (4, 'https://gsitic.wordpress.com/bloque-iv/',  'Sistemas y comunicaciones'),
)

heads = ["h1", "h2", "h3", "h4", "h5", "h6"]


def get_soup(url):
    r = requests.get(url)
    return bs4.BeautifulSoup(r.content, "lxml")


def get_graby(url):
    r = requests.get(GRABY_ENDPOINT, params={"url": url})
    if not r.text.strip():
        return None
    return r.json()

for i, url, title in bloques:
    graby = get_graby(url)
    bloque = bs4.BeautifulSoup(graby['html'], "lxml")
    temas = bloque.findAll("a")
    total = len(bloque.findAll("li"))
    porcentaje = int((len(temas) / total) * 100)
    print ("El bloque %s esta al %s%%" % (i, porcentaje))

    if len(temas) == 0:
        continue

    print ("Creando HTML del bloque " + str(i) + " ...", end="\r")
    soup = get_tpt("B%s %s" % (i, title), rec="../rec/",
                   css_screen="gsitic.css", css_print="gsitic_print.css")
    div = soup.find("div")

    for a in temas:
        graby = get_graby(a.attrs["href"])
        #h2 = soup.new_tag("h2")
        #h2.string = graby['title']
        # div.append(h2)

        tema = bs4.BeautifulSoup(graby['html'], "lxml")
        tema = tema.find("body")
        for d in tema.select("div.wpcnt"):
            d.extract()

        bios = tema.findAll(heads, text="Bibliografía")
        for bio in bios:
            bio.name = "strong"

        hss = []
        for hi in range(1, 7):
            hs = tema.findAll("h" + str(hi))
            if len(hs) > 0:
                hss.append(hs)
        hi = 1
        for hs in hss:
            for h in hs:
                h.name = "h" + str(hi)
            hi = hi + 1

        for bio in bios:
            bio.name = "h2"
            bio.attrs["class"] = "bio"
            for n in bio.find_next_siblings("ul"):
                n.attrs["class"] = "bio"

        for h in tema.findAll(heads):
            for s in h.findAll("strong"):
                s.unwrap()

        for hr in tema.findAll("hr"):
            hr.extract()

        div.append(tema)
        tema.unwrap()

    html = get_html(soup)
    out = salida + "bloque_" + str(i)
    with open(out + ".html", "w") as file:
        file.write(html)
    print ("Creando HTML del bloque " + str(i) + " 100%")
