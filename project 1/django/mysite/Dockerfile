FROM python:3.10.8-alpine3.16

EXPOSE 8000

WORKDIR /app

COPY . .

RUN python3 -m pip install django

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
