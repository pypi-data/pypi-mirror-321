# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.provider import Provider
from ..core.unchecked_base_model import construct_type
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ProvidersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_providers(
        self,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Provider]:
        """
        Get a list of all custom providers in the database

        Parameters
        ----------
        cursor : typing.Optional[str]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Provider]
            Successful Response

        Examples
        --------
        from letta_client import Letta

        client = Letta(
            token="YOUR_TOKEN",
        )
        client.providers.list_providers()
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/providers/",
            method="GET",
            params={
                "cursor": cursor,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[Provider],
                    construct_type(
                        type_=typing.List[Provider],  # type: ignore
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

    def create_provider(
        self, *, name: str, api_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Provider:
        """
        Create a new custom provider

        Parameters
        ----------
        name : str
            The name of the provider.

        api_key : str
            API key used for requests to the provider.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Provider
            Successful Response

        Examples
        --------
        from letta_client import Letta

        client = Letta(
            token="YOUR_TOKEN",
        )
        client.providers.create_provider(
            name="name",
            api_key="api_key",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/providers/",
            method="POST",
            json={
                "name": name,
                "api_key": api_key,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Provider,
                    construct_type(
                        type_=Provider,  # type: ignore
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

    def update_provider(
        self, *, id: str, api_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Provider:
        """
        Update an existing custom provider

        Parameters
        ----------
        id : str
            The id of the provider to update.

        api_key : str
            API key used for requests to the provider.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Provider
            Successful Response

        Examples
        --------
        from letta_client import Letta

        client = Letta(
            token="YOUR_TOKEN",
        )
        client.providers.update_provider(
            id="id",
            api_key="api_key",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/providers/",
            method="PUT",
            json={
                "id": id,
                "api_key": api_key,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Provider,
                    construct_type(
                        type_=Provider,  # type: ignore
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

    def delete_provider(
        self, *, provider_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.Any]:
        """
        Delete an existing custom provider

        Parameters
        ----------
        provider_id : str
            The provider_id key to be deleted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.Any]
            Successful Response

        Examples
        --------
        from letta_client import Letta

        client = Letta(
            token="YOUR_TOKEN",
        )
        client.providers.delete_provider(
            provider_id="provider_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/providers/",
            method="DELETE",
            params={
                "provider_id": provider_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.Optional[typing.Any],
                    construct_type(
                        type_=typing.Optional[typing.Any],  # type: ignore
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


class AsyncProvidersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_providers(
        self,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Provider]:
        """
        Get a list of all custom providers in the database

        Parameters
        ----------
        cursor : typing.Optional[str]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Provider]
            Successful Response

        Examples
        --------
        import asyncio

        from letta_client import AsyncLetta

        client = AsyncLetta(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.providers.list_providers()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/providers/",
            method="GET",
            params={
                "cursor": cursor,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[Provider],
                    construct_type(
                        type_=typing.List[Provider],  # type: ignore
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

    async def create_provider(
        self, *, name: str, api_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Provider:
        """
        Create a new custom provider

        Parameters
        ----------
        name : str
            The name of the provider.

        api_key : str
            API key used for requests to the provider.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Provider
            Successful Response

        Examples
        --------
        import asyncio

        from letta_client import AsyncLetta

        client = AsyncLetta(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.providers.create_provider(
                name="name",
                api_key="api_key",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/providers/",
            method="POST",
            json={
                "name": name,
                "api_key": api_key,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Provider,
                    construct_type(
                        type_=Provider,  # type: ignore
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

    async def update_provider(
        self, *, id: str, api_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Provider:
        """
        Update an existing custom provider

        Parameters
        ----------
        id : str
            The id of the provider to update.

        api_key : str
            API key used for requests to the provider.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Provider
            Successful Response

        Examples
        --------
        import asyncio

        from letta_client import AsyncLetta

        client = AsyncLetta(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.providers.update_provider(
                id="id",
                api_key="api_key",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/providers/",
            method="PUT",
            json={
                "id": id,
                "api_key": api_key,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Provider,
                    construct_type(
                        type_=Provider,  # type: ignore
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

    async def delete_provider(
        self, *, provider_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.Any]:
        """
        Delete an existing custom provider

        Parameters
        ----------
        provider_id : str
            The provider_id key to be deleted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.Any]
            Successful Response

        Examples
        --------
        import asyncio

        from letta_client import AsyncLetta

        client = AsyncLetta(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.providers.delete_provider(
                provider_id="provider_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/providers/",
            method="DELETE",
            params={
                "provider_id": provider_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.Optional[typing.Any],
                    construct_type(
                        type_=typing.Optional[typing.Any],  # type: ignore
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
