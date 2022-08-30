FROM python:3.7.13-alpine3.16

WORKDIR /

RUN apk add --no-cache jpeg-dev zlib-dev

RUN apk add --no-cache --virtual .build-deps build-base linux-headers \
    && pip install Pillow

ENV PYTHONUNBUFFERED=1

ENV PYTHONDONTWRITEBYTECODE=1

COPY /requirements/* ./requirements/

COPY .flaskenv ./

RUN pip install -r requirements/production.txt

COPY . .

ENV PORT=5000
ENV SECRET_KEY=notsafe

CMD ["flask", "run"]
