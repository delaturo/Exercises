FROM ubuntu
RUN apt-get update
RUN apt-get -y install curl
RUN apt-get -y upgrade 
RUN apt-get -y neofetch
RUN apt-get -y install python3 python3-pip git
RUN mkdir /Exercises
WORKDIR /Exercises
copy . .
# We still need to find a way to install vscode host in the container and add the correct plugins
