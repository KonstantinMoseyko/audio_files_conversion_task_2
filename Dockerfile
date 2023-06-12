FROM python:3.10-bullseye

RUN apt-get update && apt-get install -y ffmpeg

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python3", "wsgi.py"]