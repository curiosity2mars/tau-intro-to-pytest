class Accumulator:

    def __init__(self) -> None:
        self._count = 0    # private var as it's started with _

    @property
    def count(self):
        return self._count

    def add(self, more=1):
        self._count += more