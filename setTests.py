from set import *
s = PowerSet()
s2 = PowerSet()


s.put(1)
s.put(3.14)
s.put(2)
s.put(4)
# s.put(8)
# s.put("result")


# s.remove(1)
s2.put(1)
s2.put(3.14)
s2.put(4)
# s2.put(6)
# # s2.put(10)
# s.remove(21)
# s.remove(21)

print("s", s.slots)
print("s2", s2.slots)
d = s.issubset(s2)
print("issubset", d)
a = s.intersection(s2)
b = s.union(s2)
c = s.difference(s2)

print("inter", a.slots)
print("union", b.slots)
print("diffence", c.slots)


