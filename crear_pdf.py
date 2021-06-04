#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sys
from glob import iglob
from os.path import basename, isfile, dirname, abspath
from os import chdir

from core.util import html_to_pdf


abspath = abspath(__file__)
dname = dirname(abspath)
chdir(dname)

num = re.compile(r"_(\d+).html")


def get_codigo(file):
    if "temario" in file:
        return "GSI"
    fname = basename(file)
    m = num.search(fname)
    if m:
        codigo = fname[0].upper() + m.group(1)
    else:
        codigo = fname[0:2].upper()
    return codigo


files = sys.argv[1:]
if len(files)==0:
    for ht in iglob("./**/*.html", recursive=True):
        if "/_" not in ht:
            files.append(ht)
    for md in iglob("./**/*.md", recursive=True):
        if isfile(dirname(md)+"/print.css"):
            files.append(md)
    files=sorted(files)

for h in files:
    fname = basename(h)
    codigo = get_codigo(h)
    print("Convirtiendo " + fname + " a PDF ...", end="\r")
    html_to_pdf(h, codigo)
    print("Convirtiendo " + fname + " a PDF 100%")
