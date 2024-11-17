FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install kopf kubernetes

CMD ["kopf", "run", "quarantine_controller.py"]
