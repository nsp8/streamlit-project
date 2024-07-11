from pathlib import Path
from time import sleep

import streamlit
from streamlit_authenticator.utilities.hasher import Hasher
import yaml


def hash_generator(secret: str) -> str:
    return Hasher([secret]).generate()[0]


def update_credentials():
    with streamlit.form("update_user_credentials"):
        streamlit.write("Update User Credentials")
        updated_user = dict()
        username = streamlit.text_input("Enter username: ")
        secret = streamlit.text_input("Enter your secret: ", type="password")
        if streamlit.form_submit_button("Compute"):

            with open(Path("src/admin/credentials.yaml")) as f:
                config = yaml.load(f, Loader=yaml.loader.SafeLoader)
                updated_user = config["credentials"]["usernames"].get(username)
                if updated_user:
                    updated_user["password"] = hash_generator(secret)
                    config["credentials"]["usernames"][username] = updated_user
                else:
                    streamlit.error(f"User '{username}' does not exist!")
            if updated_user:
                with open(Path("src/admin/credentials.yaml"), "w") as f:
                    yaml.dump(config, f)
                # TODO: save hash instead of saving in the file!
                with streamlit.spinner("Updating credentials ..."):
                    sleep(1)
                    streamlit.success("User credentials have been updated!")
                    sleep(2)
                streamlit.switch_page(streamlit.Page("main.py"))


update_credentials()
