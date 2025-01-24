import base64
import binascii
import datetime as dt
from contextlib import suppress
from enum import Enum
from functools import cached_property
from typing import Annotated, Any, Optional, Union

from pydantic import (
    AliasChoices,
    BaseModel,
    BeforeValidator,
    ConfigDict,
    Field,
    HttpUrl,
    SecretStr,
    SerializationInfo,
    ValidationError,
    field_serializer,
    model_validator,
)

from earthscope_sdk import __version__


def _try_float(v: Any):
    try:
        return float(v)
    except (TypeError, ValueError):
        return v


Timedelta = Annotated[dt.timedelta, BeforeValidator(_try_float)]


class AccessTokenBody(BaseModel):
    """
    Access token payload

    [See Auth0 docs](https://auth0.com/docs/secure/tokens/access-tokens/access-token-profiles)
    """

    audience: Annotated[Union[str, list[str]], Field(alias="aud")]
    issuer: Annotated[str, Field(alias="iss")]
    issued_at: Annotated[dt.datetime, Field(alias="iat")]
    expires_at: Annotated[dt.datetime, Field(alias="exp")]
    scope: Annotated[str, Field(alias="scope")] = ""
    subject: Annotated[str, Field(alias="sub")]
    grant_type: Annotated[Optional[str], Field(alias="gty")] = None
    token_id: Annotated[Optional[str], Field(alias="jti")] = None
    client_id: Annotated[
        str,
        Field(
            validation_alias=AliasChoices("client_id", "azp"),
            serialization_alias="client_id",
        ),
    ]

    @cached_property
    def ttl(self) -> dt.timedelta:
        """time to live (TTL) until expiration"""
        return self.expires_at - dt.datetime.now(dt.timezone.utc)

    model_config = ConfigDict(extra="allow", frozen=True, populate_by_name=True)


class AuthFlowType(Enum):
    DeviceCode = "device_code"
    MachineToMachine = "m2m"


class Tokens(BaseModel):
    """
    EarthScope SDK oauth2 tokens
    """

    access_token: Optional[SecretStr] = None
    id_token: Optional[SecretStr] = None
    refresh_token: Optional[SecretStr] = None

    model_config = ConfigDict(frozen=True)

    @cached_property
    def access_token_body(self):
        if self.access_token is None:
            return None

        with suppress(IndexError, binascii.Error, ValidationError):
            payload_b64 = self.access_token.get_secret_value().split(".")[1]
            payload = base64.b64decode(payload_b64 + "==")  # extra padding
            return AccessTokenBody.model_validate_json(payload)

        raise ValueError("Unable to decode access token body")

    @field_serializer("access_token", "id_token", "refresh_token", when_used="json")
    def dump_secret_json(self, secret: Optional[SecretStr], info: SerializationInfo):
        """
        A special field serializer to dump the actual secret value when writing to JSON.

        Only writes secret in plaintext when `info.context == "plaintext".

        See [Pydantic docs](https://docs.pydantic.dev/latest/concepts/serialization/#serialization-context)
        """
        if secret is None:
            return None

        if info.context == "plaintext":
            return secret.get_secret_value()

        return str(secret)

    @model_validator(mode="after")
    def ensure_one_of(self):
        # allow all fields to be optional in subclasses
        if self.__class__ != Tokens:
            return self

        if self.access_token or self.refresh_token:
            return self

        raise ValueError("At least one of access token and refresh token is required.")


class AuthFlowSettings(Tokens):
    """
    Auth flow configuration

    Not for direct use.
    """

    # Auth parameters
    audience: str = "https://api.earthscope.org"
    domain: HttpUrl = HttpUrl("https://login.earthscope.org")
    client_id: str = "b9DtAFBd6QvMg761vI3YhYquNZbJX5G0"
    scope: str = "offline_access"
    client_secret: Optional[SecretStr] = None

    @cached_property
    def auth_flow_type(self) -> AuthFlowType:
        if self.client_secret is not None:
            return AuthFlowType.MachineToMachine

        return AuthFlowType.DeviceCode


class HttpSettings(BaseModel):
    """
    HTTP client configuration
    """

    # httpx limits
    keepalive_expiry: Timedelta = dt.timedelta(seconds=5)
    max_connections: Optional[int] = None
    max_keepalive_connections: Optional[int] = None

    # httpx timeouts
    timeout_connect: Timedelta = dt.timedelta(seconds=5)
    timeout_read: Timedelta = dt.timedelta(seconds=5)

    # Other
    user_agent: str = f"earthscope-sdk py/{__version__}"

    @cached_property
    def limits(self):
        """httpx Limits on client connection pool"""
        # lazy import
        import httpx

        return httpx.Limits(
            max_connections=self.max_connections,
            max_keepalive_connections=self.max_keepalive_connections,
            keepalive_expiry=self.keepalive_expiry.total_seconds(),
        )

    @cached_property
    def timeouts(self):
        """httpx Timeouts default behavior"""
        # lazy import
        import httpx

        return httpx.Timeout(
            connect=self.timeout_connect.total_seconds(),
            # reuse read timeout for others
            read=self.timeout_read.total_seconds(),
            write=self.timeout_read.total_seconds(),
            pool=self.timeout_read.total_seconds(),
        )


class ResourceRefs(BaseModel):
    """
    References to EarthScope resources
    """

    api_url: HttpUrl = HttpUrl("https://api.earthscope.org")
    """Base URL for api.earthscope.org"""


class SdkBaseSettings(BaseModel):
    """
    Common base class for SDK settings

    Not for direct use.
    """

    http: HttpSettings = HttpSettings()
    oauth2: AuthFlowSettings = AuthFlowSettings()
    resources: ResourceRefs = ResourceRefs()
