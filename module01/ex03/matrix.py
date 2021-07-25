from vector import Vector

class Matrix:
    def __init__(self, *data):
        if len(data) == 1:
            if type(data[0]) == list:
                self.data = data[0]
                self.shape = (len(self.data), len(self.data[0]))
            elif type(data[0]) == tuple:
                self.shape = data[0]
                self.data = [[0.0 for _ in range(0, self.shape[1])] for _ in range(0, self.shape[0])]
        elif len(data) == 2:
            self.data = data[0]
            self.shape = data[1]
        else:
            self.data = [[]]
            self.shape = (0, 0)

    def __add__(self, a):
        new_matrix = Matrix()
        if type(a) == Matrix and self.shape == a.shape:
            new_matrix.data = [[self.data[i][j] + a.data[i][j] for j in range(0, self.shape[1])] for i in range(0, self.shape[0])]
            new_matrix.shape = self.shape
        return new_matrix

    def __radd__(self, a):
        return self.__add__(a)

    def __sub__(self, a):
        return self.__add__(a * -1)

    def __rsub__(self, a):
        return self.__sub__(a)

    def __truediv__(self, a):
        new_matrix = Matrix()
        if (type(a) == int or type(a) == float) and a != 0:
            new_matrix.data = [[(self.data[i][j] / float(a)) for j in range(0, self.shape[1])] for i in range(0, self.shape[0])]
            new_matrix.shape = self.shape
        return new_matrix

    def __rtruediv__(self, a):
        return self.__truediv__(a)

    def __mul__(self, a):
        new_matrix = Matrix()
        if type(a) == int or type(a) == float:
            new_matrix.data = [[(self.data[i][j] * float(a)) for j in range(0, self.shape[1])] for i in range(0, self.shape[0])]
        elif type(a) == Vector and a.size == self.shape[1]:
            new_vector = Vector()
            new_vector.values = [self.data[i] * a for i in range(0, self.shape[0])]
            new_vector.size = self.shape[0]
            return new_vector
        elif type(a) == Matrix and self.shape == a.shape:
            new_matrix.data = [[self.data[i][j] * a.data[i][j] for j in range(0, self.shape[1])] for i in range(0, self.shape[0])]
        new_matrix.shape = self.shape
        return new_matrix

    def __rmul__(self, a):
        return self.__mul__(a)

    def __str__(self):
        txt = "(Matrix ["
        for i in range(0, self.shape[0]):
            txt += "[{}]".format(", ".join(map(str, self.data[i])))
            if i != self.shape[0] - 1:
                txt += ", "
        txt += "])"
        return txt

    def __repr__(self):
        txt = "(Matrix (data=["
        for i in range(0, self.shape[0]):
            txt += "[{}]".format(", ".join(map(str, self.data[i])))
            if i != self.shape[0] - 1:
                txt += ", "
        txt += "], shape=({}, {}))".format(self.shape[0], self.shape[1])
        return txt
