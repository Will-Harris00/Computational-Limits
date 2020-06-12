import numpy.linalg


a = [[1, 1, 2], [0, 2, 2], [1, 0, 3]]
b = [0, 2, 1]
x = numpy.linalg.solve(a,b)


c = [[2, 0, 0], [0, 2, 0], [0, 0, 2]]
d = [0, 2, 1]
y = numpy.linalg.solve(c,d)

print(x)
print(numpy.allclose(numpy.dot(a, x), b))

print(y)
print(numpy.allclose(numpy.dot(c, y), d))
