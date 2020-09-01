# workaround to solve ModuleNotFoundError: No module named 'categorization_pb2' due to
# current limitations of the protoc generated code, which generates absolute imports
# instead of relative.
# More details in https://github.com/protocolbuffers/protobuf/pull/7470
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
