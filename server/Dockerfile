FROM python:3.8

WORKDIR /app

COPY ./server/requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY ./server /app/

COPY ./proto/* /app/proto/

RUN python -m grpc_tools.protoc -I./proto --python_out=. --grpc_python_out=. ./proto/*

CMD ["python", "server.py"]