FROM ubuntu:latest

RUN apt-get update -y && apt-get install -y python3-pip python-dev

ARG telegram_bot_token
ARG project_id
ARG todoist_api_token

ENV telegram_bot_token $telegram_bot_token
ENV project_id $project_id
ENV todoist_api_token $todoist_api_token

COPY ./requirements.txt /bot/requirements.txt

WORKDIR /bot

COPY . /bot

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3" ]

CMD [ "__main__.py" ]