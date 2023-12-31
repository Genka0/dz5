FROM python:3.11.4-slim

RUN mkdir my_code

WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get upgrade

COPY . .

# CMD ["python", "stationlocation.py", "timestamp", "iss_position", "message"]
CMD ["python", "my_code/stationlocation.py"]
