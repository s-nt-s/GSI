from bs4 import BeautifulSoup, Tag, NavigableString
from pelican import contents, signals
import re
from munch import Munch
from .core.util import get_dom, get_class_dom, readyaml
from .core.boe import BoeApi
from .core.abbr import Abbr
from pathlib import Path

import unidecode

re_tabcaption = re.compile(r"^Tabla( \d+)?: .+")
re_figcaption = re.compile(r"^Figura( \d+)?: .+")
re_sp = re.compile(r"\s+")
heads=tuple("h"+str(i) for i in range(1,7))

fake_sep = "@#~½$"
fake_rem = "x@@@BORRAME@@@x"

SUP="⁰¹²³⁴⁵⁶⁷⁸⁹"
re_sup=re.compile(r"(["+SUP+"]+)")

def add_class(n, name):
    if name is None:
        return
    c = n.attrs.get("class", None)
    if c is None or len(c) == 0:
        n.attrs["class"] = name
    elif isinstance(c, list):
        if name not in c:
            n.attrs["class"].append(name)
    elif isinstance(c, str):
        if (" "+name+" ") not in " "+c+" ":
            n.attrs["class"] = c+" "+name

def get_anchor_id(id):
    return BeautifulSoup('''
        <a class="anchormark" aria-hidden="true" href="#{0}"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true">
            <path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path>
        </svg></a>
    '''.format(id), "html.parser")

def find_text(soup, re_text, *no_parent):
    for n in soup.findAll(text=re_text):
        if not any(n.find_parent(p) for p in no_parent):
            yield n

def myzip(arr):
    arr = list(arr)
    return zip(range(1, len(arr)), arr[1:], arr)

def toTag(template, *args, **kargv):
    args = list(args)
    for i, v in enumerate(args):
        if isinstance(v, str):
            args[i]=v.strip()
    for k, v in list(kargv.items()):
        if isinstance(v, str):
            kargv[k]=v.strip()
    if args or kargv:
        template = template.format(*args, **kargv)
    return BeautifulSoup(template, "html.parser")

def to_txtline(node):
    node = BeautifulSoup(str(node), 'html.parser')
    for br in node.findAll("br"):
        br.replaceWith("\n")
    for p in node.findAll("p"):
        p.append("\n")
    txt = node.get_text()
    txt = re_sp.sub(" ", txt).strip()
    return txt

def find_in_bloque(ha, select=None):
    if ha is None:
        return []
    if ha.name not in heads:
        raise Exception(id+" no es un head")
    hds = heads[:heads.index(ha.name)+1]
    sbl = []
    for e in ha.next_siblings:
        if e.name in hds:
            return sbl
        if select is None or select == e.name:
            sbl.append(e)
        elif not isinstance(e, NavigableString):
            sbl.extend(e.select(select))
    return sbl

def real_next(n):
    for e in n.next_siblings:
        if isinstance(e, NavigableString) and e.strip()=="":
            continue
        return e

