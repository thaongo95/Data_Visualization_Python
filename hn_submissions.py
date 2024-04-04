import requests
import pygal

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
response = requests.get(url)
print("Status code:", response.status_code)
submission_ids = response.json()

story_urls = []
for submission_id in submission_ids:
	story_urls.append("https://hacker-news.firebaseio.com/v0/item/{}.json".format(submission_id))
for story in story_urls:
	res = requests.get(story)
	res_json = res.json()
	if res.status_code==200:
		print(res_json["id"])
		print(res_json["title"])
		print(res_json["url"])
		print(res_json.get('descendants', 0))
