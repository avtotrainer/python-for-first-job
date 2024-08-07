"""
ძირითადი მონაცემთა სტრუქტურები
"""
# 1. როგორ იქმნება / იცვლება / იშლება
# 2. ცვლადი / არაცვლადი ობიექტები
# 3. საბაზო სტურქტურების ძირიდადი მეთოდები
a = []
a = list()
a = [1] * 10
a = [1, 2, 3] + [3, 4, 5]
a = [*a]
a.append(a)
a.pop()
a.extend(a)
# ...

b = (1, 2, a)
b = tuple([1, 2])
b = b[:]
b, _ = b
# ...

c = {1, 2}
d = set([1, 2])
c.add(3)
c.remove(3)
c.update({None, })
_ = c - d
_ = c | d
_ = c & d
_ = frozenset(c)
# ...

d = dict(none123=None)
d = {None: None, **d}
d[1] = 1
d = d | {2: 2}
_ = d.setdefault(3, 3)
_ = d.get(4)
d.pop(1)
d.items()
d.keys()
d.values()
# ...
