import os
import re
from munch import Munch
import yaml


import bs4
from weasyprint import CSS, HTML

re_head = re.compile(r"<(h[1-6])>\s*(.*?)\s*</\1>", re.MULTILINE)

def read(file):
    ext = file.rsplit(".")[-1].lower()
    if ext in ("yml", "yaml"):
        with open(file, "r") as f:
            yml = yaml.load(f, Loader=yaml.FullLoader)
            return Munch.fromDict(yml)

    with open(file, "r") as f:
        return f.read()


def get_tpt(title, rec=None, css_screen=None, css_print=None, extra=None):
    html = '''
    <!DOCTYPE html>
    <html>
        <head>
            <title>{}</title>
            <meta charset="utf-8"/>
            <link rel="stylesheet" type="text/css" media="screen" href="{}"/>
            <link rel="stylesheet" type="text/css" media="print" href="print.css" />
            <link rel="stylesheet" type="text/css" media="print" href="{}" />
            {}
        </head>
        <body>
            <div class="content">
            </div>
        </body>
    </html>
    '''.format(title, css_screen, css_print, (extra or ""))
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
    dirname = os.path.dirname(fuente)
    styles = []
    with open(fuente, "r") as f:
        soup = bs4.BeautifulSoup(f.read(), 'lxml')
        for link in soup.findAll("link"):
            if link.attrs.get("media", None) == "print":
                css = dirname + "/" + link.attrs["href"]
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
    styles = get_css_print(fuente)

    html = HTML(fuente).render(stylesheets=styles)

    for i, page in enumerate(html.pages):
        page_body = get_page_body(page._page_box.all_children())
        if i % 2 == 0:
            p = int((i / 2) + 1)
            page_body.children += get_footer(styles, codigo, p)

    html.write_pdf(fuente[:-5] + ".pdf")

def clean_url(url):
    spl = url.split("://", 1)
    if len(spl)==2:
        url = spl[1]
    if url.lower().startswith("www") and "." in url[4:6]:
        url = url.split(".", 1)[1]
    url = url.rsplit("/")
    return url
