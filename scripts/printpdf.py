from os import remove
from os.path import isfile
from pathlib import Path
from textwrap import dedent

import bs4
import yaml
from munch import Munch
from weasyprint import CSS, HTML
import sys

from .core.util import rcglob, read, write

ROOT = Path(__file__).parent.parent.resolve()
PRINT_CSS = str(ROOT / "themes/mini/static/css/print.css")


class PDF:
    def __init__(self, print=PRINT_CSS):
        if not isfile(print):
            raise Exception(print+" no existe")
        self.footer = '<div class="pag"><span>{code}</span><br/>{page}</div>'
        self.print_css = print
        self.template = dedent('''
            <!DOCTYPE html>
            <html>
                <head>
                    <title>{title}</title>
                    <meta charset="utf-8"/>
                    <link rel="stylesheet" type="text/css" media="print" href="%s" />
                </head>
                <body class="{body_class}"><main>
                {content}
                </main></body>
            </html>
        ''' % (self.print_css))

    def get_css_print(sef, fuente):
        dir = Path(fuente).parent
        styles = []
        with open(fuente, "r") as f:
            soup = bs4.BeautifulSoup(f.read(), 'lxml')
            for link in soup.findAll("link"):
                if link.attrs.get("media", None) == "print":
                    css = dir / link.attrs["href"]
                    styles.append(str(css))
        return styles

    def get_page_body(self, boxes):
        for box in boxes:
            if box.element_tag == 'body':
                return box
            return self.get_page_body(box.all_children())

    def get_footer(self, styles, codigo, page):
        string = self.footer.format(code=codigo, page=page)
        html = HTML(string=string)
        footer = html.render(stylesheets=styles)
        footer_page = footer.pages[0]
        footer_body = self.get_page_body(footer_page._page_box.all_children())
        footer_body = footer_body.copy_with_children(footer_body.all_children())
        return footer_body.all_children()

    def to_pdf(self, fuente, codigo=None, body_class=None, overview=False):
        fuente = str(fuente)
        target = fuente.rsplit(".", 1)[0] + ".pdf"
        if isfile(target) and not overview:
            return
        delFuente = False
        if fuente.endswith(".md"):
            delFuente = True
            MD = read(fuente)
            codigo = MD.meta.pdf_code
            body_class = MD.meta.get('body_class', "")
            html = self.template.format(title=MD.meta.title, content=MD.html, body_class=body_class)
            fuente = fuente.rsplit(".", 1)[0] + ".html"
            with open(fuente, "w") as f:
                f.write(html)

        styles = self.get_css_print(fuente)

        html = HTML(fuente).render(stylesheets=styles)

        for i, page in enumerate(html.pages):
            page_body = self.get_page_body(page._page_box.all_children())
            if i % 2 == 0:
                p = int((i / 2) + 1)
                page_body.children += self.get_footer(styles, codigo, p)

        html.write_pdf(target)

        if delFuente:
            remove(fuente)


if __name__ == "__main__":
    overview = len(sys.argv)==2 and self.salida[1]=="overview"
    for md in rcglob(ROOT/"content/posts", "md"):
        MD = read(md)
        if MD.meta.get("pdf_code"):
            print(md)
            pdf = PDF()
            pdf.to_pdf(md, overview=overview)
