def ft_filter(function_to_apply, iterable):
    return (i for i in iterable if function_to_apply(i))

if __name__ == "__main__":
    myList = [1, 2, 3]
    fct = lambda a: (a % 2 == 0)
    print(list(ft_filter(fct, myList)))