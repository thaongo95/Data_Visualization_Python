import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

#get data from github API
#need to know how to create a API to request real-time data
#the url below is a query to get the list of git repo that in top 30 most stars python repos 
#the API request have a rare limit (example 10 times per minute)
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code: ", r.status_code) #status_code=200 is success

response_dict = r.json()

print(response_dict['total_count'])
print(response_dict['incomplete_results'])
items = response_dict['items']

keys = []
for key in items[0].keys():
	keys.append(key)

owner_info = []
languages = []
licenses = []
topics = []

#get the owner information
for i in range(len(items)):
	owner_info.append(items[i]['owner'])
#get the language
for i in range(len(items)):
	languages.append(items[i]['language'])
#get the type of license
for i in range(len(items)):
	licenses.append(items[i]['license'])
#get the topics
for i in range(len(items)):
	topic = items[i]['topics']
	topics.append(topic)
	print("Number {}:".format(i+1))
	print(topic)
	print("####################\n")

stars_list, plot_dicts, names = [], [], []

for i in range(len(items)):
	print("Programmer {}: ".format(i))
	print("\tName: ", items[i]["name"])
	print("\tOwner: ", items[i]["owner"]["login"])
	print("\tStars: ", items[i]["stargazers_count"])
	print("\tRepository: ", items[i]["html_url"])
	print("\tCreated: ", items[i]["created_at"])
	print("\tUpdated: ", items[i]["updated_at"])
	print("\tDescription: ", items[i]["description"])
	print("###########################")
	stars_list.append(items[i]["stargazers_count"])
	names.append(items[i]["name"])
	plot_dict = {
		'value': items[i]["stargazers_count"],
		'label': items[i]["description"],
		'xlink': items[i]["html_url"],
	}
	plot_dicts.append(plot_dict)

my_style = LS('#333366', base_style=LCS)
bar = pygal.Bar(style= my_style, x_label_rotation = 45, show_legend = False)
bar.title = "Python language projects most stars in Github"
bar.x_labels = names
bar.add("Stars", plot_dicts)
bar.render_to_file("svgfile/python_repos.svg")
