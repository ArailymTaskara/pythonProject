#Вычисление суммы всех элементов списка при помощи reduce:
from functools import reduce
items = [10, 20, 30, 40, 50]
sum_all = reduce(lambda x,y: x + y, items)
print(sum_all)