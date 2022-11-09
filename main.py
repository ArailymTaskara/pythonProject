numbers = [1, 2, 3, 4, 5]
squared = map(lambda num: num ** 2, numbers)
print(list(squared))
#[1, 4, 9, 16, 25]

str_nums = ["4", "8", "6", "5", "3", "2", "8", "9", "2", "5"]
int_nums = map(int, str_nums)
print(int_nums)
print(list(int_nums))