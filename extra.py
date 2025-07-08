def connect_to_lms():
    for node in nodes:
        try:
            channel = grpc.insecure_channel(node)
            stub = lms_pb2_grpc.LMSStub(channel)
            response = stub.Login(lms_pb2.LoginRequest(username="test", password="test"))
            if response.success:
                print(f"Connected to LMS at {node}")
                return stub
        except grpc.RpcError:
            print(f"Failed to connect to {node}")
    return None