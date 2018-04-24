from utils.secret import githubtoken
from github import Github

r = None
g = Github(githubtoken)


for repo in g.get_user().get_repos():
    if repo.name == "tas":
        r = repo


def create_issue(submitter, title, body):
    r.create_issue(title=": ".join(submitter, title), body=body)
