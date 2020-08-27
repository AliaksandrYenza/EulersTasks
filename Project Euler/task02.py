#https://projecteuler.net/problem=2


def fib():
    to = int(input('fib to'))
    arr = []
    arr.append(1)
    arr.append(2)
    #arr[0] = 1
    #arr[1] = 2
    for i in range(2,to):
        arr.append(arr[i-2] + arr[i-1])
    print(arr)


if __name__ == '__main__':
    fib()
