from typing import Optional

import requests

from .environment import BaseEnv, Env, get_default_headers


class Session(BaseEnv):
    """
    A class to manage API sessions for handling specific situations and tasks.

    Parameters
    ----------
    name : str
        The name identifier for the session.
    situation : str
        The context or situation description for the session.
    task : str
        The task to be performed in this session.
    session_id : str, optional
        Unique identifier for an existing session. If None, a new session will be created.
    env : dict, optional
        Environment configuration dictionary. If None, default environment will be used.

    Attributes
    ----------
    session_version : str
        Version string for the Session. Set to "1".
    name : str
        The name identifier for the session.
    situation : str
        The context or situation description.
    task : str
        The task description.
    session_id : str
        Unique identifier for the session.
    """

    session_version = "1"

    def __init__(self, name: str, situation: str, task: str, session_id: Optional[str] = None, env: Optional[dict] = None):
        super().__init__(**(env if env and isinstance(env, dict) else {}))

        self.name = name
        self.situation = situation
        self.task = task
        self.session_id = session_id

        if self.session_id is None:
            self.create()

    def create(self):
        """
        Create a new session using the API.

        This method sends a POST request to create a new session with the specified
        name, situation, and task. Upon successful creation, the session_id is
        updated with the response from the API.

        Raises
        ------
        Exception
            If the API key is invalid or not active (403 status code).
            If the session creation fails with any other status code.
        """

        resp = requests.post(
            url=f"{self.env.API_URI}/sessions/{self.session_version}/create",
            headers=self.headers,
            json=dict(
                name=self.name,
                situation=self.situation,
                task=self.task,
                session_id=self.session_id,
            )
        )
        response_json = resp.json()
        if resp.status_code != 200:
            if resp.status_code == 403:
                raise Exception("Failed to create session. API Key is not valid or not yet active. Please allow up to 1 minute for activation of new keys.")
            else:
                raise Exception(f"Failed to create session with status code: {resp.status_code}")
        else:
            self.session_id = response_json['session_id']
            print(f"Session created with session_id: {response_json['session_id']}")

    @staticmethod
    def load_from_saved_session(session_id: str, env: Optional[dict] = None):
        """
        Load an existing session using a session ID.

        Parameters
        ----------
        session_id : str
            The unique identifier of the session to load.
        env : dict, optional
            Environment configuration dictionary. If None, default environment will be used.

        Returns
        -------
        Session
            A new Session instance initialized with the saved session data.

        Raises
        ------
        ValueError
            If the session loading fails or if the response cannot be parsed.
        """
        env = Env(**env) if env and isinstance(env, dict) else Env()
        headers = get_default_headers(env)

        resp = requests.post(
            url=f"{env.API_URI}/sessions/from-session-id",
            headers=headers,
            json=dict(session_id=session_id)
        )

        if resp.status_code != 200:
            raise ValueError(f"Failed to create session with status code: {resp.status_code}, {resp.text}")

        try:
            response_json = resp.json()
            return Session(**response_json)

        except Exception as e:
            raise ValueError(f"Failed to parse session response: {resp.text}")



