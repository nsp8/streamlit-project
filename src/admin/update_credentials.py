import streamlit

from utils.components import show_header, show_success_spinner
from utils.file_io import read_config, update_config
from utils.user_manager import hash_generator


def update_credentials():
    """Form to update user credentials"""
    show_header("User management")
    with streamlit.form("update_user_credentials"):
        streamlit.write("Update User Credentials")
        username = streamlit.text_input("Enter username: ")
        secret = streamlit.text_input("Enter your secret: ", type="password")
        if streamlit.form_submit_button("Update User"):
            if len(secret) < 8:
                streamlit.warning("Password can't be less than 8 characters")
            else:
                config = read_config()
                updated_user = dict()
                if config:
                    updated_user = config["credentials"]["usernames"].get(username)
                    if updated_user:
                        updated_user["password"] = hash_generator(secret)
                        config["credentials"]["usernames"][username] = updated_user
                    else:
                        streamlit.error(f"User '{username}' does not exist!")
                if updated_user:
                    update_config(config)
                    # TODO: save hash instead of saving in the file!
                    show_success_spinner(
                        "Updating credentials ...",
                        "User credentials have been updated!"
                    )
                    streamlit.switch_page(streamlit.Page("main.py"))


update_credentials()
