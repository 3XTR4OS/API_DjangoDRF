FROM python:3.8
RUN apt-get update -y
RUN apt-get upgrade -y

WORKDIR /app

Copy ./requirements.txt ./
RUN pip install -r requirements.txt
# 12:30 тайминг
COPY . .

CMD ["python3", "./manage.py", "runserver", "0.0.0.0:8000"]