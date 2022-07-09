#!/bin/bash
python -m grpc_tools.protoc -I./protos protos/lab2.proto --python_out=. --grpc_python_out=.