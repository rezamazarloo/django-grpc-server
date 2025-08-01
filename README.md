# django-grpc-server

A test project for using Django with gRPC based on [djangogrpcframework]

## Requirements (very important!!)

This project requires only python 3.10 and the following Python packages versions otherwise it will not work:

```plaintext
djangogrpcframework==0.2.1
grpcio==1.60.1
grpcio-tools==1.60.1
protobuf==4.25.3
```

## requires_system_checks error solution

to avoid the `requires_system_checks` error, we recreated the grpcrunserver with ourr custom command `rungrpcserver` which is a copy of the original `grpcrunserver` command from `djangogrpcframework`. and we set the `requires_system_checks` attribute to an empty list.


## generate .proto file from Django model

```bash
python manage.py generateproto --model blog.models.Post --fields id,title,content --file  blog/protos/post/post.proto
```

## Generate python gRPC code from .proto file

```bash
python -m grpc_tools.protoc --proto_path=. --python_out=. --grpc_python_out=. --pyi_out=. blog/protos/post/post.proto
```

## Run the gRPC server

```bash
python manage.py rungrpcserver --dev 0.0.0.0:50051
```
