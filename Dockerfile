FROM python:3.9-slim

WORKDIR /app

# Install curl
RUN apt-get update && apt-get install -y curl

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]