from dataclasses import dataclass
from datetime import datetime as dt
from uuid import uuid4

import streamlit
from streamlit_authenticator.utilities.hasher import Hasher

from utils.components import show_header
from utils.file_io import read_config


@dataclass
class UserSession:
    username: str
    session_id: str
    last_login: dt
    login_attempts: int = 0
    authenticated: bool = False


def authenticate(username: str, password: str) -> None:
    """Authenticates entered username and password"""
    config = read_config()
    if config:
        users = config["credentials"]["usernames"]
        try:
            user_secret = users[username]["password"]
            add_to_session(username)
            if Hasher.check_pw(password, user_secret):
                user_session = streamlit.session_state.user_sessions[username]
                user_session.login_attempts = 0
                user_session.authenticated = True
                streamlit.session_state.logged_in = user_session.session_id
                streamlit.toast("Login successful!", icon="✅")
                streamlit.rerun()
            else:
                streamlit.session_state.user_sessions.pop(username)
                streamlit.toast("Invalid credentials. Please try again.")
        except KeyError:
            streamlit.toast("Invalid credentials. Please try again.")
        except AttributeError as e:
            streamlit.error(f"Something went horribly wrong ...{e}")


def add_to_session(username: str) -> None:
    """Adds UserSession object to the Streamlit session state"""
    try:
        user_sessions = streamlit.session_state.user_sessions
        if not user_sessions:
            user_sessions[username] = UserSession(
                username=username,
                session_id=uuid4().hex,
                last_login=dt.now(),
                login_attempts=1
            )
        else:
            if username in user_sessions and not user_sessions[username].authenticated:
                user_sessions[username].login_attempts += 1
    except AttributeError:
        streamlit.error("Session state wasn't initialised properly")


def login():
    """Form to log a user in with a username and password"""
    show_header()
    with streamlit.form("login_form"):
        streamlit.write("Login")
        username = streamlit.text_input("Username")
        password = streamlit.text_input("Password", type="password")
        if streamlit.form_submit_button("Login"):
            authenticate(username, password)


login()
