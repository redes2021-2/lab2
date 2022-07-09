import grpc
import time
import lab2_pb2
import lab2_pb2_grpc
from concurrent import futures


class OrderVectorServicer(lab2_pb2_grpc.OrderVectorServicer):
    def OrderVector(self, request, context):
        response = lab2_pb2.Response()
        # sort request vector
        vector = request.vector
        vector.sort()
        # find maior and menor values
        response.maior = self.vector[-1]
        response.menor = self.vector[0]

        print("Sending response: " + response)
        return response


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    lab2_pb2_grpc.add_OrderVectorServicer_to_server(
        OrderVectorServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started at port 50051")
    server.wait_for_termination()


main()
