# Image
FROM rasa/rasa:2.5.0-full

ARG BOT_NAME

# At the end, set the user to use when running this image
USER root

# create bot directory in container
RUN mkdir -p /bot

# set /bot directory as default working directory
WORKDIR /bot

# copy all file from current dir to /bot in container
COPY . /bot/
RUN pip install --upgrade python-socketio==4.6.0
RUN pip install --upgrade python-engineio==3.13.2
RUN pip install --upgrade Flask-SocketIO==4.3.1
# Author
LABEL Version=1.0.0 maintainer="UFRJ IA"

# train rasa framework and set enveriments
RUN rasa train --quiet --force

#Assim que for carregado o container será executado
#ENTRYPOINT ["/bin/bash", "run.sh"]