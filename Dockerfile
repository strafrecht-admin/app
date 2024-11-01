FROM python:3.10

RUN apt-get update && apt-get install -y \
    npm
RUN npm install -g mjml
RUN pip install lxml==4.6.3 poetry

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY . /app
WORKDIR /app

ENTRYPOINT ["python", "manage.py"]

CMD ["runserver", "0.0.0.0", "8000"]