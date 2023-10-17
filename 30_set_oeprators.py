s1 = {'a', 'b', 'c'}
s2 = {'b', 'c', 'd'}

# print(f'union: {s1.union(s2)}')
print(f'union: {s1 | s2}')
# print(f'intersection: {s1.intersection(s2)}')
print(f'intersetion: {s1 & s2}')
# print(f'difference: {s1.difference(s2)}')
print(f'diference: {s1 - s2}')
# print(f'symethric difference: {s1.symmetric_difference(s2)}')
print(f'symethric difference: {s1 ^ s2}')
# print(f'is subset: {s1.issubset({"a", "b", "c", "d"})}')
print(f'is subset {s1 <= {"a", "b", "c", "d"} }')
# print(f'is superset: {s1.issuperset({"a", "b"})}')
print(f'is superset: {s1 >= {"a", "b"} }')

print(s1 | ('e', 'f', 'g'))
print(s1.union(('e', 'f', 'g')))
