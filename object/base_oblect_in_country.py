from object.base_oblect import BaseObject

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from world import World
    from object.country import Country


class BaseObjectInCountry(BaseObject):
    def __init__(self, world: 'World', country: 'Country', name: str):
        super().__init__(world=world, name=name)
        self._country = country
        self._type = 'baseObjectInCountry'

    def get_country(self) -> 'Country':
        return self._country





