from functools import cached_property

from alloniaconfigs import Configs as BaseConfigs
from pydantic import UUID4, BaseModel, Field, HttpUrl

from .client import Client


class ConfigSchema(BaseModel):
    USER_TOKEN_ID: str = Field(min_length=16, max_length=16)
    USER_TOKEN_SECRET: str = Field(min_length=32, max_length=32)
    TRACK_ID: UUID4
    PROJECTS_API_INTERNAL_URL: HttpUrl


class Configs(BaseConfigs):
    schema = ConfigSchema

    @cached_property
    def projects_api_client(self):
        """Client to request the Projects API."""
        return Client(
            str(self.PROJECTS_API_INTERNAL_URL),
            user_token={
                "id": self.USER_TOKEN_ID,
                "token": self.USER_TOKEN_SECRET,
            },
            trace=False,
        )


def get_external_api_key_value(name):
    """Get the secret value of a saved external API key.

    Args:
        name: The name of the saved external API key.

    Returns: The str token value.
    """
    response = Configs.instance.projects_api_client.request(
        "GET",
        f"/external-api-tokens/tracks/{Configs.instance.TRACK_ID}/name/{name}",
    )
    response.raise_for_status()
    return response.json()["value"]
