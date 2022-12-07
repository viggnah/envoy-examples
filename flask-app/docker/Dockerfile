FROM python:3.8.9-slim

WORKDIR /livescores

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . /livescores

EXPOSE 5200

CMD [ "flask", "--app", "sportshome.py", "--debug", "run", "--host=0.0.0.0", "--port=5200"]