def set_notas(soup):

    def fun_sup(x):
        o = x.group(1)
        x = unidecode.unidecode(o)
        return '<sup class="nota" data-nota="{0}" data-text="{1}">{0}</sup>'.format(x, o)


    for n in find_text(soup, re.compile(r".*["+SUP+"].*"), "pre", "code", "abbr"):
        a = n.find_parent("a")
        if a and "abbr" in a.attrs.get("class", ""):
            continue
        n.replaceWith(BeautifulSoup(re_sup.sub(fun_sup, n), "html.parser"))

    sp_notas = list(soup.select("sup.nota"))
    if len(sp_notas)==0:
        return

    ol_notas = None
    h1_notas = soup.select_one("#notas")
    if h1_notas:
        ol_notas = h1_notas.find_next("ol")

    gr_notas = {}
    g = 0
    next_n = 1
    for i, nota in enumerate(sp_notas):
        n = int(nota.attrs["data-nota"])
        if n not in (1, next_n):
            nota.replaceWith(nota.attrs["data-text"])
            continue
        if n == 1:
            if i>0:
                notas[-1].attrs["data-last"] = "true"
            g = g + 1
        nota.attrs["data-grupo"]=g
        next_n = n + 1

    sp_notas = list(soup.select("sup.nota"))
    if len(sp_notas)==0:
        return
    sp_notas[-1].attrs["data-last"] = "true"
    for nota in soup.select("sup.nota[data-last='true']"):
        if ol_notas:
            ol = ol_notas
        else:
            ol = nota.find_next("ol")
        gr_notas[nota.attrs["data-grupo"]]=ol

    for nota in sp_notas:
        g = int(nota.attrs["data-grupo"])
        n = int(nota.attrs["data-nota"])
        ol = gr_notas[g]
        if ol is None:
            continue
        add_class(ol, "notas")
        li = ol.findAll("li")
        if len(li)<n:
            continue
        li = li[n-1]
        id = "notas"+str(g)+"_"+str(n)
        li.attrs["id"]=id
        nota.attrs["title"]=to_txtline(li)
        a = soup.new_tag('a', href='#'+id)
        a.string = str(n)
        nota.string = ""
        nota.append(a)
        for a in list(nota.attrs.keys()):
            if a.startswith("data-"):
                del nota.attrs[a]

