
class multifilter:

    def __init__(self, iterable, func):
        self.iterable = iterable
        self.counter = 0
        self.func = func

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < len(self.iterable):
            self.counter += 1
            if self.func(self.iterable[self.counter - 1]) is True:
                return self.iterable[self.counter - 1]
            else:
                return self.__next__()
        else:
            raise StopIteration


def mul2(x):
    return x % 2 == 0



a = [i for i in range(31)]

print(list(multifilter(a, mul2)))

