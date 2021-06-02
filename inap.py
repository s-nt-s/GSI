#!/usr/bin/env python3

from core.web import Web, FF
from core.util import read, clean_url
from time import sleep
from munch import Munch
import re

cfg = read("config/inap.yml")
re_sp = re.compile(r"\s+")
re_test = re.compile(r"\bTest\b", re.IGNORECASE)
re_tema = re.compile(r"^\s*Tema\s+\d+\..+")
salida = "docs/"


f=FF()
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
w.get(cfg.curso)

CURSO = re_sp.sub(" ", w.soup.find("h1").get_text()).strip().capitalize()
CODIGO = re_sp.sub(" ", w.soup.select("li.breadcrumb-item a")[-1].get_text()).strip()


def get_urls(slc, text=None):
    urls = w.soup.select(slc)
    r=[]
    done = set()
    for i in urls:
        url = i.attrs["href"]
        if url in done:
            continue
        txt = re_sp.sub(" ", i.get_text()).strip()
        if text is None or text.search(txt):
            r.append((txt, url))
            done.add(url)
    return r

def get_bloques():
    blq = 0
    URLS=get_urls("div.content h3.section-title a")
    for bloque, url in URLS:
        w.get(url)
        TEST=get_urls("div.content a.aalink", text=re_test)
        if TEST:
            TEMAS = w.soup.select_one("#region-main").findAll("p", text=re_tema)
            TEMAS = [re_sp.sub(" ", i.get_text().split(".", 1)[-1]).strip() for i in TEMAS]
            blq = blq + 1
            titulo = bloque.split("-", 1)[-1]
            titulo = titulo.strip()
            titulo = titulo.capitalize()
            b = Munch(
                bloque=blq,
                titulo=titulo,
                url=url,
                temas=[]
            )
            for (i, ((_, href), txt)) in enumerate(zip(TEST, TEMAS)):
                t=Munch(
                    tema=i+1,
                    titulo=txt,
                    url=href,
                    feedback=set()
                )
                b.temas.append(t)
                w.get(href)
                revs = [a.attrs["href"] for a in w.soup.findAll("a", text="Revisión")]
                for rev in revs:
                    w.get(rev)
                    for a in w.soup.select("div.feedback a"):
                        t.feedback.add(a.attrs["href"])
            yield b


feedback=set()
MD=[]
for b in get_bloques():
    MD.append("\n{bloque}. [{titulo}]({url})".format(**dict(b)))
    for t in b.temas:
        MD.append("    {tema}. [{titulo}]({url})".format(**dict(t)))
        feedback = feedback.union(t.feedback)

feedback=sorted(feedback)
if feedback:
    MD.append("\nURLs referenciadas en las soluciones de algunos de los tests:\n")
    for a in feedback:
        if "_" in a:
            MD.append('* <a href="{1}">{0}</a>'.format(clean_url(a), a))
        else:
            MD.append("* [{}]({})".format(clean_url(a), a))


MD="\n".join(MD).strip()
MD='''
---
title: {cod} {cur}
---
<div class="alert">
{cod} <a href="{url}">{cur}</a>
</div>

'''.lstrip().format(cod=CODIGO, cur=CURSO, url=cfg.curso)+MD

with open(salida+CODIGO+ ".md", "w") as file:
    file.write(MD)
