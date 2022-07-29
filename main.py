
class multifilter:

    def __init__(self, iterable, *funcs):
        self.iterable = iterable
        self.counter = 0
        self.funcs = funcs
        self.pos = 0
        self.neg = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < len(self.iterable):
            self.counter += 1
            for func in self.funcs:
                if func(self.iterable[self.counter - 1]) is True:
                    self.pos += 1
                else:
                    self.neg += 1
            if self.pos >= self.neg:
                self.pos = 0
                self.neg = 0
                return self.iterable[self.counter - 1]
            else:
                self.pos = 0
                self.neg = 0
                return self.__next__()

        else:
            raise StopIteration


def mul2(x):
    return x % 2 == 0


def mul3(x):
    return x % 3 == 0


def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)]

print(list(multifilter(a, mul2, mul3, mul5)))

