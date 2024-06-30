from object.base_oblect_in_country import BaseObjectInCountry

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from world import World
    from object.country import Country


class BaseCompany(BaseObjectInCountry):
    def __init__(self, world: 'World', country: 'Country', name: str):
        super().__init__(world=world, country=country, name=name)
        self._type = 'baseCompany'

