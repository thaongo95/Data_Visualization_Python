import json
import pygal
import matplotlib.pyplot as plt

filename = 'json_file/population_data.json'

#get the data from filepath and store it into pop_data
with open(filename) as file:
	pop_data = json.load(file)

#create a dict Name:Code for findCode use
name_code = {}
for pop_dict in pop_data:
	if pop_dict['Country Name'] not in name_code:
		name_code.update({pop_dict['Country Name']:pop_dict['Country Code']})

#func to find the code corresponding to the country name
def findCode(name):
	return name_code[name]

names, codes, years, values = [], [], [], []
pop_vietnam = []

#loop through the pop_data and find useful data
for pop_dict in pop_data:
	if pop_dict['Year'] == '2010':
		value = float(pop_dict['Value'])
		if value >= 1000000000:
			names.append(pop_dict['Country Name'])
			codes.append(pop_dict['Country Code'])
			
			values.append(float(pop_dict['Value']))
	if pop_dict['Country Name'] == "Vietnam":
		pop_vietnam.append(int(float(pop_dict['Value'])))
		years.append(int(pop_dict['Year']))
		
#create a bar instance to plot data
bar = pygal.Bar()
print(names)
bar.x_labels = names
bar.add("population", values)
bar.render_to_file('svgfile/populationB-2010.svg')

print(findCode("China"))
print(name_code)

plt.figure(dpi=128, figsize=(16,9))
plt.scatter(years, pop_vietnam, s=8, c="red")
plt.xlabel("Years", fontsize=16)
plt.ylabel("Population", fontsize=16)
plt.show()
