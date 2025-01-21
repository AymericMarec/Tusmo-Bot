FROM python:3

WORKDIR /usr/src/app

RUN pip install flask

COPY . .

CMD [ "python", "./API.py" ]