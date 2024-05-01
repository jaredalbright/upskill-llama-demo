FROM ubuntu:latest

USER root

RUN apt-get -y update && apt-get -y install curl

RUN apt install python3 python3-pip -y

RUN curl -fsSL https://ollama.com/install.sh | sh

RUN useradd -ms /bin/bash llama_user
USER llama_user
WORKDIR /home/llama_user

CMD ollama pull llama3