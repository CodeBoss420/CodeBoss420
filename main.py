import requests
import plotly.express as px 


url = "http://api.github.com/search/repositories?q=language:python+sort:stars+stars:>1000"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)

response_dict = r.json()
print(f"Status Code: {r.status_code}")
print(f"Complete Results: {not response_dict['incomplete_results']}")
repo_dicts = response_dict['items']

repo_names, repos_stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    repos_stars.append(repo_dict['stargazers_count'])
    #hover texts
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}</br>{description}"
    hover_texts.append(hover_text)
     
title = "Most starred python projects on github"
label = {'x' : 'Repositories', 'y' : 'stars'}
fig = px.bar(x = repo_names, y = repos_stars, title = title, labels = label, hover_name=hover_texts)
fig.update_layout(title_font_size = 28, xaxis_title_font_size = 20, yaxis_title_font_size = 20)
fig.show()



