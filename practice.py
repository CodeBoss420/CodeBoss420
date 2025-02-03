import requests
import plotly.express as px 
url = "https://api.github.com/search/repositories?q=language:python+sort:stars+stars:>10000"
headers = {"Accept" : "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")
reslut_dict = r.json()

print(f"Complete Results {not reslut_dict['incomplete_results']}")
repo_dicts = reslut_dict['items']

repo_names, stars, hover_texts = [], [], []

for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
    own = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{own}</br>{description}"
    hover_texts.append(hover_text)
    title = "Most starred python projects in github"
    label = {'x':'Repositories', 'y' : 'stars'}
    
fig = px.bar(x = repo_names, y = stars,title=title, labels=label, hover_name=hover_texts)
fig.update_layout(title_font_size = 30, xaxis_font_size = 20, yaxis_font_size = 20)
fig.show()    



