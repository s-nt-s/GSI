import requests
from bs4 import BeautifulSoup
from munch import Munch
from .core.util import write
from .core.web import Web
from textwrap import dedent
from myplugins.core.decorators import MunchCache, Cache
from markdownify import markdownify, MarkdownConverter
import re
import os

HEAD = list("h%s" % x for x in range(1,7))
re_sp = re.compile(r"\s+")
WEB=Web()


class MyConverter(MarkdownConverter):
    HID=0
    def convert_table(self, el, text, convert_as_inline):
        el.attrs.clear()
        if el.find("thead") is None:
            el.insert(0, BeautifulSoup("<thead></thead>", "html.parser"))
            el.find("thead").append(el.find("tr"))
            for th in el.select("thead td"):
                th.name = "th"
                for s in th.select("strong"):
                    s.unwrap()
        for x in el.select(":scope *"):
            if x.name == "span":
                x.unwrap()
                continue
            for k in list(x.attrs.keys()):
                if k not in ("rowspan", "colspan", "id", "name", "href", "src"):
                    del x.attrs[k]
        md = str(el)
        for t in ("table", "thead", "tbody", "tfoot", "tr"):
            md = md.replace("<"+t, "\n<"+t)
            if t != "tr":
                md = md.replace("</"+t+">", "\n</"+t+">")
        return "\n"+md.strip()+"\n"
        #return super().convert_table(el, text, convert_as_inline) + '\n\n'
    def convert_hn(self, n, el, text, convert_as_inline):
        if n>6:
            return "\n**{}**\n".format(text)
        md = super().convert_hn(n, el, text, convert_as_inline)
        MyConverter.HID = MyConverter.HID + 1
        id = el.name + "_" + str(MyConverter.HID)
        md = md.strip()
        md = md + " {#"+id+"}"
        return "\n"+md+"\n"
        #return '\n<h{0} id="{2}">{1}</h{0}>\n'.format(n, text, id)

def my_md(html, **options):
    return MyConverter(**options).convert(html)

def fix_char(s):
    for a,b in (
        ("á", "á"),
        ("é", "é"),
        ("í", "í"),
        ("ó", "ó"),
        ("ú", "ú"),
        ("ñ", "ñ"),
        ("ü", "ü")
    ):
        s = s.replace(a, b)
        s = s.replace(a.upper(), b.upper())
    return s


def to_md(s):
    txt_md = my_md(str(s), heading_style="ATX_CLOSED", bullets="*")
    txt_md = re.sub(r"\n\s*\n\s*\n+", "\n\n", txt_md)
    txt_md = re.sub(r"\n+#", "\n\n#", txt_md)
    txt_md = fix_char(txt_md)
    return txt_md

def norm_url(url):
    url = url.split("://", 1)[-1]
    url = url.rstrip("/")
    if url == "manuel.cillero.es/doc/metrica-3/tecnicas/wbs":
        url = "manuel.cillero.es/doc/metodologia/metrica-3/tecnicas/planificacion/wbs"
    if url == "manuel.cillero.es/doc/metrica-3/tecnicas/diagrama-de-extrapolacion":
        url = "manuel.cillero.es/doc/metodologia/metrica-3/tecnicas/planificacion/diagrama-de-extrapolacion"
    url = url.replace("/doc/metrica-3/", "/doc/metodologia/metrica-3/")
    return url

