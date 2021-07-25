from matrix import Matrix

if __name__ == "__main__":
    m1 = Matrix([[0.0, 1.0, 2.0, 3.0], [0.0, 2.0, 4.0, 6.0]])
    m2 = Matrix([[0.0, 1.0, 2.0, 3.0], [0.0, 2.0, 4.0, 6.0]])

    print(m1)
    print(m2)
    print(m1 + m2)
    print(m1 - m2)
    print(m1 * 3.0)
    print(m1 * m2)
    print(m1 / 2.0)

