from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from object.companies.base_company import BaseCompany


class ListCompany:
    def __init__(self):
        self._list_company = {}

    def add_new_company(self, company: 'BaseCompany') -> None:
        self._list_company[company.get_id()] = company

    def get_all_company(self) -> dict:
        return self._list_company

    def get_company_id(self, id_: int):
        return self._list_company[id_]