def mod_content(content, *args, **kargv):
    if isinstance(content, contents.Static):
        return
    if content.metadata.get('changeable', False):
        return

    _content = content._content
    for k, v in content.metadata.get('replace', {}).items():
        _content = _content.replace(k, v)

    _content = re.sub(r"<([a-z]+)\s+data-open([^>]*)></\1>", r"<\1 \2>", _content)
    _content = re.sub(r"<([a-z]+)\s+data-close([^>]*)></\1>", r"</\1>", _content)
    soup = BeautifulSoup(_content, 'html.parser')

    for td in soup.findAll(['th', 'td']):
        align = td.attrs.get("align", None)
        if align is not None:
            del td.attrs["align"]
            if align != "left":
                add_class(td, align)
    for table in soup.findAll("table"):
        cpt = table.find_next_sibling("p")
        if cpt is not None:
            text = cpt.get_text().strip()
            m = re_tabcaption.match(text)
            if m:
                spn = cpt.find(lambda x: x.name=="span" and len(x.get_text().strip())==0 and x.attrs.keys())
                if spn:
                    spn.extract()
                cpt.name = "caption"
                table.insert(0, cpt)
                m = m.group(1)
                if m is None or len(m.strip())==0:
                    m = None
                if m is None:
                    cpt.replaceWith(BeautifulSoup(str(cpt).replace("Tabla: ", ""), "html.parser"))
                elif table.attrs.get("id") is None:
                    table.attrs["id"]="tb"+m.strip()
                if spn:
                    for k, v in spn.attrs.items():
                        table.attrs[k]=v
        if table.select_one("*[rowspan]") or table.select_one("*[colspan]"):
            continue

        changed = True
        while changed:
            changed = False
            for table in soup.findAll("table"):
                tbody = table.find("tbody")
                thead = table.find("thead")
                if None in (tbody, thead):
                    continue
                tr = tbody.find("tr")
                if None in (tr, thead.find("tr")):
                    continue
                if tr.find(lambda n: n.name=="td" and n.get_text().strip()=="^"):
                    for td in tr.findAll("td"):
                        td.name = "th"
                    table.find("thead").append(tr)
                    changed = True

        for tbody in soup.findAll(["thead", "tbody"]):
            trs = list(tbody.findAll("tr"))
            for i, tr in reversed(list(enumerate(trs))):
                tds = tr.findAll(["td", "th"])
                for c, td in reversed(list(enumerate(tds))):
                    text = td.get_text().strip()
                    if text == "<":
                        prev = tds[c-1]
                        prev.attrs["colspan"] = prev.get("colspan", 0) + td.get("colspan", 1) + 1
                        td.extract()
                    elif text == ">":
                        post = tds[c+1]
                        post.attrs["colspan"] = post.get("colspan", 0) + td.get("colspan", 1) + 1
                        td.extract()
                if i == 0:
                    continue
                for c, td in enumerate(tds):
                    text = td.get_text().strip()
                    if text == "^":
                        prev = trs[i-1].findAll(["td", "th"])[c]
                        prev.attrs["rowspan"] = prev.get("rowspan", 0) + td.get("rowspan", 1) + 1
                        td.extract()

    changed = True
    while changed:
        changed = False
        for tr in soup.select("tbody tr"):
            td = tr.find("td")
            if td and td.name == "td":
                st = td.find("strong")
                txt = td.get_text().strip()
                if st and txt == st.get_text().strip():
                    st.unwrap()
                    td.name = "th"
                    changed = True
                elif len(txt)>2 and txt[0] == txt[-1] and txt[0] == "▼":
                    td.name = "th"
                    changed = True


    for td in soup.findAll("td"):
        if td.get_text().strip().lower() == 'x':
            add_class(td, "td_x")

    '''
    for td in soup.findAll("td"):
        st = td.find("strong")
        if st and td.get_text().strip() == st.get_text().strip():
            st.unwrap()
            add_class(td, "strong")
    '''

    for img in soup.select("img"):
        p = img.find_parent("p")
        if p is None or len(p.get_text().strip())>0:
            continue
        cpt = p.find_next_sibling("p")
        if cpt is None:
            continue
        text = cpt.get_text().strip()
        m = re_figcaption.match(text)
        if m:
            spn = cpt.find(lambda x: x.name=="span" and len(x.get_text().strip())==0 and x.attrs.keys())
            if spn:
                spn.extract()
            add_class(p, "fig")
            p.name = "figure"
            cpt.name = "figcaption"
            p.append(cpt)
            m = m.group(1)
            if m is None or len(m.strip())==0:
                m = None
            if m is None:
                cpt.replaceWith(BeautifulSoup(str(cpt).replace("Figura: ", ""), "html.parser"))
            elif p.attrs.get("id") is None:
                p.attrs["id"]="fg"+m
            cap = text.split(":", 1)[1].strip()
            for att in ("title", "alt"):
                if not img.attrs.get(att):
                    img.attrs[att] = cap
            if spn:
                for k, v in spn.attrs.items():
                    p.attrs[k]=v

    for img in soup.select("img"):
        t = img.attrs.get("title")
        if t is None or len(t.strip()) == 0:
            a = img.attrs.get("alt")
            if a is not None and len(a.strip()) > 0:
                img.attrs["title"] = a

    for h in soup.findAll(heads):
        if h.attrs.get("id") in (None, ""):
            text = re_sp.sub(" ", h.get_text())
            text = text.strip()
            if len(text)>0:
                text = text.lower()
                text = unidecode.unidecode(text)
                text = text.replace(":", "")
                text = text.strip()
                h.attrs["id"]=text.replace(" ", "-")
        if h.attrs.get("id") not in (None, ""):
            add_class(h, "anchormark")
            h.insert(0, get_anchor_id(h.attrs["id"]))

    for a in soup.findAll("a"):
        cls = get_class_dom(a.attrs.get("href"))
        add_class(a, cls)

    for table in soup.findAll("tbody"):
        rowspan = False
        for td in table.select(":scope *[rowspan]"):
            if td.attrs.get("rowspan") not in (None, 1, "1"):
                rowspan = True
        if rowspan:
            add_class(table, "hasRowspan")

    if content.metadata.get('build_notas', False):
        set_notas(soup)

    for ul in find_in_bloque(soup.select_one("#bibliografia"), "ul"):
        if ul.find_parent(["ul", "ol", "li"]) in (None, ul):
            add_class(ul, "bibliografia")

    grupos=[[]]
    for i, fig, prev in myzip(soup.select("figure")):
        if real_next(prev) == fig:
            if prev not in grupos[-1]:
                grupos[-1].append(prev)
            grupos[-1].append(fig)
        else:
            grupos.append([])
    for grupo in grupos:
        if len(grupo)>1:
            div = soup.new_tag('div')
            div.attrs["class"] = 'figgroup figgroup'+str(len(grupo))
            grupo[0].wrap(div)
            for g in grupo[1:]:
                div.append(g)

    boeApi = BoeApi()
    for a in soup.select("a[href]"):
        href = a.attrs["href"]
        boe = boeApi.safe_get(href)
        if boe:
            if boe.nula:
                add_class(a, boe.nula)
            if not a.attrs.get("title"):
                nula = boe.nula.title()+": " if boe.nula else ""
                a.attrs["title"] = nula+boe.titulo

    hardCode(content, soup)

    soup.renderContents()
    _content = soup.decode()

    content._content = _content


