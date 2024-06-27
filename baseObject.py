class BaseObject:
    _count_id = 0

    def __init__(self):
        self._id = self._get_new_id()

    def get_id(self):
        return self._id

    @classmethod
    def _get_new_id(cls):
        cls._count_id += 1
        return cls._count_id


class Country(BaseObject):
    def __init__(self, name: str):
        super().__init__()
        self._name = name

    def get_name(self):
        return self._name
