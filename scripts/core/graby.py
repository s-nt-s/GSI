import requests
from bs4 import BeautifulSoup
import sys
from subprocess import check_output, STDOUT
from myplugins.core.decorators import MunchCache, Cache
import os
import json

GRABY_ENDPOINT = os.environ['GRABY_ENDPOINT']
GRABY_LOCAL = "graby/graby.php"

class Graby:
    def __init__(self, endpoint=os.environ['GRABY_ENDPOINT'], local=GRABY_LOCAL):
        self.endpoint = endpoint
        self.local = local

    def get_local(self, *args, **kargv):
        js = check_output([self.local] + list(args), stderr=STDOUT).decode(sys.stdout.encoding)
        js = json.loads(js)
        return js

    def get_endpoint(self, url, *args, **kargv):
        r = requests.get(self.endpoint, params={"url": url})
        if not r.text.strip():
            return None
        js = r.json()
        return r.json()

    def _get(self, *args, **kargv):
        return sef.get_endpoint(*args, **kargv)

    @Cache("graby/{}data.json")
    def get(self, *args, **kargv):
        return sef._get(*args, **kargv)

    def get_soup(self, url):
        graby = self.get(url)
        html = graby['html']
        soup = BeautifulSoup(html, "html.parser")
        return soup
