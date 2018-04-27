from github import Github
from utils.secret import githubtoken
from utils.logger import log

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
    channel: the channel where the issue got reported
    message: is the message the user typed without the ping
    author: is the name of the user who submitted the issue

returns:
    nothing

"""
async def create_issue(client, channel, message, author):
    title = ""
    issue_type = ""
    body = ""

    try:
        issue_type, title, body = message.split(';')
    except ValueError:
        await client.send_message(channel, "I'm sorry but your issue request was malformed. Please write it like `<type of issue>; <title>; <body>`!")
        return

    if not title or not body:
        await client.send_message(channel, "Please don't leave the title or the body empty!")
        return

    if issue_type not in ["suggestion", "issue"]:
        await client.send_message(channel, "Please only use `suggestion` or `issue` as the type of issue!")
        return

    r.create_issue(title=": ".join("{} by {}".format(issue_type.strip().title(), author), title.strip()), body=body.strip())
    log("INFO", "create_issue", "A new Issue from '{}' with the title '{}' was created".format(author, title))
    await client.send_message(channel, "Thank you for reporting your {}".format(issue_type.strip()))
