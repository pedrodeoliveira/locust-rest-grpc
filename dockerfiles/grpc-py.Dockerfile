FROM python:3.8-slim

COPY requirements/requirements-grpc-py.txt .
RUN pip install --no-cache-dir -r requirements-grpc-py.txt

WORKDIR /app
COPY . /app
ENV PYTHONPATH=/app

# expose port for gRPC server
EXPOSE 50051

ENTRYPOINT ["python", "apis/python/grpc/grpc_server.py"]