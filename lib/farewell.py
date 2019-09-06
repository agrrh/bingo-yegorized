class Farewell(object):
    def __init__(self, attempts, secret):
        self.secret = secret

        self.result = attempts.main()

    def say(self):
        if self.result:
            print('Congratulations, you won!')
        else:
            print('Sadly, you failed to guess a number ...')
        print('Secret number was: {}'.format(self.secret.value))
