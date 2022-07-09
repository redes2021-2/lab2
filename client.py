import grpc
import time
import lab2_pb2
import lab2_pb2_grpc
from concurrent import futures


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = lab2_pb2_grpc.OrderVectorStub(channel)
        response = stub.Order_Vector(lab2_pb2.Request(
            vector='1,2,3,15,0,12,4,5,6,7,8,9,10,11'))
        print("Received response: " + response.ma)
