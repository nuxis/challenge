FROM python:3.5.2

MAINTAINER Kristoffer Dalby


ENV NAME=challenge

ENV DIR=/srv/app

RUN mkdir $DIR
WORKDIR $DIR

# Install requirements
COPY ./requirements $DIR/requirements
RUN pip install -r requirements/production.txt --upgrade
RUN pip install -r requirements/development.txt --upgrade

# Copy project files
COPY . $DIR

RUN mkdir static media
ENV DJANGO_SETTINGS_MODULE=$NAME.settings.base
RUN python manage.py collectstatic --noinput --clear
ENV DJANGO_SETTINGS_MODULE=$NAME.settings.prod

EXPOSE 8080
EXPOSE 8081

CMD ["sh", "docker-entrypoint.sh"]
