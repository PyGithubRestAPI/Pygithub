""" Display Github Organizations in Python """
from github import Github
import requests

# Getting Github Repositories
my_git = Github("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")
for repo in my_git.get_user().get_repos():
    print(repo.name)
print("---------------------------------------")

# Getting Github Repositories-Contents
my_code = my_git.get_repo("Thilaga-26/Flask_Python")
contents = my_code.get_contents("")
for content_file in contents:
    print(content_file)
print("---------------------------------------")

# Getting Github Organizations
for orgs in my_git.get_user().get_orgs():
    print(orgs)
print("---------------------------------------")

# Getting Github Organizations-Repositories
USERNAME = "Thilaga-26"
ORG = "PyGithubRestAPI"
URL = f"https://api.github.com/orgs/{ORG}/repos"
USER_DATA = requests.get(URL, timeout=(3.05, 27)).json()
print(USER_DATA)
print("---------------------------------------")
