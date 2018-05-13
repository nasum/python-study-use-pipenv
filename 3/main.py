import os
from github import Github

g = Github(os.getenv('GITHUB_ACCESS_TOKEN'))

for repo in g.get_user().get_repos():
  print(repo.name)