def fake_sub(r, n, x):
    nw = x.group(0)
    doRm = None
    if "rm" in r.groupindex and x.group("rm") not in (None, ""):
        doRm = x.group("rm")
    if doRm:
        nw = nw.replace(x.group("rm"), fake_rem)
        r = re.compile(r.pattern.replace("(?P<rm>", "(?P<rm>"+fake_rem+"|"), r.flags)

    if n is not None:
        nw = r.sub(n, nw)
    if doRm:
        nw = nw.replace(fake_rem, "")
    nw = fake_sep.join(list(nw))
    return fake_sep+nw+fake_sep

def load_abbr(pelican_object):
    abbr = []
    for md in pelican_object.settings.get('CONTENT_MARKD', []):
        meta = readyaml("content/"+md)
        if meta is None:
            continue
        meta = meta.get('abbr')
        if meta is None:
            continue
        ab = Abbr(**meta)
        ab.add_url("{filename}/"+md, insert=0)
        abbr.append(ab)

    abbr.extend(Abbr.load(pelican_object.settings['ABBR_CONFIG']))
    for a in abbr:
        print(a.re)

    pelican_object.settings['ABBR_CONFIG'] = abbr

def do_abbr(soup):
    if not abbrs:
        return
    for n in soup.findAll(text=True):
        if n.find_parent("a"):
            continue
        if n.find_parent("abbr"):
            continue
        cd = n.find_parent("code")
        if cd and cd.find_parent("pre"):
            continue
        txt = str(n)
        for abbr in abbrs:
            txt = abbr.re.sub(lambda x:fake_sub(abbr.re, abbr.new_text, x), txt)
        txt = txt.replace(fake_sep, "")
        if txt != str(n):
            n.replaceWith(toTag(txt))

def register():
    #signals.initialized.connect(load_abbr)
    signals.content_object_init.connect(mod_content)


#########################

def findBetween(soup, start, end, *args):
    ini = False
    for n in soup.findAll(args):
        txt = n.get_text().strip()
        if ini is False and txt != start:
            continue
        if ini is True and txt == end:
            break
        ini = True
        yield n

def cdc(s, kv, df=None):
    if df is None:
        df = s
    return kv.get(s, df)

