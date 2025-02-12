import numpy as np

# Z = np.arange(9).reshape(3,3)
# print(Z)

# Z = np.arange(4).reshape(2,2)
# print(Z)

# Z = np.arange(1,50)
# print(Z)


# nz = np.nonzero([1, 2,0,0,4,0]) #0이 아닌 값들의 인덱스를 반환
# print(nz)

# Z = np.eye(3)
# print(Z) 

# Z = np.random.random((3, 3, 3))
# print(Z)


# Z = np.random.random((10,10))
# m, M = Z.min(), Z.max()
# print(Z)
# print()
# print(m, M)

# Z = np.ones((10, 10))
# Z[1:-1, 1:-1] = 0
# print(Z)

# Z = np.ones((5, 5))
# # Z = np.pad(Z, pad_width=1, mode='constant', constant_values=0)
# print(Z)
# print()
# Z[:, [0, -1]] = 0
# Z[[0,-1], : ] = 0
# print(Z)

# Z = np.zeros((8, 8), dtype=int)
# Z[::2, ::2] = 1
# Z[ 1::2,1::2] = 1
# print(Z)

# print(np.unravel_index(99, (6,7,8)))

# Z = np.ones((5, 3),dtype=int) @ np.ones((3, 2),dtype=int)
# print(Z)

# Z = np.arange(12)
# Z[ (3 < Z) & (Z < 8)] = -1
# print(Z)

# Z = np.linspace(0,1,11, endpoint=False)[1:]
# print(Z)

# Z = np.random.random(10)
# print(Z)
# Z.sort()
# print(Z)

# A = np.random.randint(0, 2, 5)
# B = np.random.randint(0, 2, 5)
# print(A)
# print(B)
# equal = np.allclose(A,B)
# print(equal)

# equal = np.array_equal(A,B)
# print(equal)

A = np.arange(25).reshape(5, 5)
A[[0, 1],:] = A[[1, 0],:]
print(A)

