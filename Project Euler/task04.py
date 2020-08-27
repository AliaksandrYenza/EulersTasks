#https://projecteuler.net/problem=4

def poli(n):
    n = str(n)
    rev = n[::-1]
    return n == rev


def fn(n):
    arr = []
    max_p = 1
    for i in range(n,1,-1):
        for j in range(n,1,-1):
            max_p = i * j
            if poli(max_p):
                arr.append(max_p)
                print(f'i = {i} j = {j} num = {max_p}')
    return max(arr)


if __name__ == "__main__":
    n = int(input('Num from = '))
    n = fn(n)
    print(f'max {n}')


