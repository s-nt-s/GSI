from bs4 import BeautifulSoup, Tag
from pelican import contents, signals
import re
from .util import get_dom, get_class_dom
from .mod_html import ModHtml

import unidecode

re_tabcaption = re.compile(r"^Tabla (\d+|X): .+")
re_figcaption = re.compile(r"^Figura (\d+|X): .+")
re_sp = re.compile(r"\s+")
heads=tuple("h"+str(i) for i in range(1,7))

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

def mod_content(content, *args, **kargv):
    if isinstance(content, contents.Static):
        return


    def fun_sup(x):
        x = [str(SUP.index(n)) for n in x.group(1)]
        x = "".join(x)
        return '<sup class="nota" data-nota="{0}">{0}</sup>'.format(x)

    _content = re_sup.sub(fun_sup, content._content)
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
                cpt.name = "caption"
                table.insert(0, cpt)
                if table.attrs.get("id") is None:
                    table.attrs["id"]="tb"+m.group(1)
        if table.select_one("*[rowspan]") or table.select_one("*[colspan]"):
            continue
        for tbody in soup.findAll(["thead", "tbody"]):
            trs = list(tbody.findAll("tr"))
            for i, tr in reversed(list(enumerate(trs))):
                tds = tr.findAll(["td", "th"])
                for c, td in reversed(list(enumerate(tds))):
                    if c == 0:
                        continue
                    text = td.get_text().strip()
                    if text == "<":
                        prev = tds[c-1]
                        prev.attrs["colspan"] = prev.get("colspan", 0) + td.get("colspan", 1) + 1
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
                if st and td.get_text().strip() == st.get_text().strip():
                    st.unwrap()
                    td.name = "th"
                    changed = True
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
            add_class(p, "fig")
            p.name = "figure"
            cpt.name = "figcaption"
            p.append(cpt)
            if p.attrs.get("id") is None:
                p.attrs["id"]="fg"+m.group(1)

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

    #mod = ModHtml(content.settings, content.source_path, soup)
    #mod.set_target()
    #mod.fix_href()

    g = 0
    notas = list(soup.select("sup.nota"))
    if notas:
        notas[-1].attrs["data-last"] = "true"
        for i, nota in enumerate(notas):
            n = int(nota.get_text().strip())
            if n == 1:
                if i>0:
                    notas[-1].attrs["data-last"] = "true"
                g = g + 1
            nota.attrs["data-grupo"]=g
        for nota in soup.select("sup.nota[data-last='true']"):
            ol = nota.find_next("ol")
            if ol:
                ol.attrs["id"]="notas"+str(nota.attrs["data-grupo"])
        for nota in notas:
            g = nota.attrs["data-grupo"]
            n = int(nota.get_text().strip())
            ol = soup.select_one("ol#notas"+str(g))
            if ol:
                li = ol.findAll("li")
                if len(li)>=n:
                    li=li[n-1]
                    id = "notas"+str(g)+"_"+str(n)
                    li.attrs["id"]=id
                    nota.attrs["title"]=re_sp.sub(" ", li.get_text()).strip()
                    a = soup.new_tag('a', href='#'+id)
                    a.string = str(n)
                    nota.string = ""
                    nota.append(a)

    soup.renderContents()
    _content = soup.decode()
    for k, v in content.metadata.get('replace', {}).items():
        _content = _content.replace(k, v)
    content._content = _content


def register():
    signals.content_object_init.connect(mod_content)
