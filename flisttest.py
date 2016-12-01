from flist import flist, fmap

def test(expr, expected):
    actual = eval(expr)
    if not actual == expected:
        print expr
        raise ValueError("test failed; actual:%s, expected:%s" % (actual, expected))
    print "%s == %s" % (expr, expected)

l = flist([1,2])
print "l = %s" % l
test("l.filter(lambda x: x % 2 == 0).size()     ", 1)
test("l.map(lambda x: x + 2)                    ", [3, 4])
print ""

l = flist([[1,2],[3,4]])
print "l = %s" % l
test("l.flatten()                               ", [1,2,3,4])
print ""

test("flist([1,2]).flatmap(lambda x: [x, x])         ", [1, 1, 2, 2])
test("flist([1,2]).reduce(lambda a, b: a + b, 0)     ", 3)
test("flist(['a','b']).reduce(lambda a, b: a + b, '')", "ab")
print ""

m = fmap({'k1':'v1','k2':'v2'})
print "m = %s" % m
test("sorted(m.keys())                          ", ['k1','k2'])
test("sorted(m.values())                        ", ['v1','v2'])
test("sorted(m.items())                         ", [('k1','v1'),('k2','v2')])
test("sorted(m.map(lambda key, val: key + val)) ", ['k1v1','k2v2'])
print ""

print "list -> map() -> [(key,val)] -> tomap():"
test("m.map(lambda key, val: (key, val)).tomap()", m)
print ""

print "An flist should transform its mappable items to fmaps:"
l = flist([
      {'id':1, 'op':'registration'},
      {'id':2, 'op':'transfer'}])
print "l = %s" % l
test("type(l[0])                                ", fmap)
test("l.map(lambda e: sorted(e.map(lambda key, val: '%s=%s'%(key,val))))\n",
        [['id=1','op=registration'],['id=2','op=transfer']])
print ""

print "pluck:"
test("l.map(lambda x: {'id':x['id'], 'optype':x['op']})\n", 
    [{'id':1, 'optype':'registration'}, {'id':2, 'optype':'transfer'}])

