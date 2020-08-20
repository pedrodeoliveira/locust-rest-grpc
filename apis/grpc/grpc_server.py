from concurrent import futures

# noinspection PyPackageRequirements
import grpc
import logging
import os

from apis.grpc.categorization_pb2_grpc import TextCategorizationServicer, \
    add_TextCategorizationServicer_to_server
from apis.grpc.categorization_pb2 import TextCategorizationOutput
from apis.common import categorize_text, generate_random_id


log_level = os.getenv('LOG_LEVEL', 'INFO')
logging.basicConfig(format='%(levelname)s:%(message)s', level=getattr(logging, log_level))
log = logging.getLogger(__name__)


class TextCategorizationService(TextCategorizationServicer):

    def GetPrediction(self, request, context):
        log.debug(f'Received request: {request}')
        category = categorize_text(text=request.text)
        prediction_id = generate_random_id()
        log.debug(f'Predicted category: {category}')
        response = TextCategorizationOutput(prediction_id=prediction_id,
                                            text=request.text, category=category)
        return response


class TextCategorizationServer:

    def __init__(self, max_workers):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers))
        add_TextCategorizationServicer_to_server(TextCategorizationService(), self.server)
        self.server.add_insecure_port('[::]:50051')

    def start(self):
        log.info('Started server on port 50051 ...')
        self.server.start()
        self.server.wait_for_termination()


if __name__ == "__main__":
    workers = int(os.getenv('MAX_WORKERS', 4))
    TextCategorizationServer(workers).start()
