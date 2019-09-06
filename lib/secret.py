import time
import random


class Secret(object):
    def __init__(self, min=1, max=10):
        random.seed(time.time())
        self.value = random.randint(min, max)
