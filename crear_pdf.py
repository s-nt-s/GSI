#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re
import sys
from glob import iglob

from util import html_to_pdf

num = re.compile(r"_(\d+).html")

files = sys.argv[1:] or sorted(iglob("./**/*.html", recursive=True))
for h in files:
    fname = os.path.basename(h)
    m = num.search(fname)
    if m:
        codigo = fname[0].upper() + m.group(1)
    else:
        codigo = fname[0:2].upper()
    print("Convirtiendo " + fname + " a PDF ...", end="\r")
    html_to_pdf(h, codigo)
    print("Convirtiendo " + fname + " a PDF 100%")
