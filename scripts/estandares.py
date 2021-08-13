from .core.web import Web
from munch import Munch, DefaultMunch
from textwrap import dedent
import re

re_sp = re.compile(r"\s+")

def get_text(n, dash=False):
    ps = n.findAll("p")
    if len(ps)>1:
        for i, p in enumerate(ps):
            if i < len(ps)-1:
                p.append("<br/>")
    txt = n.get_text()
    txt = txt.replace("–", " - ")
    if dash:
        txt = txt.replace("-", " - ")
    txt = txt.replace("<br/> ", "<br/>")
    txt = re_sp.sub(" ", txt)
    txt = txt.strip().rstrip(" .")
    return txt

w=Web()
w.get("https://www.boe.es/buscar/act.php?id=BOE-A-2012-13501")

items=[]
for tr in w.soup.select("table tr"):
    tds = tr.findAll("td")
    if len(tds)<9:
        continue
    item=Munch(
        cadena=get_text(tds[0], dash=True),
        categoria=get_text(tds[1], dash=True),
        subcategoria=None,
        comun=get_text(tds[2]),
        formal=get_text(tds[3]),
        tipo=(get_text(tds[4]) or get_text(tds[5])),
        estado=get_text(tds[8])
    )
    if item.comun == "Fechas y horas":
        item.comun = "ISO 8601:2004"
    if item.comun == "BebM":
        item.comun = "WebM"
    if item.comun == "MPEG - 4":
        item.comun = "MPEG-4"
    if item.formal == "SVG":
        item.comun = item.formal
        item.formal = get_text(tds[4])
        item.tipo = get_text(tds[5])
    if item.comun == "Comma Separated Values":
        item.comun = '[CSV](https://es.wikipedia.org/wiki/Valores_separados_por_comas "Valores separados por comas"){.abbr}'
    if item.formal == "SHA":
        item.formal = get_text(tds[4])
        item.tipo = get_text(tds[5])
    if " - " in item.categoria:
        item.categoria, item.subcategoria = item.categoria.split(" - ")
    elif item.categoria == "Codificación idioma":
        item.categoria, item.subcategoria = "Codificación", "Idioma"
    items.append(item)

formatos=[]
for i, item in enumerate(items):
    flag = False
    prev = DefaultMunch() if i==0 else items[i-1]
    if item.cadena != prev.cadena:
        if formatos:
            print("", ", ".join(formatos), end="")
            formatos=[]
        print("\n* "+item.cadena+":", end="")
        flag=True
    if flag or item.categoria != prev.categoria:
        if formatos:
            print("", ", ".join(formatos), end="")
        formatos=[]
        print("\n    * "+item.categoria+":", end="")
        flag=True
    if flag or item.subcategoria != prev.subcategoria:
        if formatos:
            print("", ", ".join(formatos), end="")
        formatos=[]
        if item.subcategoria:
            print("\n        * "+item.subcategoria+":", end="")
    for f in item.comun.split("<br/> "):
        f = f.replace("ETS TR", "ETSI TR")
        f = f.strip("() ")
        if item.estado == "En abandono":
            f = "<del title='En abandono: {0}'>{0}</del>".format(f)
        if item.tipo == "Uso generalizado":
            f = "*"+f+"*"
        formatos.append(f)

if formatos:
    print("", ", ".join(formatos), end="")
print('''

**Nota**: En cursiva los que son de tipo *Uso generalizado* y no *Abierto*,
tachados los que están en estado *En abandono* y no en *Admitido*.
''')
