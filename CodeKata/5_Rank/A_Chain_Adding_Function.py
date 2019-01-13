class customFn(int):
    def __call__(self, int):
        return customFn(self + int)


def add(intValue):
    return customFn(intValue)


print(add(1)(2))