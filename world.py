from current_time import CurrentTime
from object.country import Country
from list_country import ListCountry


class World:
    def __init__(self):
        self._current_time = CurrentTime()
        self._countries = ListCountry()

    def get_current_data(self) -> dict:
        return self._current_time.get_current_data()

    def create_countries(self):
        self._countries = ListCountry()
    
    def add_new_country(self, name: str) -> None:
        self._countries.add_new_country(Country(self, name))

    def get_all_country(self) -> dict:
        return self._countries.get_all_country()

    def get_country_id(self, id_: int):
        return self._countries.get_country_id(id_)
