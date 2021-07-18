from bs4 import BeautifulSoup, Tag
from pelican import contents, signals
import re

re_caption = re.compile(r"^Tabla (\d+): .+")

def add_class(n, name):
    c = n.attrs.get("class", None)
    if c is None or len(c) == 0:
        n.attrs["class"] = name
    elif isinstance(c, list):
        n.attrs["class"].append(name)
    elif isinstance(c, str):
        n.attrs["class"] = c+" "+name


def mod_content(content, *args, **kargv):
    if isinstance(content, contents.Static):
        return
    soup = BeautifulSoup(content._content, 'html.parser')

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
            m = re_caption.match(text)
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

    for tr in soup.select("tbody tr"):
        td = tr.findAll(["td", "th"])[0]
        if td.name == "td":
            st = td.find("strong")
            if st and td.get_text().strip() == st.get_text().strip():
                st.unwrap()
                td.name = "th"

    soup.renderContents()
    content._content = soup.decode()


def register():
    signals.content_object_init.connect(mod_content)
