from lib.secret import Secret
from lib.guess import Guess
from lib.diffs import Diff, VerboseDiff
from lib.attempts import Attempts
from lib.farewell import Farewell


if __name__ == '__main__':
    min, max = 1, 10
    attempts_limit = 5

    secret = Secret(min=min, max=max)

    Farewell(
        Attempts(
            VerboseDiff(
                Diff(
                    Guess(min=min, max=max),
                    secret
                )
            ), attempts_limit
        ), secret
    ).say()
