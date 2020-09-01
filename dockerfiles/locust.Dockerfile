FROM python:3.8-slim as builder

RUN apt-get update && \
    apt-get install gcc -y && \
    apt-get clean

COPY requirements/requirements-locust.txt .
RUN pip install --no-cache-dir --user -r requirements-locust.txt

WORKDIR /src
COPY . /src

FROM python:3.8-slim  as app

COPY --from=builder /root/.local /root/.local
COPY --from=builder /src /src

ENV PATH=/root/.local/bin:$PATH

WORKDIR /src
COPY . /src
ENV PYTHONPATH=/src

# exposing ports for master web ui (8089) and communication w/locust workers (5557,5558)
EXPOSE 8089 5558 5557

CMD ["locust", "-f" , "locust/locust_rest.py"]