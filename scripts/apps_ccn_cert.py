from .core.web import Web, FF
import re
from time import sleep

re_sp = re.compile(r"\s+")
re_cod = re.compile(r"^(CCN-STIC)\s+(\d+)")

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

def get_desc(s):
    if s == "INES":
        return "Informe Nacional del Estado de Seguridad, permite evaluar regularmente el estado de la seguridad de los sistemas TIC"
    if s == "LUCIA":
        return "Listado Unificado de Coordinación de Incidentes y Amenazas, herramienta para la Gestión de Ciberincidentes"

guias = set()
w = get_session("https://www.ccn-cert.cni.es/soluciones-seguridad.html")
for h in w.soup.select("div.item-page h3"):
    name = h.get_text().strip()
    url = h.find("a").attrs["href"]
    print(name)
    print(url)
    des = get_desc(name)
    if des is None:
        p = h.find_parent("div").find("p")
        des = re_sp.sub(" ", p.get_text()).strip()
    des = des + " (CCN-CERT)"
    print(des)
    print("")
