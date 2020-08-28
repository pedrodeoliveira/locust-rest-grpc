FROM golang:1.15

RUN go get github.com/go-playground/validator/v10 && \
    go get github.com/gorilla/mux && \
    go get github.com/sirupsen/logrus

COPY apis/restgo /go/src/github.com/pedrodeoliveira/locust-rest-grpc/apis/restgo

WORKDIR /go/src/app
COPY . .

RUN cd apis/restgo && go build app/apis/restgo
ENTRYPOINT ["/go/src/app/apis/restgo/restgo"]
EXPOSE 10000