s1 = {'a', 'b', 'c'}
s2 = {'b', 'c', 'd'}

print(f'union: {s1.union(s2)}')
print(f'intersection: {s1.intersection(s2)}')
print(f'difference: {s1.difference(s2)}')
print(f'symethric difference: {s1.symmetric_difference(s2)}')
print(f'is subset: {s1.issubset({"a", "b", "c", "d"})}')
print(f'is superset: {s1.issuperset({"a", "b"})}')
