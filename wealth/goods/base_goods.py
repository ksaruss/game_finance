class BaseGoods:
    def __init__(self):
        self._name = 'baseGoods'
        self._quantity = 0
        self._cost = 0

    def get_name(self) -> str:
        return self._name

    