from utils.secret import githubtoken
from github import Github

r = None
g = Github(githubtoken)


for repo in g.get_user().get_repos():
    if repo.name == "tas":
        r = repo


"""
This function will create an issue on github once one is found.

The message will look like this
    @Bot <type of issue>; <title>; <body>

So for example
    @Bot suggestion; better money name; i don't like euro, shekles is way cooler
    @Bot issue; comand xyz breaks on certain input; the input looks like this "blub"

params:
    client: is the client object of the bot
    message: is the message the user typed without the ping

"""
async def create_issue(client, message):
    submitter = ""
    title = ""
    body = ""

    r.create_issue(title=": ".join(submitter, title), body=body)
