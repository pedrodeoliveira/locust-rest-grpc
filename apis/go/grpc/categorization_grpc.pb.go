// Code generated by protoc-gen-go-grpc. DO NOT EDIT.

package grpc

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
const _ = grpc.SupportPackageIsVersion6

// TextCategorizationClient is the client API for TextCategorization service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type TextCategorizationClient interface {
	GetPrediction(ctx context.Context, in *TextCategorizationInput, opts ...grpc.CallOption) (*TextCategorizationOutput, error)
}

type textCategorizationClient struct {
	cc grpc.ClientConnInterface
}

func NewTextCategorizationClient(cc grpc.ClientConnInterface) TextCategorizationClient {
	return &textCategorizationClient{cc}
}

func (c *textCategorizationClient) GetPrediction(ctx context.Context, in *TextCategorizationInput, opts ...grpc.CallOption) (*TextCategorizationOutput, error) {
	out := new(TextCategorizationOutput)
	err := c.cc.Invoke(ctx, "/categorization.TextCategorization/GetPrediction", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// TextCategorizationServer is the server API for TextCategorization service.
// All implementations must embed UnimplementedTextCategorizationServer
// for forward compatibility
type TextCategorizationServer interface {
	GetPrediction(context.Context, *TextCategorizationInput) (*TextCategorizationOutput, error)
	mustEmbedUnimplementedTextCategorizationServer()
}

// UnimplementedTextCategorizationServer must be embedded to have forward compatible implementations.
type UnimplementedTextCategorizationServer struct {
}

func (*UnimplementedTextCategorizationServer) GetPrediction(context.Context, *TextCategorizationInput) (*TextCategorizationOutput, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetPrediction not implemented")
}
func (*UnimplementedTextCategorizationServer) mustEmbedUnimplementedTextCategorizationServer() {}

func RegisterTextCategorizationServer(s *grpc.Server, srv TextCategorizationServer) {
	s.RegisterService(&_TextCategorization_serviceDesc, srv)
}

func _TextCategorization_GetPrediction_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(TextCategorizationInput)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TextCategorizationServer).GetPrediction(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/categorization.TextCategorization/GetPrediction",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TextCategorizationServer).GetPrediction(ctx, req.(*TextCategorizationInput))
	}
	return interceptor(ctx, in, info, handler)
}

var _TextCategorization_serviceDesc = grpc.ServiceDesc{
	ServiceName: "categorization.TextCategorization",
	HandlerType: (*TextCategorizationServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "GetPrediction",
			Handler:    _TextCategorization_GetPrediction_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "grpc/categorization.proto",
}