from copy import deepcopy

import streamlit

from utils.file_io import read_config, update_config
from utils.components import show_header, show_success_spinner
from utils.user_manager import get_username_from_session


def delete_user():
    show_header("User management")
    with streamlit.form("delete_user_form"):
        streamlit.write("Delete User")
        username = streamlit.text_input("Username", max_chars=20)
        if streamlit.form_submit_button("Delete User"):
            if username != get_username_from_session():
                config = read_config()
                if config:
                    if username not in config["credentials"]["usernames"]:
                        streamlit.warning(f"User '{username}' does not exist.")
                    else:
                        updated_config = deepcopy(config)
                        updated_config["credentials"]["usernames"].pop(username)
                        update_config(updated_config)
                        show_success_spinner("Deleting user...", "User has been deleted!")
                        streamlit.switch_page(streamlit.Page("main.py"))
            else:
                streamlit.warning("User can't be deleted")


delete_user()
