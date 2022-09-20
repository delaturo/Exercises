FROM ubuntu
RUN apt-get update
RUN apt-get -y install curl
RUN apt-get -y upgrade 
RUN apt-get -y install python3 python3-pip git
RUN mkdir /Exercises
WORKDIR /Exercises
copy . .
