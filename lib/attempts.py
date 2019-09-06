class Attempts(object):
    def __init__(self, task, limit):
        self.current = 0
        self.limit = 5

        self.task = task

    def main(self):
        while self.current < self.limit:
            print('# {} attempts left'.format(self.limit - self.current))
            result = self.task.result
            if result:
                break
            self.current += 1
        return result
