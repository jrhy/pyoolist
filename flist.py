
class fmap(dict):
    pass
fmap.keys   = lambda self:       flist(dict.keys(self))
fmap.values = lambda self:       flist(dict.values(self))
fmap.items  = lambda self:       flist(dict.items(self))
fmap.size   = lambda self:       len(self)
fmap.map    = lambda self, func: flist(dict.items(self)).map(
                                    lambda v: func(v[0], v[1]))

class flist(list):
    pass

    def __getitem__(self, x):
        return fmapify(list.__getitem__(self, x))

    def map(self, func):
        return flist(map(lambda x: func(fmapify(x)), self))
    def flatmap(self, func):
        return self.map(func).flatten()
    def flatten(self):
        res = []
        for x in self: 
            if type(x) in (list, flist):
                for y in x:
                    res.append(y)
            else:
                res.append(x)
        return flist(res)
    def filter(self, func):
        return flist(filter(func, self))
    def reduce(self, func, startval):
        cur = startval
        for x in self:
            cur = func(cur, x)
        return cur
    def size(self):
        return len(self)
    def tomap(self):
        return fmap(self)

def fmapify(m):
    if type(m) == dict:
        return fmap(m)
    else:
        return m
