def ft_reduce(fun, seq):
    return list(ft_reduce_gen(fun, seq))[-1]

def ft_reduce_gen(fun, seq):
    if len(seq) >= 2:
        result = seq[0]
        for i in range(1, len(seq)):
            result = fun(result, seq[i])
            yield result

if __name__ == "__main__":
    print(ft_reduce((lambda a, b: a + b), [1, 2, 3]))