FROM alpine:3.4

MAINTAINER Kristoffer Dalby


ENV NAME=challenge
ENV DIR=/srv/app
ENV LIBRARY_PATH=/lib:/usr/lib

RUN apk update
RUN apk add postgresql-dev \
        git \
        mailcap \
        build-base \
        python3-dev \
        jpeg-dev \
        zlib-dev \
        python3 \
        linux-headers \
        pcre-dev


WORKDIR $DIR

# Install requirements
COPY ./requirements $DIR/requirements
RUN python3 -m pip install pip -U && \
    pip3 install -r requirements/production.txt --upgrade && \
    pip3 install -r requirements/development.txt --upgrade

# Delete unneeded files.
RUN apk del build-base \
        python-dev

# Copy project files
COPY . $DIR

RUN mkdir collected_static media
ENV DJANGO_SETTINGS_MODULE=$NAME.settings.dev
RUN python3 manage.py collectstatic --noinput --clear

ENV DJANGO_SETTINGS_MODULE=$NAME.settings.prod
EXPOSE 8080
EXPOSE 8081

ENTRYPOINT ["/srv/app/docker-entrypoint.sh"]
