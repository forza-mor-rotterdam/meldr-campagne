FROM python:3.9.15-slim-buster

ENV PYTHONUNBUFFERED 1

EXPOSE 8000

WORKDIR /app/

RUN apt-get update && apt-get install -y postgresql-client build-essential python-dev
RUN pip install --upgrade pip

COPY . /app/

RUN chmod +x /app/deploy/docker-entrypoint.sh && chown root:root /app/deploy/docker-entrypoint.sh

RUN pip install --no-cache-dir -r /app/requirements.txt

CMD ["bash", "/app/deploy/docker-entrypoint.sh"]