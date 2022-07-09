import grpc
import time
import lab2_pb2
import lab2_pb2_grpc
from concurrent import futures
import random
from math import sqrt


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = lab2_pb2_grpc.OrderVectorStub(channel)
    # create random vector of 500k elements
    vector = [0] * 500000
    for i in range(len(vector)):
        vector[i] = (i - random.randint(0, 500000)/2) ** 2
        vector[i] = sqrt(vector[i])
    response = stub.OrderVector(lab2_pb2.Request(vector=vector))
    print("Received response: " + response.maior + " " + response.menor)


run()