class CrawlMetrica:
    def __init__(self, salida):
        self.salida = salida
        self.indent = 0

    @Cache("config/metrica/html/{}/index.html")
    def get(self, url):
        WEB.get(url)
        return WEB.soup

    @MunchCache("content/posts/otros/metrica.json")
    def get_index(self):
        inx = []
        hsh = {}
        lsU = None
        url = "https://manuel.cillero.es/doc/metodologia/metrica-3/introduccion/"
        while url:
            soup = self.get(url)
            bread = soup.select_one("div.breadcrumb-trail")
            parent = bread.findAll("a")[-1]
            parent = parent.attrs["href"]
            tt = fix_char(re_sp.sub(" ",soup.find("h1").get_text()).strip())
            h2 = soup.select_one("section h2")
            if h2:
                h2 = fix_char(re_sp.sub(" ",h2.get_text()).strip())
                if h2.startswith(tt):
                    tt = h2
            m = Munch(
                title=tt,
                url=url,
            )
            if m.title.upper() == m.title:
                lsU = url
            elif parent == "https://manuel.cillero.es/doc/metodologia/metrica-3/tecnicas/":
                parent = lsU
            elif parent == "https://manuel.cillero.es/doc/metodologia/metrica-3/procesos-principales/":
                lw = m.title.split()[-1]
                lw = lw.strip("()")
                if lw in ("EVS", "ASI", "DSI", "CSI", "IAS"):
                    parent = "https://manuel.cillero.es/doc/metodologia/metrica-3/procesos-principales/desarrollo/"
            if parent in hsh:
                if "childrens" not in hsh[parent]:
                    hsh[parent].childrens=[]
                hsh[parent].childrens.append(m)
            else:
                inx.append(m)
            source = self.get_source(soup.select_one("section"))
            if source:
                m.source = source
            hsh[url]=m
            url = soup.select_one("a.avia-icon_select-yes-right-icon")
            if url:
                url = url.attrs["href"]
        return inx

    def iter_index(self, *jump):
        def iter_level(l, i):
            if i.url in jump:
                l = l - 1
            else:
                yield (l, i)
            for x in i.get("childrens" , []):
                yield from iter_level(l+1, x)

        for i in self.get_index():
            yield from iter_level(1, i)

    def save_index(self):
        with open(self.salida+"metrica.md", "w") as f:
            f.write(dedent('''
            ---
            title: Métrica v3
            ---
            ''').strip())
            spl_level = 2
            for level, i in self.iter_index():
                if level < spl_level:
                    f.write("\n\n{lv} [{title}]({url})\n".format(lv='#'*level, **dict(i)))
                else:
                    f.write("\n{sp}* [{title}]({url})".format(sp=' '*(4*(level-spl_level)), **dict(i)))

    def get_source(self, node):
        source = node.find(lambda x: x.name=="p" and re_sp.sub(" ", x.get_text()).strip()=="Fuente original (PDF) http://administracionelectronica.gob.es")
        if source:
            source.extract()
            source = source.find("a").attrs["href"]
        return source

    def save_book(self):
        id_url={}
        for level, i in self.iter_index():
            id_url[norm_url(i.url)]="a%s" % (len(id_url)+1)

        def get_sp(level, i):
            soup = self.get(i.url)
            for n in soup.findAll(HEAD+["p", "div", "table", "li", "ol", "ul"]):
                txt = re_sp.sub("", n.get_text())
                if len(txt)==0 and n.select_one(":scope *") is None:
                    n.extract()
            for li in soup.findAll("li"):
                for x in li.findAll(HEAD):
                    x.unwrap()
            soup = soup.select_one("main section")
            h2 = soup.select_one("h2")
            if h2 and re_sp.sub(" ", h2.get_text()).strip()==i.title:
                h2.extract()
            for a in soup.findAll("a"):
                img = a.select_one("img")
                href = a.attrs.get("href")
                if len(a.get_text().strip())==0 and img and img.attrs["src"] == href:
                    a.unwrap()
                    continue
                if href is None:
                    continue
                href = norm_url(href)
                if href == "manuel.cillero.es/doc/metodologia/metrica-3/procesos-principales/desarrollo":
                    href = "manuel.cillero.es/doc/metodologia/metrica-3/introduccion/procesos-principales/desarrollo"
                if href in id_url:
                    a.attrs["href"]="#"+id_url[href]

            heads = []
            for h in HEAD:
                hs = soup.findAll(h)
                if hs:
                    heads.append(hs)

            if level > 6:
                print("WARNING level={} en {}".format(level, i.url), heads)

            for inx, hs in enumerate(heads):
                l = level + inx
                x = l#min(6, l)
                for h in hs:
                    h.name = "h%s" % x
            return soup

        with open(self.salida+"metrica_v3.md", "w") as f:
            f.write(dedent('''
            ---
            title: Métrica v3
            status: draft
            harddraft: true
            author: Ministerio de Administraciones Pública
            description: MÉTRICA v3 es propiedad intelectual del Ministerio de Administraciones Públicas, ver http://administracionelectronica.gob.es/pae_Home/pae_Documentacion/pae_Metodolog/pae_Metrica_v3.html
            lang: es-ES
            pandoc: --toc-depth 3 --parse-raw --epub-chapter-level 2
            source: Ministerio de Administraciones Pública
            summary: Contenido propiedad del [Ministerio de Administraciones Públicas](http://administracionelectronica.gob.es/pae_Home/pae_Documentacion/pae_Metodolog/pae_Metrica_v3.html).
            txt-cover: Métrica v3
            ---
            ''').strip())
            for level, i in self.iter_index("https://manuel.cillero.es/doc/metodologia/metrica-3/procesos-principales/desarrollo/"):

                sp = get_sp(level+1, i)

                source = self.get_source(sp)

                if source:
                    i.soruce = source
                    f.write('\n\n{h} [{title}]({source}) {h} {{#{id}}}\n\n'.format(h='#'*level, id=id_url[norm_url(i.url)], **dict(i)))
                else:
                    f.write('\n\n{h} {title} {h} {{#{id}}}\n\n'.format(h='#'*level, id=id_url[norm_url(i.url)], **dict(i)))

                md = to_md(sp).strip()
                for a in sp.findAll("a"):
                    if a.attrs.get("href", "").startswith("#a"):
                        a.extract()
                if len(re_sp.sub("", sp.get_text()).strip())==0:
                    continue

                f.write(md)

if __name__ == "__main__":
    c = CrawlMetrica("content/posts/otros/")
    c.save_index()
    c.save_book()
