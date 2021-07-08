import re
from textwrap import dedent
from time import sleep

from munch import Munch

from .core.util import clean_url, read, url_key, write
from .core.web import FF, Web

re_sp = re.compile(r"\s+")
re_test = re.compile(r"\bTest\b", re.IGNORECASE)
re_tema = re.compile(r"^\s*Tema\s+\d+\..+")


def get_session(cfg):
    f = FF()
    f.get("https://cas.inap.es/cas/login")
    f.val("username", cfg.username)
    f.val("password", cfg.password)
    f.click("//form[@id='fm1']/*/input[contains(@class,'btn-submit')]")
    sleep(1)
    f.get(cfg.curso)
    sleep(1)
    w = Web()
    w.s = f.get_session()
    f.close()
    return w


class CrawlInap:
    def __init__(self, salida):
        self.cfg = read("config/inap.yml")
        self.salida = salida
        self.w = get_session(self.cfg)
        self.w.get(self.cfg.curso)

        self.CURSO = re_sp.sub(" ", self.w.soup.find("h1").get_text()).strip().capitalize()
        self.CURSO = self.CURSO.replace(".- oep", " - OEP")
        self.CODIGO = re_sp.sub(" ", self.w.soup.select("li.breadcrumb-item a")[-1].get_text()).strip()

    def get_urls(self, slc, text=None):
        urls = self.w.soup.select(slc)
        r = []
        done = set()
        for i in urls:
            url = i.attrs["href"]
            if url in done:
                continue
            txt = re_sp.sub(" ", i.get_text()).strip()
            if text is None or text.search(txt):
                r.append((txt, url))
                done.add(url)
        return r

    def get_bloques(self):
        blq = 0
        URLS = self.get_urls("div.content h3.section-title a")
        for bloque, url in URLS:
            self.w.get(url)
            TEST = self.get_urls("div.content a.aalink", text=re_test)
            if TEST:
                TEMAS = self.w.soup.select_one("#region-main").findAll("p", text=re_tema)
                TEMAS = [re_sp.sub(" ", i.get_text().split(".", 1)[-1]).strip() for i in TEMAS]
                blq = blq + 1
                titulo = bloque.split("-", 1)[-1]
                titulo = titulo.strip()
                titulo = titulo.capitalize()
                b = Munch(
                    bloque=blq,
                    titulo=titulo,
                    url=url,
                    temas=[]
                )
                for (i, ((_, href), txt)) in enumerate(zip(TEST, TEMAS)):
                    t = Munch(
                        tema=i+1,
                        titulo=txt,
                        url=href,
                        feedback=set(),
                        done=0
                    )
                    b.temas.append(t)
                    self.w.get(href)
                    revs = [a.attrs["href"] for a in self.w.soup.findAll("a", text="Revisión")]
                    t.done = len(revs)
                    for rev in revs:
                        self.w.get(rev)
                        for a in self.w.soup.select("div.feedback a"):
                            t.feedback.add(a.attrs["href"])
                yield b

    def save(self):
        feedback = set()
        MD = []
        for b in self.get_bloques():
            MD.append("\n{bloque}. [{titulo}]({url})".format(**dict(b)))
            for t in b.temas:
                MD.append("    {tema}. [{titulo}]({url}) <small>[{done}]</small>".format(**dict(t)))
                feedback = feedback.union(t.feedback)
        feedback = sorted(feedback, key=url_key)
        if feedback:
            MD.append(
                "\nURLs referenciadas en las soluciones de algunos de los tests:\n")
            for a in feedback:
                if "_" in a:
                    MD.append('* <a href="{1}">{0}</a>'.format(clean_url(a), a))
                else:
                    MD.append("* [{}]({})".format(clean_url(a), a))

        MD = "\n".join(MD).strip()
        MD = dedent('''
        ---
        title: {cod} {cur}
        summary: Curso INAP [{cod} {cur}]({url}).
        ---

        ''').lstrip().format(cod=self.CODIGO, cur=self.CURSO, url=self.cfg.curso)+MD

        write(self.salida+self.CODIGO+".md", MD)


if __name__ == "__main__":
    c = CrawlInap("content/posts/ejercicios/")
    c.save()
