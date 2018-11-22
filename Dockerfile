FROM python:3.6

RUN mkdir -p /opt/services/autocomplete_feature/
WORKDIR /opt/services/autocomplete_feature/

COPY . .

ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz

RUN pip install -r requirements.txt
WORKDIR autocomplete_feature
RUN chmod +x start.sh

EXPOSE 8000


