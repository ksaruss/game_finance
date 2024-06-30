from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from object.country import Country


class ListCountry:
    def __init__(self):
        self._list_country = {}

    def add_new_country(self, country: 'Country') -> None:
        self._list_country[country.get_id()] = country

    def get_all_country(self) -> dict:
        return self._list_country

    def get_country_id(self, id_: int):
        return self._list_country[id_]



