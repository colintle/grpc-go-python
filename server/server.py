import grpc
from concurrent import futures
import time

# Import the generated classes from hello_pb2 and hello_pb2_grpc
import hello_pb2
import hello_pb2_grpc

# Create a class to define the server functions, derived from hello_pb2_grpc.GreeterServicer
class GreeterServicer(hello_pb2_grpc.GreeterServicer):

    # hello_pb2 and hello_pb2_grpc contain the generated request and response classes
    def SayHello(self, request, context):
        # Implement the SayHello RPC method
        response = hello_pb2.HelloReply()
        response.message = 'Hello, {}! This is from Python!'.format(request.name)
        return response

# Create a function to start the server
def serve():
    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Use the generated function `add_GreeterServicer_to_server` to add the defined class to the server
    hello_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)

    # Listen on port 50051
    print('Starting server. Listening on port 50051.')
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
