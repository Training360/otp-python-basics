import numpy as np

a = np.zeros(100)
print(a)
print(type(a))
print(type(a[0]))

b = np.ones(100)
print(b)

c = np.empty(100)
print(c)

d = np.linspace(0, 100, 5)
print(d)

e = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(e.shape)

f = np.random.randint(1, 10, size=10)
print(f)

g = np.array([1, 2, 3, 4, 5])
h = np.array([6, 7, 8, 9, 10])
print(g > 3)
print(g * 3)
print(g + h)
print(g @ h)  # skaláris szorzat

i = np.arange(10)
print(i)
j = np.where(i > 5, i, 0)
print(j)

i.sort()
print(i)

print(np.max(i))
print(np.min(i))
print(np.sum(i))
print(np.mean(i))  # átlag
print(np.std(i))  # szórás
print(np.var(i))  # szórásnégyzet
print(np.argmin(i))  # min index
print(np.argmax(i))  # max index
