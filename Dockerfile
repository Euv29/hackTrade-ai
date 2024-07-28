FROM python:3.8-slim

RUN pip install --upgrade pip
RUN pip install tensortrade==1.0.3 numpy pandas

WORKDIR /app
COPY . /app

CMD ["python", "test_tensortrade.py"]
