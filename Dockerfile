FROM python:3.10-bullseye

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python3", "wsgi.py"]