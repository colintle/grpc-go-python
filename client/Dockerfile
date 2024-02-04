# Use the official Go image as a builder base
FROM golang:1.16 as builder

WORKDIR /app

# Install protoc compiler
RUN apt-get update && apt-get install -y protobuf-compiler

# Copy the go.mod and if you have go.sum, copy it here as well
COPY ./client/go.mod /app/
RUN go mod download

# Copy proto file
COPY ./proto/* /app/proto/

RUN go install google.golang.org/protobuf/cmd/protoc-gen-go@v1.26
RUN go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@v1.1
RUN go mod tidy

ENV PATH="$PATH:$(go env GOPATH)/bin"

# Generate Go gRPC code
RUN protoc --proto_path=./proto --go_out=. --go-grpc_out=. ./proto/*

# Copy the rest of the client application source code
COPY ./client /app/

# Build the client binary
RUN CGO_ENABLED=0 GOOS=linux go build -o /client 

# Start a new stage from scratch for the final image
FROM alpine:latest  
RUN apk --no-cache add ca-certificates

COPY --from=builder /client /app/

ENTRYPOINT ["/app/client"]
