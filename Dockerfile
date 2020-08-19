FROM tiangolo/uvicorn-gunicorn:python3.8-slim as builder

RUN apt-get update && \
    apt-get install gcc -y && \
    apt-get clean

COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

WORKDIR /src
COPY . /src

FROM tiangolo/uvicorn-gunicorn:python3.8-slim as app

COPY --from=builder /root/.local /root/.local
COPY --from=builder /src /src

ENV PATH=/root/.local/bin:$PATH

WORKDIR /src
ENV PYTHONPATH=/src

# exposing ports to grpc server (50051), fastapi (8000), locustui (8089) and 5557 and 5558
# for communicating with locust workers
EXPOSE 50051 8000 8089 5558 5557

CMD ["../start.sh"]