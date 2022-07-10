import grpc
import lab2_pb2
import lab2_pb2_grpc
from concurrent import futures


class OrderVectorServicer(lab2_pb2_grpc.OrderVectorServicer):
    def OrderVector(self, request, context):
        vector = request.vector
        # sort the vector
        vector.sort()
        # get max and min
        maior = vector[-1]
        menor = vector[0]

        return lab2_pb2.Response(maior=maior, menor=menor)


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=3))
    lab2_pb2_grpc.add_OrderVectorServicer_to_server(
        OrderVectorServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('Server running...')
    server.wait_for_termination()


main()
