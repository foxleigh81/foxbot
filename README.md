# Telegram -> Todoist Shopping list bot

Allows you to add items to a todoist project via a telegram message

## Installation

This assumes some basic knowledge of developer paradigms such as deploying python apps and using environment variables.

### Step 1:

Rename `.env_sample` to `.env`

### Step 2:
Create a telegram bot using the Botfather: https://core.telegram.org/bots and put the bot token in the `telegram_bot_token` env variable

### Step 3:
Get an API key from todoist, this is really easy, just go to https://todoist.com/prefs/integrations, scroll down to `API Token` and copy the todek into the `todoist_api_token` env variable.

### Step 4:
Get the id of the project you want to be able to add items to by visiting the todoist web app (https://todoist.com/app), clicking on the project in question and copying the number after `/project/` in the url and paste into the `project_id` environement variable

### Step 5:
Deploy the python project to somewhere it can run 24/7 with internet access, I personally run it on my home server which works like a charm but there are plenty of cloud based options available out there.

### Step 6:
Install everything in requirements.txt and then run the project. You're done!

## Usage

You should have been given a username for your bot when you created it, add this to your telegram contact list and now you can add items to your project. You can add as few or as many items as you like, just make sure you only have one item per line.

To view the items in that list in your bot, you can send a `/list` command.

## Roadmap
This is version 1 of my application I have the following updates in mind:
- Add Docker compatibility to make deployment and installation easier
- Allow items to be added via comma separated list as well as one per line
- Allow completions of items from the bots
- Add tests


