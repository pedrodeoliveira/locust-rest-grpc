import time
from locust import User, task, between
# noinspection PyPackageRequirements
import grpc

from servers.grpc.categorization_pb2_grpc import TextCategorizationStub
from servers.grpc.categorization_pb2 import TextCategorizationInput
from servers.common import get_random_input_data


class GrpcUser(User):
    abstract = True

    def __init__(self, *args, **kwargs):
        super(GrpcUser, self).__init__(*args, **kwargs)
        target = self.host.lstrip('http://')
        channel = grpc.insecure_channel(target)
        self.stub = TextCategorizationStub(channel=channel)


class ApiUser(GrpcUser):
    wait_time = between(0.9, 1.1)

    @task
    def get_prediction(self):
        data = get_random_input_data()
        input_data = TextCategorizationInput(**data)
        start_time = time.time()
        try:
            self.stub.GetPrediction(input_data)
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            print(e)
            self.environment.events.request_failure.fire(request_type="grpc",
                                                         name=self.host,
                                                         response_time=total_time,
                                                         exception=e)
        else:
            total_time = int((time.time() - start_time) * 1000)
            print(e)
            self.environment.events.request_success.fire(request_type="grpc",
                                                         name=self.host,
                                                         response_time=total_time,
                                                         response_length=0)
