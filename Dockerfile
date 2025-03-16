FROM python:3.10-alpine

RUN mkdir -p /home/app
WORKDIR /home/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./

RUN adduser -S remote_user
USER remote_user

EXPOSE 5010

CMD [ "gunicorn", "--bind", "0.0.0.0:5010", "wsgi:app" ]