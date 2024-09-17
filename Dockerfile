FROM ubuntu:22.04
RUN apt-get update && \
    apt-get install python3.11 python3-pip -y && \
    pip3 install flask pymongo

WORKDIR /app
COPY . .
CMD [ "python3", "app.py" ]