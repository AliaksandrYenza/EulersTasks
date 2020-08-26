# https://projecteuler.net/problem=1

class Z_One:

    def starter(self):
        s = self.findMultiples(self.inputValue(), self.nums())
        print(s)
        # summ()

    def nums(self):
        return input(('wat')).split()

    def inputValue(self):
        return [i for i in range(int(input('check to value = ')))]

    def findMultiples(self, arr, num):
        setsum = set()
        print(f"arr = {arr} type = {type(arr)}")
        print(f"num = {num} type = {type(num)}")

        for i in arr:
            for n in num:
                if (int(i) % int(n)) == 0:
                    setsum.add(i)
        print(setsum)
        return sum(setsum)


if __name__ == '__main__':
    z = Z_One()
    z.starter()
