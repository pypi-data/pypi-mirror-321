"""
Type annotations for bedrock-runtime service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_runtime/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_bedrock_runtime.client import BedrockRuntimeClient

    session = Session()
    client: BedrockRuntimeClient = session.client("bedrock-runtime")
    ```

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import ListAsyncInvokesPaginator
from .type_defs import (
    ApplyGuardrailRequestRequestTypeDef,
    ApplyGuardrailResponseTypeDef,
    ConverseRequestRequestTypeDef,
    ConverseResponseTypeDef,
    ConverseStreamRequestRequestTypeDef,
    ConverseStreamResponseTypeDef,
    GetAsyncInvokeRequestRequestTypeDef,
    GetAsyncInvokeResponseTypeDef,
    InvokeModelRequestRequestTypeDef,
    InvokeModelResponseTypeDef,
    InvokeModelWithResponseStreamRequestRequestTypeDef,
    InvokeModelWithResponseStreamResponseTypeDef,
    ListAsyncInvokesRequestRequestTypeDef,
    ListAsyncInvokesResponseTypeDef,
    StartAsyncInvokeRequestRequestTypeDef,
    StartAsyncInvokeResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack


__all__ = ("BedrockRuntimeClient",)


class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ModelErrorException: Type[BotocoreClientError]
    ModelNotReadyException: Type[BotocoreClientError]
    ModelStreamErrorException: Type[BotocoreClientError]
    ModelTimeoutException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class BedrockRuntimeClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-runtime.html#BedrockRuntime.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_runtime/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        BedrockRuntimeClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-runtime.html#BedrockRuntime.Client)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_runtime/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-runtime/client/can_paginate.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_runtime/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-runtime/client/generate_presigned_url.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_runtime/client/#generate_presigned_url)
        """

    def apply_guardrail(
        self, **kwargs: Unpack[ApplyGuardrailRequestRequestTypeDef]
    ) -> ApplyGuardrailResponseTypeDef:
        """
        The action to apply a guardrail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-runtime/client/apply_guardrail.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_runtime/client/#apply_guardrail)
        """

    def converse(self, **kwargs: Unpack[ConverseRequestRequestTypeDef]) -> ConverseResponseTypeDef:
        """
        Sends messages to the specified Amazon Bedrock model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-runtime/client/converse.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_runtime/client/#converse)
        """

    def converse_stream(
        self, **kwargs: Unpack[ConverseStreamRequestRequestTypeDef]
    ) -> ConverseStreamResponseTypeDef:
        """
        Sends messages to the specified Amazon Bedrock model and returns the response
        in a stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-runtime/client/converse_stream.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_runtime/client/#converse_stream)
        """

    def get_async_invoke(
        self, **kwargs: Unpack[GetAsyncInvokeRequestRequestTypeDef]
    ) -> GetAsyncInvokeResponseTypeDef:
        """
        Retrieve information about an asynchronous invocation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-runtime/client/get_async_invoke.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_runtime/client/#get_async_invoke)
        """

    def invoke_model(
        self, **kwargs: Unpack[InvokeModelRequestRequestTypeDef]
    ) -> InvokeModelResponseTypeDef:
        """
        Invokes the specified Amazon Bedrock model to run inference using the prompt
        and inference parameters provided in the request body.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-runtime/client/invoke_model.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_runtime/client/#invoke_model)
        """

    def invoke_model_with_response_stream(
        self, **kwargs: Unpack[InvokeModelWithResponseStreamRequestRequestTypeDef]
    ) -> InvokeModelWithResponseStreamResponseTypeDef:
        """
        Invoke the specified Amazon Bedrock model to run inference using the prompt and
        inference parameters provided in the request body.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-runtime/client/invoke_model_with_response_stream.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_runtime/client/#invoke_model_with_response_stream)
        """

    def list_async_invokes(
        self, **kwargs: Unpack[ListAsyncInvokesRequestRequestTypeDef]
    ) -> ListAsyncInvokesResponseTypeDef:
        """
        Lists asynchronous invocations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-runtime/client/list_async_invokes.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_runtime/client/#list_async_invokes)
        """

    def start_async_invoke(
        self, **kwargs: Unpack[StartAsyncInvokeRequestRequestTypeDef]
    ) -> StartAsyncInvokeResponseTypeDef:
        """
        Starts an asynchronous invocation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-runtime/client/start_async_invoke.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_runtime/client/#start_async_invoke)
        """

    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_async_invokes"]
    ) -> ListAsyncInvokesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-runtime/client/get_paginator.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_runtime/client/#get_paginator)
        """
