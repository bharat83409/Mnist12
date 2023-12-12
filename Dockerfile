

FROM tensorflow/tensorflow:latest

WORKDIR /app

COPY . /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD ["python", "app1.py"]

