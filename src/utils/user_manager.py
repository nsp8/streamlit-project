import streamlit
from streamlit_authenticator.utilities.hasher import Hasher


def get_username_from_session():
    for user, session in streamlit.session_state.user_sessions.items():
        if session.session_id == streamlit.session_state.logged_in:
            return user
    return None


def hash_generator(secret: str) -> str:
    return Hasher([secret]).generate()[0]
