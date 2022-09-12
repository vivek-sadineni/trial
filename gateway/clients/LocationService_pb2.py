# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gateway/clients/LocationService.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gateway.requests import SetLocationByPincodeRequest_pb2 as gateway_dot_requests_dot_SetLocationByPincodeRequest__pb2
from gateway.requests import SetCurrentLocationRequest_pb2 as gateway_dot_requests_dot_SetCurrentLocationRequest__pb2
from gateway.responses import SetLocationByPincodeResponse_pb2 as gateway_dot_responses_dot_SetLocationByPincodeResponse__pb2
from gateway.responses import SetCurrentLocationResponse_pb2 as gateway_dot_responses_dot_SetCurrentLocationResponse__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='gateway/clients/LocationService.proto',
  package='fkhp.gateway.layer.client',
  syntax='proto3',
  serialized_options=_b('\n\031fkhp.gateway.layer.clientP\001'),
  serialized_pb=_b('\n%gateway/clients/LocationService.proto\x12\x19\x66khp.gateway.layer.client\x1a\x32gateway/requests/SetLocationByPincodeRequest.proto\x1a\x30gateway/requests/SetCurrentLocationRequest.proto\x1a\x34gateway/responses/SetLocationByPincodeResponse.proto\x1a\x32gateway/responses/SetCurrentLocationResponse.proto2\xc7\x02\n\x0fLocationService\x12\x9b\x01\n\x14setLocationByPincode\x12?.fkhp.gateway.layer.client.requests.SetLocationByPincodeRequest\x1a@.fkhp.gateway.layer.client.response.SetLocationByPincodeResponse\"\x00\x12\x95\x01\n\x12setCurrentLocation\x12=.fkhp.gateway.layer.client.requests.SetCurrentLocationRequest\x1a>.fkhp.gateway.layer.client.response.SetCurrentLocationResponse\"\x00\x42\x1d\n\x19\x66khp.gateway.layer.clientP\x01\x62\x06proto3')
  ,
  dependencies=[gateway_dot_requests_dot_SetLocationByPincodeRequest__pb2.DESCRIPTOR,gateway_dot_requests_dot_SetCurrentLocationRequest__pb2.DESCRIPTOR,gateway_dot_responses_dot_SetLocationByPincodeResponse__pb2.DESCRIPTOR,gateway_dot_responses_dot_SetCurrentLocationResponse__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_LOCATIONSERVICE = _descriptor.ServiceDescriptor(
  name='LocationService',
  full_name='fkhp.gateway.layer.client.LocationService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=277,
  serialized_end=604,
  methods=[
  _descriptor.MethodDescriptor(
    name='setLocationByPincode',
    full_name='fkhp.gateway.layer.client.LocationService.setLocationByPincode',
    index=0,
    containing_service=None,
    input_type=gateway_dot_requests_dot_SetLocationByPincodeRequest__pb2._SETLOCATIONBYPINCODEREQUEST,
    output_type=gateway_dot_responses_dot_SetLocationByPincodeResponse__pb2._SETLOCATIONBYPINCODERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='setCurrentLocation',
    full_name='fkhp.gateway.layer.client.LocationService.setCurrentLocation',
    index=1,
    containing_service=None,
    input_type=gateway_dot_requests_dot_SetCurrentLocationRequest__pb2._SETCURRENTLOCATIONREQUEST,
    output_type=gateway_dot_responses_dot_SetCurrentLocationResponse__pb2._SETCURRENTLOCATIONRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_LOCATIONSERVICE)

DESCRIPTOR.services_by_name['LocationService'] = _LOCATIONSERVICE

# @@protoc_insertion_point(module_scope)