def hardCode(content, soup):
    if content.source_path.endswith("/csstic.md"):
        num = 1
        for ol in soup.findAll("ol"):
            ol.attrs["start"] = str(num)
            num = num + len(ol.findAll("li"))
    if content.source_path.endswith("-patrones.md"):
        table = BeautifulSoup('''
        <table class="tabla_patrones">
            <caption>Resumen de patrones de diseño</caption>
            <thead>
                <tr>
                </tr>
            </thead>
            <tbody>
                <tr>
                </tr>
            </tbody>
        </table>
        ''', "html.parser")
        cur = None
        tip = {}
        for n in findBetween(soup, "Creacional", "Arquitectura", "h1", "h2", "ul"):
            txt = n.get_text().strip()
            if txt == "Otros":
                continue
            if n.name == "h1":
                cur = str(txt)
                tip[cur]=(n, [])
                continue
            lis = n.findAll("li")
            if lis:
                for l in lis:
                    tip[cur][1].append(l)
            else:
                tip[cur][1].append(n)
        for t, data in tip.items():
            table.find("thead").find("tr").append(toTag("<th>{}</th>", data[0].get_text()))
            ptr = []
            for n in sorted(data[1], key=lambda x:x.get_text().lower()):
                n = toTag(str(n))
                for slc in ("a.anchormark",):
                    for x in n.select(slc):
                        x.extract()
                n = str(n).split(">", 1)[-1].rsplit("<", 1)[0].strip()
                n = "<li>"+n+"</li>"
                ptr.append(n)
            table.find("tbody").find("tr").append(toTag("<td><ul>{}</ul></td>", "\n".join(ptr)))

        soup.find(lambda x:x.name=="h1" and x.get_text().strip()=="Creacional").insert_before(table)

    if content.source_path.endswith("normativa.md") and soup.select_one("table.articulos"):
        for tr in soup.select("table.articulos tbody tr"):
            tds = tr.findAll("td")
            txt = [re_sp.sub(" ", (i.find("a") or i).get_text().strip()) for i in tds]
            url = tr.find("a").attrs["href"]
            art = txt[1]
            atd = tds[1]
            atd.string = ""
            atd.append(BeautifulSoup('<a href="{}"></a>'.format(url), "html.parser"))
            atd = atd.find("a")
            atd.string = art
            if txt[0] == "RGPD":
                atd.attrs["href"] = cdc(art, {
                    "6": "https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:02016R0679-20160504&from=EN#tocId10",
                    "9": "https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:02016R0679-20160504&from=EN#tocId13",
                    "25": "https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:02016R0679-20160504&from=EN#tocId37",
                    "30": "https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:02016R0679-20160504&from=EN#tocId42",
                    "35": "https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:02016R0679-20160504&from=EN#tocId49",
                    "39": "https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:02016R0679-20160504&from=EN#tocId54"
                })
            else:
                if txt[0] == "RD 203/2021":
                    mrk = cdc(art, {
                        "10": "a1-2",
                        "11": "a1-3",
                        "S2": "s2",
                        "19": "a1-11",
                        "20": "a2-2",
                        "21": "a2-3",
                        "22": "a2-4",
                        "26": "a2-8",
                        "29": "a2-11",
                        "30": "a3-2",
                        "31": "a3-3",
                        "32": "a3-4",
                        "33": "a3-5",
                        "37": "a3-9",
                        "38": "a3-10",
                        "40": "a4-2",
                        "41": "a4-3",
                        "42": "a4-4",
                        "43": "a4-5",
                        "55": "a5-7",
                        "60": "a6-2",
                        "62": "a6-4",
                    }, "a"+art)
                else:
                    mrk = cdc(art, {
                        "A1": "ani",
                        "A2": "anii",
                        "A3": "aniii",
                        "DA4": "dacuaa"
                    }, "a"+art)
                atd.attrs["href"] = atd.attrs["href"]+"#"+mrk
        for tbody in soup.select("table tbody"):
            if tbody.select_one("*[rowspan]") or tbody.select_one("*[colspan]"):
                continue
            lstTxt = None
            for tr in tbody.findAll("tr"):
                tds = tr.findAll("td")
                txt = [re_sp.sub(" ", i.get_text().strip()) for i in tds]
                for i, t in enumerate(txt):
                    if len(t.split())<2:
                        add_class(tds[i], "word")
                if lstTxt is not None:
                    for i, (lst, cur) in enumerate(zip(lstTxt, txt)):
                        if lst == cur:
                            add_class(tds[i], "dup")
                lstTxt = txt
