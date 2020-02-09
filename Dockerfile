FROM python:3.8.0a3-alpine3.9

RUN apk update
RUN apk add build-base libffi-dev nodejs nodejs-npm
ENV TZ JST-9

COPY ./ /opt/yansan-web/
WORKDIR /opt/yansan-web
RUN pip install --upgrade pip
RUN pip install -r ./backend/requirements.txt
RUN npm --prefix frontend/ install
RUN npm --prefix frontend/ rebuild node-sass

CMD sh ./assets/docker_bootstrap.sh -d
