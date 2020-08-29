# https://projecteuler.net/problem=5
import math
from functools import reduce


def take_d():
    n = int(input("Input value: "))
    return n


def simples_v(arr, n):
    if n == 1:
        return arr
    if n < 1 or not  isinstance(n, int): raise  TypeError
    i=2
    while n != 1:
        if n % i ==0:
            n = n// i
            if arr[-1] != i:
                arr.append(i)
            continue
        i +=1
    print(f' arr from s_v = {arr}')
    return arr


def get_d(arr):
    r = reduce(lambda x, y: x * y, arr)
    print(f'from get_d {r}')
    return r


def check_to_d(value, arr, n):
    for num in range(1,n+1):
        if value%num == 0:
            print(f'{value} / {num } = {value/num} COOL')
        else:
            print(f'{value} / {num} = {value / num} BAD')

            arr = simples_v(arr,num)
            value = get_d(arr)
            return value, arr, n
    print("return check_t_d")
    return value,arr,0



if __name__ == "__main__":
    n = 30          #n = take_d()
    arr = [1]
    arr = simples_v(arr, n)
    v = get_d(arr)
    while True:


        v, arr, n = check_to_d(v,arr,n)
        if n == 0:
            break
