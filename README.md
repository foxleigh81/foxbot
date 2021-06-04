![Foxbot logo](./icon.png)
# Foxbot
# A Telegram -> Todoist list bot

Foxbot allows you to add items to a todoist project via a telegram message. 

There are two options for running the application, via manual installation into a Python environment or via Docker.

## Usage

You should have been given a username for your bot when you created it, add this to your telegram contact list and now you can add items to your project. You can add as few or as many items as you like, just make sure you only have one item per line.

To view the items in that list in your bot, you can send a `/list` command.

## Get your API keys and project ID

First of all, create a telegram bot using the Botfather: https://core.telegram.org/bots and make a note of the bot token.

Next, get an API key from todoist, this is really easy, just go to https://todoist.com/prefs/integrations, scroll down to `API Token` and make a note of the token.

Finally, get the id of the project you want to be able to add items to by visiting the todoist web app (https://todoist.com/app), clicking on the project in question and noting the number after `/project/` in the url 
## Manual installation

This assumes some basic knowledge of developer paradigms such as deploying python apps and using environment variables.
### Step 1:

Rename `.env_sample` to `.env`

### Step 2:

Put the bot token you got from The Botfather in the `telegram_bot_token` env variable

### Step 3:
Copy your telegram API token into the `todoist_api_token` env variable.

### Step 4:
Get your todoist project id and paste into the `project_id` env variable

### Step 5:
Deploy the python project to somewhere it can run 24/7 with internet access, I personally run it on my home server which works like a charm but there are plenty of cloud based options available out there.

### Step 6:
Install everything in requirements.txt and then run the project. You're done!

## Docker (recommended)

To run via Docker, simply pull the docker image:

```
docker pull foxleigh81/foxbot
```

and then run with the following commands

```

docker run -e 'telegram_bot_token=[your bot token here]' -e 'todoist_api_token=[your todoist token here]' -e 'project_id=[your project id here]' foxbot
```
Don't forget to replace everything in each square bracket (including the bracket itself) with the tokens and id you retrieved above.

## Roadmap
This is version 1 of my application I have the following updates in mind:
- Allow items to be added via comma separated list as well as one per line
- Allow completions of items from the bots
- Add tests


