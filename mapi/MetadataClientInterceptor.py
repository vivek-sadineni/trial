from collections.abc import Callable

import grpc
from google.protobuf.internal.well_known_types import Any
from grpc_interceptor import ClientCallDetails, ClientInterceptor


class MetadataClientInterceptor(ClientInterceptor):

    def intercept(
            self,
            method: Callable,
            request_or_iterator: Any,
            call_details: grpc.ClientCallDetails,
    ):
        """Override this method to implement a custom interceptor.

        This method is called for all unary and streaming RPCs. The interceptor
        implementation should call `method` using a `grpc.ClientCallDetails` and the
        `request_or_iterator` object as parameters. The `request_or_iterator`
        parameter may be type checked to determine if this is a singluar request
        for unary RPCs or an iterator for client-streaming or client-server streaming
        RPCs.

        Args:
            method: A function that proceeds with the invocation by executing the next
                interceptor in the chain or invoking the actual RPC on the underlying
                channel.
            request_or_iterator: RPC request message or iterator of request messages
                for streaming requests.
            call_details: Describes an RPC to be invoked.

        Returns:
            The type of the return should match the type of the return value received
            by calling `method`. This is an object that is both a
            `Call <https://grpc.github.io/grpc/python/grpc.html#grpc.Call>`_ for the
            RPC and a `Future <https://grpc.github.io/grpc/python/grpc.html#grpc.Future>`_.

            The actual result from the RPC can be got by calling `.result()` on the
            value returned from `method`.
        """
        new_details = ClientCallDetails(
            method=call_details.method,
            timeout=call_details.timeout,
            metadata=[
                ("content-type", "application/grpc-web+proto"),
                ("x-client", "mapi"),
                ("x-cookie",
                 "fb.1.1662015076054.1596726062; moe_uuid=43b0bccf-d0da-4dff-a274-0fd2dfca531d; isPanIndia=Y; cartsynch=0; WHId=1; UserLocationPincode=560103; PanIndiaCityName=Others; userLocation=Others; PanIndiaStateName=Others; PanIndiaStateCode=OT; PanIndiaCityID=6310; LocationSkipped=0; IsLab=0; PanIndiaStateID=37; sspl_csrf=9cf44d9773fd4e2999e4a7aca8c03e00; UIVAL=BQcAdA%3D%3D; cisession_in_com=c1defbc5b983305d72dd32a3b3137e95; AWSALBTG=W0e8uSeeGv9f1/J3uaDDZLBrulZ7j3/9HupdAhvwn4pW8UCftHEabTKXgQYReX5rPIUbEqEV9hepoxJTzJAJX57MYwu2XMfYU/xbjoOeaE60wf95DZgS8k+04XgAjB9FcXVsM1pS264/Xum2/q5EH2cV6Hq6WJhMW2dcp7fvPolNsl53Bgw=; AWSALBTGCORS=W0e8uSeeGv9f1/J3uaDDZLBrulZ7j3/9HupdAhvwn4pW8UCftHEabTKXgQYReX5rPIUbEqEV9hepoxJTzJAJX57MYwu2XMfYU/xbjoOeaE60wf95DZgS8k+04XgAjB9FcXVsM1pS264/Xum2/q5EH2cV6Hq6WJhMW2dcp7fvPolNsl53Bgw="),
                ("x-csrf-test-name", "9cf44d9773fd4e2999e4a7aca8c03e00"),
                ("x-timestamp", "142433"),
                ("x-user-agent",
                 "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36")
            ],
            credentials=call_details.credentials,
            wait_for_ready=call_details.wait_for_ready,
            compression=call_details.compression,
        )

        return method(request_or_iterator, new_details)



