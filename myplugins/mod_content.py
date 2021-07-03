from bs4 import BeautifulSoup
from pelican import contents, signals


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

    soup.renderContents()
    content._content = soup.decode()


def register():
    signals.content_object_init.connect(mod_content)
