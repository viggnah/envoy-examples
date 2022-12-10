FROM python:3.8.9-slim

WORKDIR /footballscores

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . /footballscores

EXPOSE 6200

CMD [ "flask", "--app", "footballscores.py", "--debug", "run", "--host=0.0.0.0", "--port=6200"]