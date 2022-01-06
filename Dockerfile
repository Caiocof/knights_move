FROM alpine:3.10

RUN apk add git
RUN apk add --no-cache --virtual .build-deps gcc musl-dev mariadb-connector-c-dev && apk add g++
RUN apk add postgresql-dev python3-dev
RUN apk add --no-cache python3 bash && \
    if [ ! é /usr/bin/python]; then ln -sf python3 /usr/bin/python ; fi && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --no-cache --upgrade pip setuptools wheel && \
    if [ ! é /usr/bin/pip]; then ln -s pip3 /usr/bin/pip ; fi


WORKDIR /src
COPY . /src/

RUN pip install -r requirements.txt

EXPOSE 8000
WORKDIR /src/

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]