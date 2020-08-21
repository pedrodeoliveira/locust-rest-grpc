import grpc
import logging

from apis.grpc.categorization_pb2_grpc import TextCategorizationStub
from apis.grpc.categorization_pb2 import TextCategorizationInput


log = logging.getLogger(__name__)


if __name__ == "__main__":
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
    with grpc.insecure_channel('34.105.137.182:50051') as channel:
        stub = TextCategorizationStub(channel=channel)
        input_data = TextCategorizationInput(text='predict this')
        response = stub.GetPrediction(input_data)
        log.info(f'Text category: {response.category}')
