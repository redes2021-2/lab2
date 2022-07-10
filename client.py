import grpc
import lab2_pb2
import lab2_pb2_grpc
from math import sqrt
import random

tam_max = 500000


def randomizer(i):
    return (i - (random.randint(0, tam_max) / 2))**2


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = lab2_pb2_grpc.OrderVectorStub(channel)
        # create 500k vector with random numbers
        vector = [sqrt(randomizer(i)) for i in range(tam_max)]
        response = stub.OrderVector(lab2_pb2.Request(
            vector=vector))
        print('maior:', response.maior)
        print('menor:', response.menor)


if __name__ == '__main__':
    run()
