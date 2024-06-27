from baseObject import Country


class ListCountry:
    def __init__(self):
        self._list_country = {}

    def add_new_country(self, country: Country):
        self._list_country[country.get_id()] = country

    def get_country(self):
        pass
