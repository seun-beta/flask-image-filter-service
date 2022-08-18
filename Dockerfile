FROM python:3.7.13-alpine3.16

WORKDIR /app

COPY . .

RUN pip install -r requirements/production.txt

ENV PORT=5000

CMD ["flask", "run"]
