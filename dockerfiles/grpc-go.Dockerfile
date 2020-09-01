FROM golang:1.15

RUN go get google.golang.org/grpc
COPY apis/go/grpc /go/src/github.com/pedrodeoliveira/locust-rest-grpc/apis/go/grpc

WORKDIR /go/src/app
COPY . .

RUN cd apis/go/grpc/server && go build app/apis/go/grpc/server
ENTRYPOINT ["/go/src/app/apis/go/grpc/server/server"]
EXPOSE 50051