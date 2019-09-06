import copy


class Diff(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def result(self):
        return self.a.value - self.b.value


class VerboseDiff(object):
    def __init__(self, diff):
        self.diff = diff

    @property
    def result(self):
        # NOTE
        # Here we use copy.deepcopy() to access guess.value only once since we obtain it via input() getter
        diff = copy.deepcopy(self.diff.result)

        if diff == 0:
            result, verbose = True, 'Equals!'
        else:
            if diff > 0:
                result, verbose = False, 'Greater'
            else:
                result, verbose = False, 'Lower'
        print(verbose)
        return result
