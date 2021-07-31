def ft_map(function_to_apply, list_of_inputs):
    return (function_to_apply(i) for i in list_of_inputs)


if __name__ == "__main__":
    my_list = [1, 2]
    print(list(ft_map(str, my_list)))
