import streamlit

from utils.user_manager import get_username_from_session


def logout():
    """Logout control"""
    try:
        username = get_username_from_session()
        streamlit.session_state.user_sessions.pop(username)
        streamlit.session_state.logged_in = ""
    except KeyError:
        streamlit.error(f"Invalid session state. Please reload.")
    else:
        streamlit.rerun()


logout()
