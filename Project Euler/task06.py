#https://projecteuler.net/problem=6
from functools import reduce
from math import sqrt


def a():
    a = reduce(lambda x,y: x+y, ([n ** 2 for n in range(101)]))
    print(a)
    b = (reduce(lambda x,y: x+y, ([n  for n in range(101)]))) **2
    print(b)
    print(b-a)



if __name__ == '__main__':
    a()