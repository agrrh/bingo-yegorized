class Guess(object):
    def __init__(self, min=1, max=10):
        print('Enter integer from {} to {}'.format(min, max))

    @property
    def value(self):
        v = None
        while not v:
            try:
                v = int(input('--> '))
            except Exception:
                v = None
        return v
