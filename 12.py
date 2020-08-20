#arr = (int(i) for i in input().split())


string = input('Vvedite chisla razdelyaya ih probelami: ')
x = input('Vvedite chislo dlya poiska v predyduschei posledovatelnosti: ')
lst = (input().split())
res = [str(pos) for pos, num in enumerate(lst) if num == x]
print(''.join(res) if res else 'Отсутствует')
