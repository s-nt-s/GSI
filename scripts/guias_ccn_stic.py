from .core.web import Web, FF
import re
from time import sleep

re_sp = re.compile(r"\s+")
re_cod = re.compile(r"^(CCN-STIC)\s+(\d+)\S*")

def get_session(url):
    f = FF()
    f.get(url)
    sleep(1)
    w = Web()
    w.s = f.get_session()
    f.close()
    w.get(url)
    return w

def get_text(n):
    if n is None:
        return None
    txt = n.get_text()
    txt = re_sp.sub(" ", txt)
    return txt.strip()

guias = set()
w = get_session("https://www.ccn-cert.cni.es/guias/guias-series-ccn-stic.html")
urls = list(w.soup.select("div.item-page a"))
links = list(a.attrs["href"] for a in urls)
for url in urls:
    cap = get_text(url)
    url = url.attrs["href"]
    w.get(url)
    trs = list(w.soup.select("#tablesort tbody tr"))
    if len(trs)==0:
        w = get_session(url)
        trs = list(w.soup.select("#tablesort tbody tr"))
    for tr in w.soup.select("#tablesort tbody tr"):
        tds = tr.findAll("td")
        file = tds[-1].find("a")
        if file is not None:
            file = file.attrs["href"]
            if file in links:
                continue
        for n in tds[0].select("ul"):
            n.extract()
        cod = get_text(tds[0])
        cod = re_cod.sub(r"\1-\2", cod)
        name = ""
        slp = cod.split(" ", 1)
        if len(slp)==2:
            cod, name = slp
        guias.add((cod.upper(), file, name))

def sort_keys(x):
    cod, file, name = x
    return (0 if file else 9, cod, name, file)

done = set()
for cod, file, name in sorted(guias,key=sort_keys):
    if cod in done:
        continue
    done.add(cod)
    num = cod.rsplit("-", 1)[-1]
    while len(num)>0 and not num.isdigit():
        num = num[:-1]
    if len(num)==0 or not(num.isdigit() and 799 < int(num) < 900):
        continue
    print(cod)
    print(file)
    print(name)
    print("")
