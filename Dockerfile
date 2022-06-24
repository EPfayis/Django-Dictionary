FROM python:3.8-slim-buster


WORKDIR .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["sh", "./entrypoint.sh"]

