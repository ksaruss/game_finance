from world import World
from object.base_oblect import BaseObject
from object.country import Country

world = World()


world.add_new_country('test1')
world.add_new_country('test2')

country1 = world.get_country_id(1)
country2 = world.get_country_id(2)

country1.add_new_company('productionCompany', 'company1')
country1.add_new_company('productionCompany', 'company2')

print(country1.get_all_company())





