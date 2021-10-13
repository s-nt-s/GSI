import functools
import os
import time
from munch import Munch

from .filemanager import FM

class Cache:
    def __init__(self, file, *args, reload=False, maxOld=30, **kargs):
        self.file = file
        self.data = {}
        self.func = None
        self.reload = reload
        self.maxOld = maxOld
        if maxOld is not None:
            self.maxOld = time.time() - (maxOld * 86400)

    def parse_file_name(self, *args, **kargv):
        if args or kargv:
            return self.file.format(*args, **kargv)
        return self.file

    def read(self, file, *args, **kargs):
        return FM.load(file)

    def save(self, file, data, *args, **kargs):
        FM.dump(file, data)

    def tooOld(self, fl):
        if not os.path.isfile(fl):
            return True
        if self.maxOld is None:
            return False
        if os.stat(fl).st_mtime < self.maxOld:
            return True
        return False

    def callCache(self, slf, *args, **kargs):
        fl = self.parse_file_name(*args, **kargs)
        if not self.reload and not self.isReload(slf, *args, **kargs):
            data = self.read(fl, *args, **kargs)
            return data
        data = self.func(slf, *args, **kargs)
        self.save(fl, data, *args, **kargs)
        return data

    def isReload(self, slf, *args, **kargs):
        reload = getattr(slf, "reload", False)
        if reload == True:
            return True
        fl = self.parse_file_name(*args, **kargs)
        if isinstance(reload, (list, tuple)):
            if self.file in reload:
                return True
            if fl in reload:
                return True
        if self.tooOld(fl):
            return True
        return False

    def __call__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        return lambda *args, **kargs: self.callCache(*args, **kargs)


class MunchCache(Cache):
    def read(self, *args, **kargs):
        data = super().read(*args, **kargs)
        return Munch.fromDict(data)
