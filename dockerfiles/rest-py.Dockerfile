FROM tiangolo/uvicorn-gunicorn:python3.8-slim as builder

RUN apt-get update && \
    apt-get install gcc -y && \
    apt-get clean

COPY requirements/requirements-rest-py.txt .
RUN pip install --no-cache-dir --user -r requirements-rest-py.txt

WORKDIR /src
COPY . /src

FROM tiangolo/uvicorn-gunicorn:python3.8-slim as app

COPY --from=builder /root/.local /root/.local
COPY --from=builder /src /src

WORKDIR /src

ENV PATH=/root/.local/bin:$PATH
ENV MODULE_NAME="apis.python.rest.main"
ENV PYTHONPATH=/src

# exposing port to rest api
EXPOSE 80

CMD ["../start.sh"]