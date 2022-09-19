import hashmap


# abbreviation of the provinces
abbreviation_provinces = hashmap.new()
# set the abbreviation of the provinces
hashmap.set(abbreviation_provinces, 'Ji', 'Hebei')
hashmap.set(abbreviation_provinces, 'Meng', 'InnerMongolia')
hashmap.set(abbreviation_provinces, 'Jing', 'Beijing')
hashmap.set(abbreviation_provinces, 'Hu', 'Shanghai')
hashmap.set(abbreviation_provinces, 'Jiang', 'Xinjiang')


# cities of the provinces
provinces_cities = hashmap.new()
# set the cities of the provinces
hashmap.set(provinces_cities, 'Hebei', 'Zhangjiakou')
hashmap.set(provinces_cities, 'InnerMongolia', 'HuhHot')
hashmap.set(provinces_cities, 'Shanghai', 'Jinganqu')
# add more cities
hashmap.set(provinces_cities, 'Beijing', 'Xichengqu')
hashmap.set(provinces_cities, 'Xinjiang', 'Wulumuqi')

# print some provinces
hashmap.list(abbreviation_provinces)
hashmap.list(provinces_cities)
print(hashmap.get(provinces_cities, hashmap.get(abbreviation_provinces, 'Ji')))

# copy a dict 
try_map = hashmap.dump(provinces_cities)
print(">>>>>>>> Now we have the map copied.")
hashmap.list(try_map)

    