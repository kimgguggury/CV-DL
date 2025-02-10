import numpy as np

# a = np.arange(12).reshape(3, 4)
# print(a)

# print(a.shape)

# print(a.dtype)

# print(a.size)

# a = np.array([2, 3, 4])
# print(a)
# print(a.dtype)

# b = np.array([1.2, 3.5, 5.1])
# print(b)
# print(b.dtype)

# a = np.zeros((3, 4), dtype = np.int64)
# print(a)

# a = np.ones((2, 3, 4), dtype = np.int64)
# print(a)

# a = np.empty((2, 3))
# print(a)

# a = np.arange(10, 30, 5)
# print(a)

# a = np.arange(0, 2, 0.3)
# print(a)

# a = np.linspace(0, 99, 100)
# print(a)

# a = np.array([20, 30, 40, 50])
# b = np.arange(4)

# print(a)
# print(b)

# c = a - b
# print(c)

# b = b ** 2
# print(b)

# print(a*10)

# print(a<35)

# A = np.array([[1, 1],
#               [0, 1]])
# B = np.array([[2, 0],
#               [3, 4]])

# print(A)
# print(B)

# print(A * B)
# print(A @ B)

# a = np.ones(3, dtype=np.int32)
# b = np.linspace(0, np.pi, 3)

# print(a)
# print(b)
# print(a.dtype)
# print(b.dtype)

# c = a + b
# print(c)
# print(c.dtype)

# a = np.arange(8).reshape(2, 4)**2
# print(a)

# print(a.sum())

# print(a.min())
# print(a.max())

# print(a.argmax()) #최대값의 인덱스

# print(a.cumsum())

# b = np.arange(12).reshape(3, 4)
# print(b)

# print(b.sum(axis=0))
# print(b.sum(axis=1))

# a = np.arange(8)**3
# print(a)
# i = np.array([1, 1, 3, 5])
# print(a[i])

a = np.arange(12).reshape(3, 4)
print(a)

b = a > 4
print(b)

print(a[b])
print(a[b].shape)

print(a)
a[b] = a