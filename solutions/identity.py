import numpy
numpy.set_printoptions(legacy='1.13')

n,m = map(int, input("Please enter n and m: ").split())

print(numpy.eye(n,m))