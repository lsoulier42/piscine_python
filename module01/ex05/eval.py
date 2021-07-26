class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        if len(words) == len(coefs):
            mul = lambda l: (x * len(y) for x, y in l)
            print(sum(mul(zip(coefs, words))))
        else:
            print(-1)

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if len(words) == len(coefs):
            mul = lambda coefs, words: (coefs[count] * len(word) for count, word in enumerate(words))
            print(sum(mul(coefs, words)))
        else:
            print(-1)


if __name__ == "__main__":
    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    Evaluator.zip_evaluate(coefs, words)
    Evaluator.enumerate_evaluate(coefs, words)
    words = ["Le", "Lorem", "Ipsum", "n'", "est", "pas", "simple"]
    coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
    Evaluator.zip_evaluate(coefs, words)
    Evaluator.enumerate_evaluate(coefs, words)
