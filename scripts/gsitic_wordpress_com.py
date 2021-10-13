#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re

import bs4
import html2markdown
from markdownify import markdownify
import requests
import yaml
from munch import Munch
from weasyprint import CSS, HTML

from .core.util import write

salida = "docs/gsitic.wordpress.com/"
GRABY_ENDPOINT = os.environ['GRABY_ENDPOINT']

heads = ["h1", "h2", "h3", "h4", "h5", "h6"]
re_head = re.compile(r"<(h[1-6])>\s*(.*?)\s*</\1>", re.MULTILINE)


def get_graby(url):
    r = requests.get(GRABY_ENDPOINT, params={"url": url})
    if not r.text.strip():
        return None
    return r.json()


def get_graby_soup(url):
    graby = get_graby(url)
    html = graby['html']
    html = re_head.sub(r"<\1>\2</\1>", html)
    soup = bs4.BeautifulSoup(html, "lxml")
    return soup


class CrawlGstic:
    def __init__(self, salida):
        self.bloques = {b: Munch(
            bloque=b,
            source=url,
            title="B%s %s" % (b, title),
            html=None,
            pdf_code="B"+str(b)
        ) for b, url, title in (
            (1, 'https://gsitic.wordpress.com/bloque-i/', 'Organización del Estado y Administración electrónica'),
            (2, 'https://gsitic.wordpress.com/bloque-ii/',  'Tecnología básica'),
            (3, 'https://gsitic.wordpress.com/bloque-iii/', 'Desarrollo de sistemas'),
            (4, 'https://gsitic.wordpress.com/bloque-iv/',  'Sistemas y comunicaciones'),
        )}
        self.salida = salida

    def read_bloque(self, b):
        b = self.bloques[b]
        bloque = get_graby_soup(b.source)
        temas = bloque.findAll("a")
        b.total = len(bloque.findAll("li"))
        b.porcentaje = int((len(temas) / b.total) * 100)

        if len(temas) == 0:
            return b

        b.pandoc = '--toc-depth 2 --parse-raw --epub-chapter-level 2'
        b.author = 'gsitic.wordpress.com'
        b.lang = 'es-ES'
        b['ebook-meta'] = "-s gsitic.wordpress.com -i "+str(b.bloque)
        b['txt-cover'] = b.title

        div = bs4.BeautifulSoup("", "html.parser")

        for a in temas:
            url_tema = a.attrs["href"]
            tema = get_graby_soup(url_tema)

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
                if src == "https://s1.wp.com/wp-content/mu-plugins/wpcom-smileys/wordpress.svg":
                    img.extract()
                    continue
                img.attrs.clear()
                img.attrs["src"] = src

            h1 = div.new_tag("h1")
            h1.string = a.get_text()
            div.append(h1)
            div.append(tema)
            tema.attrs.clear()
            tema.name = "article"
            tema.unwrap()

        html = str(div)
        b.html = html
        return b

    def save(self, *bloques):
        if len(bloques) == 0:
            bloques = sorted(self.bloques.keys())
        for b in bloques:
            b = self.read_bloque(b)
            print("El bloque %s esta al %s%%" % (b.bloque, b.porcentaje))
            if b.html:
                out = self.salida + "bloque_" + str(b.bloque)
                yml = dict(b)
                del yml['html']
                yml['Status'] = 'published'
                yml['summary'] = 'Contenido propiedad de [gsitic.wordpress.com]({source}).'.format(**dict(b))
                yml = yaml.safe_dump(yml, allow_unicode=True)
                yml = '\n'.join(('---', yml.strip(), '---'))
                #write(out+".md", yml+"\n\n"+html2markdown.convert(b.html))
                txt_md = markdownify(b.html, heading_style="ATX", bullets="*")
                txt_md = re.sub(r"\n\n\n+", "\n\n", txt_md)
                txt_md = re.sub(r"^[\t ]+#", "#", txt_md, flags=re.MULTILINE)
                write(out+".md", yml+"\n\n"+txt_md)
                print("Creando MD del bloque " + str(b.bloque) + " 100%")


if __name__ == "__main__":
    c = CrawlGstic("content/posts/gsitic.wordpress.com/")
    c.save()
