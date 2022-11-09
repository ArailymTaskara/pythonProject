def outer_func():
    def inner_func():
        print("Hello, World!")

    inner_func()


def reducer_func(el_prev, el):
    # el_prev — предшествующий элемент
    # el — текущий элемент
    return el_prev + el

    # python 2


reduce(reducer_func, [1, 2, 3])  # 6

# python 3
from functools import reduce

reduce(reducer_func, [1, 2, 3])  # 6