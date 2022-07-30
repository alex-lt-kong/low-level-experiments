# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import calculator_pb2 as calculator__pb2


class CalculatorStub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.add = channel.unary_unary(
                '/mytest.Calculator/add',
                request_serializer=calculator__pb2.CalculatorRequest.SerializeToString,
                response_deserializer=calculator__pb2.CalculatorReply.FromString,
                )
        self.minus = channel.unary_unary(
                '/mytest.Calculator/minus',
                request_serializer=calculator__pb2.CalculatorRequest.SerializeToString,
                response_deserializer=calculator__pb2.CalculatorReply.FromString,
                )


class CalculatorServicer(object):
    """The greeting service definition.
    """

    def add(self, request, context):
        """Sends a greeting
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def minus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CalculatorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'add': grpc.unary_unary_rpc_method_handler(
                    servicer.add,
                    request_deserializer=calculator__pb2.CalculatorRequest.FromString,
                    response_serializer=calculator__pb2.CalculatorReply.SerializeToString,
            ),
            'minus': grpc.unary_unary_rpc_method_handler(
                    servicer.minus,
                    request_deserializer=calculator__pb2.CalculatorRequest.FromString,
                    response_serializer=calculator__pb2.CalculatorReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mytest.Calculator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Calculator(object):
    """The greeting service definition.
    """

    @staticmethod
    def add(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mytest.Calculator/add',
            calculator__pb2.CalculatorRequest.SerializeToString,
            calculator__pb2.CalculatorReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def minus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mytest.Calculator/minus',
            calculator__pb2.CalculatorRequest.SerializeToString,
            calculator__pb2.CalculatorReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
