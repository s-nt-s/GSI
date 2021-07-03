#!/usr/bin/python3
import re

import bs4

re_sp = re.compile(r"\s+")

sub_plain = tuple((
    ("á", "a"),
    ("é", "e"),
    ("í", "i"),
    ("ó", "o"),
    ("ú", "u"),
))


def wc(html):
    html = bs4.BeautifulSoup(html, "lxml")
    text = html.get_text()
    text = [l.strip() for l in text.split("\n") if len(l.strip()) > 0]
    lines = len(text)
    text = "\n".join(text)
    words = len(text.split())
    letters = len(text)
    return lines, words, letters


def plain(s):
    s = s.lower()
    for a, b in sub_plain:
        s = s.replace(a, b)
    s = re_sp.sub("", s)
    return s

def millar(value):
    value = "{:,.0f}".format(value).replace(",", ".")
    return value

JINJA_FILTERS = {
    'wc': wc,
    'plain': plain,
    'millar': millar
}
