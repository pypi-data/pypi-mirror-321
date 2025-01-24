# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.block import Block
from ..core.unchecked_base_model import construct_type
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..core.jsonable_encoder import jsonable_encoder
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class BlocksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        label: typing.Optional[str] = None,
        templates_only: typing.Optional[bool] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Block]:
        """
        Parameters
        ----------
        label : typing.Optional[str]
            Labels to include (e.g. human, persona)

        templates_only : typing.Optional[bool]
            Whether to include only templates

        name : typing.Optional[str]
            Name of the block

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Block]
            Successful Response

        Examples
        --------
        from letta_client import Letta

        client = Letta(
            token="YOUR_TOKEN",
        )
        client.blocks.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/blocks/",
            method="GET",
            params={
                "label": label,
                "templates_only": templates_only,
                "name": name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[Block],
                    construct_type(
                        type_=typing.List[Block],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        *,
        value: str,
        label: str,
        limit: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        is_template: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Block:
        """
        Parameters
        ----------
        value : str
            Value of the block.

        label : str
            Label of the block.

        limit : typing.Optional[int]
            Character limit of the block.

        name : typing.Optional[str]
            Name of the block if it is a template.

        is_template : typing.Optional[bool]

        description : typing.Optional[str]
            Description of the block.

        metadata : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Metadata of the block.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Block
            Successful Response

        Examples
        --------
        from letta_client import Letta

        client = Letta(
            token="YOUR_TOKEN",
        )
        client.blocks.create(
            value="value",
            label="label",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/blocks/",
            method="POST",
            json={
                "value": value,
                "limit": limit,
                "name": name,
                "is_template": is_template,
                "label": label,
                "description": description,
                "metadata_": metadata,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Block,
                    construct_type(
                        type_=Block,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, block_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Block:
        """
        Parameters
        ----------
        block_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Block
            Successful Response

        Examples
        --------
        from letta_client import Letta

        client = Letta(
            token="YOUR_TOKEN",
        )
        client.blocks.get(
            block_id="block_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/blocks/{jsonable_encoder(block_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Block,
                    construct_type(
                        type_=Block,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, block_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Block:
        """
        Parameters
        ----------
        block_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Block
            Successful Response

        Examples
        --------
        from letta_client import Letta

        client = Letta(
            token="YOUR_TOKEN",
        )
        client.blocks.delete(
            block_id="block_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/blocks/{jsonable_encoder(block_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Block,
                    construct_type(
                        type_=Block,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(
        self,
        block_id: str,
        *,
        value: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        is_template: typing.Optional[bool] = OMIT,
        label: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Block:
        """
        Parameters
        ----------
        block_id : str

        value : typing.Optional[str]
            Value of the block.

        limit : typing.Optional[int]
            Character limit of the block.

        name : typing.Optional[str]
            Name of the block if it is a template.

        is_template : typing.Optional[bool]
            Whether the block is a template (e.g. saved human/persona options).

        label : typing.Optional[str]
            Label of the block (e.g. 'human', 'persona') in the context window.

        description : typing.Optional[str]
            Description of the block.

        metadata : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Metadata of the block.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Block
            Successful Response

        Examples
        --------
        from letta_client import Letta

        client = Letta(
            token="YOUR_TOKEN",
        )
        client.blocks.update(
            block_id="block_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/blocks/{jsonable_encoder(block_id)}",
            method="PATCH",
            json={
                "value": value,
                "limit": limit,
                "name": name,
                "is_template": is_template,
                "label": label,
                "description": description,
                "metadata_": metadata,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Block,
                    construct_type(
                        type_=Block,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def link_agent_memory_block(
        self, block_id: str, *, agent_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Link a memory block to an agent.

        Parameters
        ----------
        block_id : str

        agent_id : str
            The unique identifier of the agent to attach the source to.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from letta_client import Letta

        client = Letta(
            token="YOUR_TOKEN",
        )
        client.blocks.link_agent_memory_block(
            block_id="block_id",
            agent_id="agent_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/blocks/{jsonable_encoder(block_id)}/attach",
            method="PATCH",
            params={
                "agent_id": agent_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def unlink_agent_memory_block(
        self, block_id: str, *, agent_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Unlink a memory block from an agent

        Parameters
        ----------
        block_id : str

        agent_id : str
            The unique identifier of the agent to attach the source to.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from letta_client import Letta

        client = Letta(
            token="YOUR_TOKEN",
        )
        client.blocks.unlink_agent_memory_block(
            block_id="block_id",
            agent_id="agent_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/blocks/{jsonable_encoder(block_id)}/detach",
            method="PATCH",
            params={
                "agent_id": agent_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncBlocksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        label: typing.Optional[str] = None,
        templates_only: typing.Optional[bool] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Block]:
        """
        Parameters
        ----------
        label : typing.Optional[str]
            Labels to include (e.g. human, persona)

        templates_only : typing.Optional[bool]
            Whether to include only templates

        name : typing.Optional[str]
            Name of the block

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Block]
            Successful Response

        Examples
        --------
        import asyncio

        from letta_client import AsyncLetta

        client = AsyncLetta(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.blocks.list()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/blocks/",
            method="GET",
            params={
                "label": label,
                "templates_only": templates_only,
                "name": name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[Block],
                    construct_type(
                        type_=typing.List[Block],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        *,
        value: str,
        label: str,
        limit: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        is_template: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Block:
        """
        Parameters
        ----------
        value : str
            Value of the block.

        label : str
            Label of the block.

        limit : typing.Optional[int]
            Character limit of the block.

        name : typing.Optional[str]
            Name of the block if it is a template.

        is_template : typing.Optional[bool]

        description : typing.Optional[str]
            Description of the block.

        metadata : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Metadata of the block.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Block
            Successful Response

        Examples
        --------
        import asyncio

        from letta_client import AsyncLetta

        client = AsyncLetta(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.blocks.create(
                value="value",
                label="label",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/blocks/",
            method="POST",
            json={
                "value": value,
                "limit": limit,
                "name": name,
                "is_template": is_template,
                "label": label,
                "description": description,
                "metadata_": metadata,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Block,
                    construct_type(
                        type_=Block,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, block_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Block:
        """
        Parameters
        ----------
        block_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Block
            Successful Response

        Examples
        --------
        import asyncio

        from letta_client import AsyncLetta

        client = AsyncLetta(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.blocks.get(
                block_id="block_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/blocks/{jsonable_encoder(block_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Block,
                    construct_type(
                        type_=Block,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, block_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Block:
        """
        Parameters
        ----------
        block_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Block
            Successful Response

        Examples
        --------
        import asyncio

        from letta_client import AsyncLetta

        client = AsyncLetta(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.blocks.delete(
                block_id="block_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/blocks/{jsonable_encoder(block_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Block,
                    construct_type(
                        type_=Block,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(
        self,
        block_id: str,
        *,
        value: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        is_template: typing.Optional[bool] = OMIT,
        label: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Block:
        """
        Parameters
        ----------
        block_id : str

        value : typing.Optional[str]
            Value of the block.

        limit : typing.Optional[int]
            Character limit of the block.

        name : typing.Optional[str]
            Name of the block if it is a template.

        is_template : typing.Optional[bool]
            Whether the block is a template (e.g. saved human/persona options).

        label : typing.Optional[str]
            Label of the block (e.g. 'human', 'persona') in the context window.

        description : typing.Optional[str]
            Description of the block.

        metadata : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Metadata of the block.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Block
            Successful Response

        Examples
        --------
        import asyncio

        from letta_client import AsyncLetta

        client = AsyncLetta(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.blocks.update(
                block_id="block_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/blocks/{jsonable_encoder(block_id)}",
            method="PATCH",
            json={
                "value": value,
                "limit": limit,
                "name": name,
                "is_template": is_template,
                "label": label,
                "description": description,
                "metadata_": metadata,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Block,
                    construct_type(
                        type_=Block,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def link_agent_memory_block(
        self, block_id: str, *, agent_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Link a memory block to an agent.

        Parameters
        ----------
        block_id : str

        agent_id : str
            The unique identifier of the agent to attach the source to.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from letta_client import AsyncLetta

        client = AsyncLetta(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.blocks.link_agent_memory_block(
                block_id="block_id",
                agent_id="agent_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/blocks/{jsonable_encoder(block_id)}/attach",
            method="PATCH",
            params={
                "agent_id": agent_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def unlink_agent_memory_block(
        self, block_id: str, *, agent_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Unlink a memory block from an agent

        Parameters
        ----------
        block_id : str

        agent_id : str
            The unique identifier of the agent to attach the source to.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from letta_client import AsyncLetta

        client = AsyncLetta(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.blocks.unlink_agent_memory_block(
                block_id="block_id",
                agent_id="agent_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/blocks/{jsonable_encoder(block_id)}/detach",
            method="PATCH",
            params={
                "agent_id": agent_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
