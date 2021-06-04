FROM ubuntu:latest

RUN apt-get update -y && apt-get install -y python3-pip python-dev

EXPOSE 80
EXPOSE 5565

COPY ./requirements.txt /bot/requirements.txt

WORKDIR /bot

RUN pip3 install -r requirements.txt

COPY . /bot

ENTRYPOINT [ "python3" ]

CMD [ "__main__.py" ]