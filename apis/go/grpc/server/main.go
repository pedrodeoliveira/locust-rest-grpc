package main

import (
	"context"
	"log"
	"net"

	pb "github.com/pedrodeoliveira/locust-rest-grpc/apis/go/grpc"
	"google.golang.org/grpc"
)

const (
	port = ":50051"
)

type textCategorizationServer struct {
	pb.UnimplementedTextCategorizationServer
}

// SayHello implements helloworld.GreeterServer
func (s *textCategorizationServer) GetPrediction(ctx context.Context, in *pb.TextCategorizationInput) (*pb.TextCategorizationOutput, error) {
	log.Printf("Received: %v", in.GetText())
	return &pb.TextCategorizationOutput{PredictionId: "123", Text: in.GetText(), Category: 1}, nil
}

func main() {
	lis, err := net.Listen("tcp", port)
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer()
	log.Printf("Started serving ...")
	pb.RegisterTextCategorizationServer(s, &textCategorizationServer{})
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
