from object.base_oblect import BaseObject
from list_company import ListCompany
from object.companies.production_company import ProductionCompany

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from world import World


class Country(BaseObject):
    def __init__(self, world: 'World', name: str):
        super().__init__(world=world, name=name)
        self._type = 'country'
        self._companies = ListCompany()

    def get_name(self) -> str:
        return self._name

    def add_new_company(self, type_: str, name: str) -> None:
        if type_ == 'productionCompany':
            self._companies.add_new_company(ProductionCompany(world=self.get_world(), country=self, name=name))
        else:
            print('error')

    def get_all_company(self) -> dict:
        return self._companies.get_all_company()

    def get_company_ic(self, id_: int):
        return self._companies.get_company_id(id_)

