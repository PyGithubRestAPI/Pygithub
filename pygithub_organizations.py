""" Display Github Organizations in Python """
import requests
from github import Github

# Getting Github by Username
USERNAME = "Thilaga-26"
URL = f"https://api.github.com/users/{USERNAME}"
USER_DATA = requests.get(URL, timeout=(3.05, 27)).json()
print(USER_DATA)
print("---------------------------------------")

# Getting Github Repositories
my_git = Github()
USER = my_git.get_user(USERNAME)
for repo in USER.get_repos():
    print(repo.name)
