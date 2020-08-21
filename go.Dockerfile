FROM golang:1.15

RUN go get google.golang.org/grpc
COPY apis/grpcgo /go/src/github.com/pedrodeoliveira/locust-rest-grpc/apis/grpcgo

WORKDIR /go/src/app
COPY . .

RUN cd apis/grpcgo/server && go build app/apis/grpcgo/server
ENTRYPOINT ["/go/src/app/apis/grpcgo/server/server"]
EXPOSE 50051