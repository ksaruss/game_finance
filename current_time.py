class CurrentTime:
    def __init__(self):
        self._year = 0
        self._month = 0
        self._week = 1
        self._day = 0

    def step(self) -> None:
        if self._week + 1 == 5:
            self._week = 1
            self._month += 1
        else:
            self._week += 1
        if self._month == 13:
            self._month = 0
            self._year += 1

    def get_current_data(self) -> dict:
        return {'year': self._year, 'month': self._month, 'week': self._week}

    def past_cycles(self, data: tuple) -> int:
        return (self._year - data[0]) * 48 + (self._month - data[1]) * 4 + (self._week - data[2])

