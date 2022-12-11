FROM python:3.9

COPY ./src /app/src
COPY ./api /app/api
COPY requirements.txt /app

WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "src.server:app", "--host=0.0.0.0", "--reload"]
