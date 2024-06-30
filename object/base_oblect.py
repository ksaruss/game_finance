from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from world import World


class BaseObject:
    _count_id = 0

    def __init__(self, world: 'World', name: str):
        self._id = self._get_new_id()
        self._world = world
        self._name = name
        self._type = 'baseObject'

    @classmethod
    def _get_new_id(cls) -> int:
        BaseObject._count_id += 1
        return BaseObject._count_id

    def get_id(self) -> int:
        return self._id

    def get_world(self) -> 'World':
        return self._world

    def get_type(self) -> str:
        return self._type
