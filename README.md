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

