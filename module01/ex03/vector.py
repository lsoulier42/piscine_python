class Vector:
    def __init__(self, arg=None):
        if type(arg) == list and all(type(e) == float for e in arg):
            self.values = arg
        elif type(arg) == int:
            self.values = [float(i) for i in range(0, arg + 1)]
        elif type(arg) == tuple:
            self.values = [float(i) for i in range(int(arg[0]), int(arg[1]))]
        else:
            self.values = []
        self.size = len(self.values)

    def __add__(self, a):
        new_vector = Vector()
        if type(a) == Vector and a.size == self.size:
            for i in range(0, self.size):
                new_vector.values.append(self.values[i] + a.values[i])
        elif type(a) == int or type(a) == float:
            for i in range(0, self.size):
                new_vector.values.append(self.values[i] + float(a))
        new_vector.size = len(new_vector.values)
        return new_vector

    def __radd__(self, a):
        return self.__add__(a)

    def __sub__(self, a):
        return self.__add__(a * -1)

    def __rsub__(self, a):
        return self.__sub__(a)

    def __truediv__(self, a):
        new_vector = Vector()
        if (type(a) == int or type(a) == float) and a != 0:
            for i in range(0, self.size):
                new_vector.values.append(self.values[i] / a)
        new_vector.size = len(new_vector.values)
        return new_vector

    def __rtruediv__(self, a):
        return self.__truediv__(a)

    def __mul__(self, a):
        if type(a) == int or type(a) == float:
            new_vector = Vector()
            for i in range(0, self.size):
                new_vector.values.append(self.values[i] * a)
            new_vector.size = len(new_vector.values)
            return new_vector
        elif type(a) == Vector and a.size == self.size:
            return sum([(a.values[i] * self.values[i]) for i in range(0, self.size)])

    def __rmul__(self, a):
        return self.__rmul__(a)

    def __str__(self):
        return "(Vector [{}])".format(", ".join(map(str, self.values)))

    def __repr__(self):
        return "Vector(values={}, size={})".format(", ".join((map(str, self.values))), self.size)
