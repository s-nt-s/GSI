#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

import bs4
import requests
from weasyprint import CSS, HTML

from core.util import get_html, get_tpt, html_to_pdf

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
    print("El bloque %s esta al %s%%" % (i, porcentaje))

    if len(temas) == 0:
        continue

    extra = '''
			<meta content="gsitic.wordpress.com" name="DC.creator" />
			<meta name="ebook-meta" content='-s "gsitic.wordpress.com" -i %s' />
    ''' % i

    print("Creando HTML del bloque " + str(i) + " ...", end="\r")
    soup = get_tpt("B%s %s" % (i, title), rec="../rec/",
                   css_screen="gsitic.css", css_print="gsitic_print.css", extra=extra)
    div = soup.find("div")

    for a in temas:
        url_tema = a.attrs["href"]
        graby = get_graby(url_tema)
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

        if url_tema == "https://gsitic.wordpress.com/2018/02/11/biv9-administracion-de-redes-locales-gestion-de-usuarios-gestion-de-dispositivos-monitorizacion-y-control-de-trafico-gestion-snmp-gestion-de-incidencias/":
            tema.find("h1").name = "h2"

        hss = []
        for hi in range(1, 7):
            hs = tema.findAll("h" + str(hi))
            if len(hs) > 0:
                hss.append(hs)
        '''
        if len(hss)>0 and len(hss[0])==1:
            hss[0][0].extract()
            del hss[0]
        '''

        hi = 2
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

        for n in tema.findAll(["div", "p"]):
            if not n.find("img"):
                txt = n.get_text().strip()
                if len(txt) == 0:
                    n.extract()
            if "id" in n.attrs:
                del n.attrs["id"]

        for img in tema.findAll("img"):
            src = img.attrs["src"]
            img.attrs.clear()
            img.attrs["src"] = src

        h1 = soup.new_tag("h1")
        h1.string = a.get_text()
        div.append(h1)
        div.append(tema)
        tema.attrs.clear()
        tema.name = "article"

    html = get_html(soup)
    out = salida + "bloque_" + str(i)
    with open(out + ".html", "w") as file:
        file.write(html)
    print("Creando HTML del bloque " + str(i) + " 100%")
