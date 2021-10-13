from .decorators import Cache
import requests
import xmltodict
import re
from urllib.parse import urlparse, parse_qs

re_num = re.compile(r"\d+")
re_sp = re.compile(r"\s+")

class BoeApi:
    def __init__(self):
        pass

    @Cache(file="config/boe/{}.json")
    def get(self, id):
        r = requests.get("https://www.boe.es/diario_boe/xml.php?id="+id)
        js = xmltodict.parse(r.text)
        return js

    def safe_get(self, url):
        prs = urlparse(url)
        if prs.query is None:
            return None
        dom = prs.netloc
        if dom != "www.boe.es":
            return None
        qsl = parse_qs(prs.query)
        ids = qsl.get("id")
        if ids is None or len(ids)==0:
            return None
        id = ids[0]
        return BOE(id)

def to_re(phrase):
    phrase = re_sp.sub(" ", phrase).strip()
    words = phrase.split()
    words=[]
    for word in phrase.split():
        w = word[0]
        u = w.upper()
        l = w.lower()
        if len(word)==1 or u == l or word == word.upper():
            words.append(re.escape(word))
            continue
        word = "["+u+l+"]"+re.escape(word[1:])
        words.append(word)
    return " +".join(words)

class BOE:
    def __init__(self, id):
        if id.startswith("http"):
            pr = urlparse(id)
            qr = parse_qs(pr.query)
            id = qr['id'][0]
        self.js = BoeApi().get(id)

    @property
    def meta(self):
        return self.js['documento']['metadatos']

    @property
    def id(self):
        return self.meta['identificador']

    @property
    def title(self):
        if self.meta['numero_oficial'] is None:
            return self.titulo
        r = []
        r.append(self.meta['rango']['#text'])
        r.append(self.meta['numero_oficial'])
        return " ".join(r)

    @property
    def numero(self):
        return self.meta['numero_oficial']

    @property
    def titulo(self):
        r = []
        tt = re_sp.sub(" ", self.meta['titulo']).strip()
        for t in tt.split(","):
            t = t.strip()
            if len(t)==0:
                continue
            if not re_num.search(t):
                break
            r.append(t)
        return ", ".join(r)

    @property
    def nula(self):
        if self.id == "BOE-A-1999-23750":
            return "derogada"
        ks = {
            "estatus_derogacion": "derogada",
            "vigencia_agotada": "agotada",
            "judicialmente_anulada": "anulada"
        }
        for k, label in ks.items():
            if self.meta[k].strip()=="S":
                return label
        return False

    @property
    def alias(self):
        r = []
        if self.id == "BOE-A-2015-10565":
            r.append("Procedimiento Administrativo Común")
            r.append("PACAP")
            r.append("PAC")
        if self.id == "BOE-A-2018-16673":
            r.append("LOPD-GDD")
            r.append("LOPDGDD")
        if self.id == "BOE-A-2015-10566":
            r.append("Régimen Jurídico del Sector Público")
            r.append("RJSP")
        if self.id == "BOE-A-2013-12887":
            r.append("LTAIBG")
        return tuple(r)

    @property
    def re(self):
        tt = self.titulo.split(", ")
        tt = list(map(lambda x: to_re(x), tt))
        rr = ''
        for t in reversed(tt[1:]):
            rr=rr+"(, "+t+")?"
        rr = tt[0]+rr
        arr = [self.id, rr] + list(to_re(a) for a in self.alias)
        return re.compile(r"\b(" + ("|".join(arr)) + r")\b")
