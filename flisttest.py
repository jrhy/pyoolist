from flist import flist, fmap

def test(actual, expected):
	if not actual == expected:
		raise ValueError("test failed; actual:%s, expected:%s" % (actual, expected))

l = flist([1,2])
test(l.filter(lambda x: x % 2 == 0).size(), 1)
test(l.map(lambda x: x + 2)               , [3, 4])

l = flist([[1,2],[3,4]])
test(l.flatten(), [1,2,3,4])

test(flist([1,2]).flatmap(lambda x: [x, x]), [1, 1, 2, 2])

test(flist([1,2]).reduce(lambda a, b: a + b, 0), 3)
test(flist(["1","2"]).reduce(lambda a, b: a + b, ""), "12")

m = fmap({'a':'aval','b':'bval'})
test(sorted(m.keys())                             , ['a','b'])
test(sorted(m.values())                           , ['aval','bval'])
test(sorted(m.items())                            , [('a','aval'),('b','bval')])
test(sorted(m.map(lambda key, value: key + value)), ['aaval','bbval'])
test(m.map(lambda key, value: (key, value)).tomap(), m)

l = flist([{'id':1, 'op':'registration'},
     {'id':2, 'op':'transfer'}])
# an flist should transform its mappable items to fmaps
test(type(l[0]), fmap)
test(l.map(lambda e: sorted(e.map(lambda key, val: '%s=%s'%(key,val)))), [['id=1','op=registration'],['id=2','op=transfer']])
# pluck syntax
test(l.map(lambda x: {'id':x['id'], 'optype':x['op']}), 
    [{'id':1, 'optype':'registration'}, {'id':2, 'optype':'transfer'}])

