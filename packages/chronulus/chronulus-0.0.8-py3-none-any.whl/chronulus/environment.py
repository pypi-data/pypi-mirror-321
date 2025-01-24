import os
from importlib import resources

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


def get_default_env_path():
    """
    Get the path to the default environment file in the package.

    Returns
    -------
    str
        The absolute path to the default.env file.
    """
    # Get the package directory
    for file in resources.files("chronulus.etc").iterdir():
        if file.is_file() and file.name == 'default.env':
            return str(file)


class Env(BaseSettings):
    """
    Environment settings class for managing API configuration.

    This class handles environment variables and configuration for the Chronulus API,
    with support for loading from environment files.

    Attributes
    ----------
    API_URI : str
        The URI for the Chronulus API endpoint.
    CHRONULUS_API_KEY : str or None
        The API key for authentication. Defaults to the value in CHRONULUS_API_KEY
        environment variable.

    Notes
    -----
    Configuration is loaded from environment files in order of precedence,
    with the default.env file serving as the base configuration.
    """
    API_URI: str
    CHRONULUS_API_KEY: str | None = Field(default=os.environ.get("CHRONULUS_API_KEY"))

    model_config = SettingsConfigDict(
        env_file=(
            # List them in order of precedence (last one wins)
            get_default_env_path()
        ),
        # Optional: Use case-sensitive names (default is case-insensitive)
        case_sensitive=True,
    )


def get_default_headers(env: Env):
    """
    Generate default headers for API requests.

    Parameters
    ----------
    env : Env
        The environment settings instance containing the API key.

    Returns
    -------
    dict
        A dictionary containing the X-API-Key header with the API key.
    """
    return {'X-API-Key': env.CHRONULUS_API_KEY}


class BaseEnv:
    """
    Base class for environment-aware components.

    This class provides basic environment configuration and header management
    for API interactions.

    Parameters
    ----------
    **kwargs
        Keyword arguments to pass to the Env initialization.

    Attributes
    ----------
    env : Env
        The environment settings instance.
    headers : dict
        Default headers for API requests, including authentication.
    """

    def __init__(self, **kwargs):
        self.env = Env(**kwargs)
        self.headers = get_default_headers(self.env)
