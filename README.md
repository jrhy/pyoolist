# Object-Oriented Collection Wrappers in Python

```python
from flist import flist, fmap
```

Start with a regular old list:

```python
l = flist([1,2,3,4,5,6,7,8,9,10])
```

We can filter it:

```python
l.filter(lambda x: x % 3 == 0)   == [3, 6, 9]
```

Chain more stuff:

```python
(l
  .filter(lambda x: x % 3 == 0)  #  [3,   6,   9]
  .map(lambda x: x + 200)        #  [203, 206, 209]
  .size())                       == 3
```

See [flisttest.py](flisttest.py) for more examples.

```
l = [1, 2]
l.filter(lambda x: x % 2 == 0).size()      == 1
l.map(lambda x: x + 2)                     == [3, 4]

l = [[1, 2], [3, 4]]
l.flatten()                                == [1, 2, 3, 4]

flist([1,2]).flatmap(lambda x: [x, x])          == [1, 1, 2, 2]
flist([1,2]).reduce(lambda a, b: a + b, 0)      == 3
flist(['a','b']).reduce(lambda a, b: a + b, '') == ab

m = {'k2': 'v2', 'k1': 'v1'}
sorted(m.keys())                           == ['k1', 'k2']
sorted(m.values())                         == ['v1', 'v2']
sorted(m.items())                          == [('k1', 'v1'), ('k2', 'v2')]
sorted(m.map(lambda key, val: key + val))  == ['k1v1', 'k2v2']

list -> map() -> [(key,val)] -> tomap():
m.map(lambda key, val: (key, val)).tomap() == {'k2': 'v2', 'k1': 'v1'}

An flist should transform its mappable items to fmaps:
l = [{'id': 1, 'op': 'registration'}, {'id': 2, 'op': 'transfer'}]
type(l[0])                                 == <class 'flist.fmap'>
l.map(lambda e: sorted(e.map(lambda key, val: '%s=%s'%(key,val))))
 == [['id=1', 'op=registration'], ['id=2', 'op=transfer']]

pluck:
l.map(lambda x: {'id':x['id'], 'optype':x['op']})
 == [{'optype': 'registration', 'id': 1}, {'optype': 'transfer', 'id': 2}]
```
