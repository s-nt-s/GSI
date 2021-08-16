import re
import time
from urllib.parse import urljoin

import bs4
import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

re_sp = re.compile(r"\s+")

default_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0',
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",
    "Expires": "Thu, 01 Jan 1970 00:00:00 GMT",
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}


def buildSoup(root, source):
    soup = bs4.BeautifulSoup(source, "lxml")
    for n in soup.findAll(["img", "form", "a", "iframe", "frame", "link", "script"]):
        attr = "href" if n.name in ("a", "link") else "src"
        if n.name == "form":
            attr = "action"
        ori = str(attr)
        for attr in (ori, "data-"+ori):
            val = n.attrs.get(attr)
            if val and not (val.startswith("#") or val.startswith("javascript:")):
                val = urljoin(root, val)
                n.attrs[attr] = val
    return soup


class Web:
    def __init__(self, refer=None, verify=True):
        self.s = requests.Session()
        self.s.headers = default_headers
        self.response = None
        self.soup = None
        self.form = None
        self.refer = refer
        self.verify = verify

    def get(self, url, **kargv):
        if self.refer:
            self.s.headers.update({'referer': self.refer})
        if kargv:
            self.response = self.s.post(url, data=kargv, verify=self.verify)
        else:
            self.response = self.s.get(url, verify=self.verify)
        if url.endswith(".xsd"):
            return self.response
        self.refer = self.response.url
        self.soup = bs4.BeautifulSoup(self.response.content, "lxml")
        for n in self.soup.findAll(["img", "form", "a", "iframe", "frame", "link", "script"]):
            attr = "href" if n.name in ("a", "link") else "src"
            if n.name == "form":
                attr = "action"
            val = n.attrs.get(attr)
            if val and not (val.startswith("#") or val.startswith("javascript:")):
                val = urljoin(url, val)
                n.attrs[attr] = val
        return self.soup

    def prepare_submit(self, slc, silent_in_fail=False, **kargv):
        data = {}
        self.form = self.soup.select_one(slc)
        if silent_in_fail and self.form is None:
            return None, None
        for i in self.form.select("input[name]"):
            name = i.attrs["name"]
            data[name] = i.attrs.get("value")
        for i in self.form.select("select[name]"):
            name = i.attrs["name"]
            slc = i.select_one("option[selected]")
            slc = slc.attrs.get("value") if slc else None
            data[name] = slc
        data = {**data, **kargv}
        action = self.form.attrs.get("action")
        action = action.rstrip() if action else None
        if action is None:
            action = self.response.url
        return action, data

    def submit(self, slc, silent_in_fail=False, **kargv):
        action, data = self.prepare_submit(
            slc, silent_in_fail=silent_in_fail, **kargv)
        if silent_in_fail and not action:
            return None
        return self.get(action, **data)

    def val(self, slc):
        n = self.soup.select_one(slc)
        if n is None:
            return None
        v = n.attrs.get("value", n.get_text())
        v = v.strip()
        return v if v else None


default_profile = {
    "browser.tabs.drawInTitlebar": True,
    "browser.uidensity": 1,
}


class FF:
    def __init__(self, visible=False, wait=60):
        self._driver = None
        self.visible = visible
        self._wait = wait

    @property
    def driver(self):
        if self._driver is None:
            options = Options()
            options.headless = not self.visible
            profile = webdriver.FirefoxProfile()
            for k, v in default_profile.items():
                profile.set_preference(k, v)
                profile.DEFAULT_PREFERENCES['frozen'][k] = v
            profile.update_preferences()
            self._driver = webdriver.Firefox(
                options=options, firefox_profile=profile)
            self._driver.maximize_window()
            self._driver.implicitly_wait(5)
        return self._driver

    def close(self):
        if self._driver:
            self._driver.close()
            self._driver = None

    def reintentar(self, intentos, sleep=1):
        if intentos > 50:
            return False, sleep
        if intentos % 3 == 0:
            sleep = int(sleep / 3)
            self.close()
        else:
            sleep = sleep*2
        if intentos > 20:
            time.sleep(10)
        time.sleep(2 * (int(intentos/10)+1))
        return True, sleep

    def get(self, url):
        self._soup = None
        self.driver.get(url)

    def get_soup(self):
        if self._driver is None:
            return None
        return buildSoup(self._driver.current_url, self._driver.page_source)

    @property
    def source(self):
        if self._driver is None:
            return None
        return self._driver.page_source

    def wait(self, id, seconds=None):
        if isinstance(id, (int, float)):
            time.sleep(id)
            return
        my_by = By.ID
        seconds = seconds or self._wait
        if id.startswith("//"):
            my_by = By.XPATH
        wait = WebDriverWait(self._driver, seconds)
        wait.until(ec.visibility_of_element_located((my_by, id)))
        if id.startswith("//"):
            return self._driver.find_element_by_xpath(id)
        return self._driver.find_element_by_id(id)


    def val(self, id, val=None):
        if self._driver is None:
            return None
        n = self.wait(id)
        if val is not None:
            n.clear()
            n.send_keys(val)
        return n.text

    def click(self, id):
        if self._driver is None:
            return None
        n = self.wait(id)
        n.click()

    def get_session(self):
        if self._driver is None:
            return None
        s = requests.Session()
        for cookie in self._driver.get_cookies():
            s.cookies.set(cookie['name'], cookie['value'])
        #h = self._driver.requests[-1]
        #s.headers = h.headers
        return s

    def pass_cookies(self, session=None):
        if session is None:
            session = requests.Session()
        for cookie in self._driver.get_cookies():
            session.cookies.set(cookie['name'], cookie['value'])
        return session


def get_session(url):
    f = FF()
    f.get(url)
    w = Web()
    w.s = f.get_session()
    w.get(url)
    f.close()
    return w
