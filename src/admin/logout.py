import streamlit


def get_username_from_session():
    for user, session in streamlit.session_state.user_sessions.items():
        if session.session_id == streamlit.session_state.logged_in:
            return user
    return None


def logout():
    # if streamlit.button("Log out"):
    try:
        username = get_username_from_session()
        streamlit.session_state.user_sessions.pop(username)
        streamlit.session_state.logged_in = ""
    except KeyError:
        streamlit.error(f"Invalid session state. Please reload.")
    else:
        streamlit.rerun()


logout()
