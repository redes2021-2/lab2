import grpc
import time
import lab2_pb2
import lab2_pb2_grpc
from concurrent import futures


class OrderVectorServicer(lab2_pb2_grpc.OrderVectorServicer):
    def Order_Vector(self, request, context):
        print("Received request: " + request.vector)

        # order the vector
        vector = request.vector.split(',')
        vector.sort()
        vector = ','.join(vector)
        print("Sending response: " + vector)
        return lab2_pb2.Response(vector=vector)


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
