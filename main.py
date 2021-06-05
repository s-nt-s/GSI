#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from core.temario import CrawlTemario

from os.path import basename, isfile, dirname, abspath
from os import chdir

abspath = abspath(__file__)
dname = dirname(abspath)
chdir(dname)

c = CrawlTemario()
c.save(c.anx_libre)
c.save(c.anx_interna)
