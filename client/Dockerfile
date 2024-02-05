# Use the official Go image as a builder base
FROM golang:1.16 as builder

# Set the working directory for the build
WORKDIR /app

# Install protoc compiler
RUN apt-get update && apt-get install -y protobuf-compiler

# Copy the go.mod and go.sum files and download the dependencies
COPY ./client/go.mod ./client/go.sum ./
RUN go mod download

# Copy the proto files
COPY ./proto ./proto

# Install the necessary Go tools for generating code from proto files
RUN go install google.golang.org/protobuf/cmd/protoc-gen-go@v1.26
RUN go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@v1.1
RUN go mod tidy

# Add the Go bin directory to the PATH
ENV PATH="$PATH:$(go env GOPATH)/bin"

# Generate Go gRPC code
RUN protoc --proto_path=proto --go_out=. --go-grpc_out=. proto/*.proto

# Copy the rest of the client application source code
COPY ./client .

# Build the client binary, output to the current working directory
RUN CGO_ENABLED=0 GOOS=linux go build -o built .

# Start a new stage from scratch for the final image
FROM alpine:latest  
RUN apk --no-cache add ca-certificates

COPY --from=builder /app /app
COPY --from=builder /app/internal /app/internal

# Set the working directory to /app
WORKDIR /app

# Set the entry point to the built binary
ENTRYPOINT ["./built"]
