#create a map based on population data getting from a json file

import pygal
import json

#import the world map creater
from pygal.maps.world import COUNTRIES, World

#get the country code by pass the country name
#because some name in the json file dont match the name in COUNTRIES
#so some countries is not exist in the world population map
def get_country_code(country_name):
	for code, name in COUNTRIES.items():
		if name == country_name:
			return code
	return None

print(get_country_code("Viet Nam"))

#load data from json file
filename = "json_file/population_data.json"
with open(filename) as file:
	contents = json.load(file)

#countries group based on population
xs, s, m, l, xl, xxl = [], [], [], [], [], []
for content in contents:
	if content["Year"] == "1970":
		if content["Country Name"] == "Vietnam":
			country_code = get_country_code("Viet Nam")
		else:
			country_code = get_country_code(content["Country Name"])
		population = float(content["Value"])
		if country_code != None:
			if  population< 1000000:
				xs.append(country_code)
			elif population < 10000000:
				s.append(country_code)
			elif population < 20000000:
				m.append(country_code)
			elif population < 50000000:
				l.append(country_code)
			elif population < 100000000:
				xl.append(country_code)
			else:
				xxl.append(country_code)
			
print(xs)
print(s)
print(m)
print(l)
print(xl)
print(xxl)

#create a World map via pygal.maps.world.World(),  
#the map can be readed by web browser 
worldmap_chart = World()
worldmap_chart.title = 'World Population'
worldmap_chart.add('under 1M', xs)
worldmap_chart.add('under 10M', s)
worldmap_chart.add('under 20M', m)
worldmap_chart.add('under 50M', l)
worldmap_chart.add('under 100M', xl)
worldmap_chart.add('over 100M', xxl)

worldmap_chart.render_to_file('svgfile/world_population_1970.svg')
