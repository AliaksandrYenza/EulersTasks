#https://projecteuler.net/problem=3
import math

def factor():
    a = int(input("num: "))
    i = 2
    while i < a:
        if a % i == 0:
            print(i)
            a /= i
        else:
            i += 1
    print(a)


if __name__ == '__main__':
    factor()