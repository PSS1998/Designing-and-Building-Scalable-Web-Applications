FROM python:3.10.8-alpine3.16

EXPOSE 5000

WORKDIR /app

COPY . .

RUN python3 -m pip install flask
RUN python3 -m pip install flask_sqlalchemy
RUN python3 -m pip install flask_migrate

CMD ["flask", "run", "--host=0.0.0.0"]
