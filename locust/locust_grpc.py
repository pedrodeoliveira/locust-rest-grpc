import time
from locust import User, task, between
# noinspection PyPackageRequirements
import grpc

from apis.python.grpc.categorization_pb2_grpc import TextCategorizationStub
from apis.python.grpc.categorization_pb2 import TextCategorizationInput
from apis.python.common import generate_random_text


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
        input_data = TextCategorizationInput(text=generate_random_text())
        start_time = time.time()
        try:
            self.stub.GetPrediction(input_data)
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            print(e)
            self.environment.events.request_failure.fire(request_type="grpc",
                                                         name=self.host,
                                                         response_time=total_time,
                                                         exception=e,
                                                         response_length=0)
        else:
            total_time = int((time.time() - start_time) * 1000)
            self.environment.events.request_success.fire(request_type="grpc",
                                                         name=self.host,
                                                         response_time=total_time,
                                                         response_length=0)
