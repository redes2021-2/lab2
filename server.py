import grpc
import time
import lab2_pb2
import lab2_pb2_grpc
from concurrent import futures


class OrderVectorServicer(lab2_pb2_grpc.OrderVectorServicer):
    def Order_Vector(self, request, context):
        print("Received request: " + request.name)
        response = lab2_pb2.Response(name=request.name, count=request.count)
        return response


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started at port 50051")
    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)


main()
print("Server stopped")
exit(0)
