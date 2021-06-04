import re
from munch import Munch
import yaml
from os import makedirs
from os.path import basename, dirname
from markdown import markdown


import bs4
from weasyprint import CSS, HTML
from urllib.parse import urlparse

re_head = re.compile(r"<(h[1-6])>\s*(.*?)\s*</\1>", re.MULTILINE)

def read(file):
    ext = file.rsplit(".")[-1].lower()
    if ext in ("yml", "yaml"):
        with open(file, "r") as f:
            yml = yaml.load(f, Loader=yaml.FullLoader)
            return Munch.fromDict(yml)
    if ext in ("md", ):
        md=Munch(
            meta=None,
            md=None,
            html=None
        )
        with open(file, "r") as f:
            for l in f.readlines():
                sl = l.strip()
                if md.md is not None:
                    md.md.append(l)
                    continue
                if sl == '---':
                    if md.meta is None:
                        md.meta = []
                    else:
                        md.md = []
                    continue
                md.meta.append(l)
        md.meta = "".join(md.meta)
        md.md = "".join(md.md)
        md.html = markdown(md.md)
        md.meta = yaml.safe_load(md.meta)
        md.meta = Munch.fromDict(md.meta)
        return md

    with open(file, "r") as f:
        return f.read()

def write(file, text):
    dir = dirname(file)
    makedirs(dir, exist_ok=True)
    with open(file, "w") as f:
        f.write(text)


def get_tpt(title, rec=None, css_screen=None, css_print=None, head=None, content=None):
    html = '''
    <!DOCTYPE html>
    <html>
        <head>
            <title>{title}</title>
            <meta charset="utf-8"/>
            <link rel="stylesheet" type="text/css" media="screen" href="{css_screen}"/>
            <link rel="stylesheet" type="text/css" media="print" href="print.css" />
            <link rel="stylesheet" type="text/css" media="print" href="{css_print}" />
            {head}
        </head>
        <body>
            <div class="content">
            {content}
            </div>
        </body>
    </html>
    '''.format(title=title, css_screen=css_screen, css_print=css_print, head=(head or ""), content=(content or ""))
    soup = bs4.BeautifulSoup(html, 'lxml')
    for style in soup.findAll("link"):
        if style.attrs["href"] == "None":
            style.extract()
        elif rec:
            style.attrs["href"] = rec + style.attrs["href"]
    return soup


def get_page_body(boxes):
    for box in boxes:
        if box.element_tag == 'body':
            return box
        return get_page_body(box.all_children())


def get_html(soup):
    html = soup.prettify()
    return re_head.sub(r"<\1>\2</\1>", html)


def get_css_print(fuente):
    dir = dirname(fuente)
    styles = []
    with open(fuente, "r") as f:
        soup = bs4.BeautifulSoup(f.read(), 'lxml')
        for link in soup.findAll("link"):
            if link.attrs.get("media", None) == "print":
                css = dir + "/" + link.attrs["href"]
                text = map(lambda x:x.strip(), read(css).strip().split("\n"))
                text = list(filter(lambda x:len(x)>0, text))
                while len(text) and text[0].startswith('@import "'):
                    ln = text.pop(0)
                    ln = ln.split('"')[1]
                    styles.append(dirname(css)+"/"+ln)
                styles.append(css)
    return styles


def get_footer(styles, codigo, page):
    string = '<div class="pag"><span>%s</span><br/>%s</div>' % (codigo, page)
    html = HTML(string=string)
    footer = html.render(stylesheets=styles)
    footer_page = footer.pages[0]
    footer_body = get_page_body(footer_page._page_box.all_children())
    footer_body = footer_body.copy_with_children(footer_body.all_children())
    return footer_body.all_children()


def html_to_pdf(fuente, codigo):
    delFuente = False
    if fuente.endswith(".md"):
        delFuente = True
        MD=read(fuente)
        soup = get_tpt(MD.meta.title, content=MD.html)
        #soup.find("link").attrs["href"]=dirname(fuente)+"/print.css"
        fuente = fuente.rsplit(".", 1)[0] + ".html"
        with open(fuente, "w") as f:
            f.write(str(soup))

    styles = get_css_print(fuente)

    html = HTML(fuente).render(stylesheets=styles)

    for i, page in enumerate(html.pages):
        page_body = get_page_body(page._page_box.all_children())
        if i % 2 == 0:
            p = int((i / 2) + 1)
            page_body.children += get_footer(styles, codigo, p)

    html.write_pdf(fuente[:-5] + ".pdf")

    if delFuente:
        os.remove(fuente)

def clean_url(url):
    spl = url.split("://", 1)
    if len(spl)==2:
        url = spl[1]
    if url.lower().startswith("www") and "." in url[3:5]:
        url = url.split(".", 1)[1]
    url = url.rstrip("/")
    return url


def url_key(url):
    p = urlparse(url)
    dom = p.netloc
    if dom.lower().startswith("www") and "." in url[4:6]:
        dom = dom.split(".", 1)[1]
    r = (
        tuple(reversed(dom.split("."))),
        p.path,
        p.query,
        p.fragment,
        p.scheme,
        clean_url(url)
    )
    return r
