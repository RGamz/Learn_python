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
            return self.func(self.iterable[self.counter - 1])
        else:
            raise StopIteration


def mul2(x):
    return x * 20


a = [i for i in range(31)]

print(list(multifilter(a, mul2)))

