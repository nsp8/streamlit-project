from pathlib import Path
from time import sleep
import re

from streamlit_authenticator.utilities.hasher import Hasher
import streamlit
import yaml


def hash_generator(secret: str) -> str:
    return Hasher([secret]).generate()[0]


def validate_fields(email, password, re_entered_password) -> bool:
    email_pattern = r"(.*)@(gmail|outlook|hotmail|yahoo)\.(com)$"
    email_valid = password_strength = passwords_match = True
    if not re.search(email_pattern, email):
        streamlit.warning("Email address doesn't seem valid")
        email_valid = False
    if len(password) < 8:
        streamlit.warning("Password can't be less than 8 characters")
        password_strength = False
    if password != re_entered_password:
        streamlit.warning("Passwords do not match")
        passwords_match = False
    return email_valid and password_strength and passwords_match


def update_credentials(
    username: str,
    email_address: str,
    name: str,
    hashed_password: str
):
    is_user_new = False
    with open(Path("src/admin/credentials.yaml")) as f:
        config = yaml.load(f, Loader=yaml.loader.SafeLoader)
        if username not in config["credentials"]["usernames"]:
            new_user = {
                "email": email_address,
                "name": name,
                "password": hashed_password
            }
            config["credentials"]["usernames"][username] = new_user
            is_user_new = True

    if is_user_new:
        with open(Path("src/admin/credentials.yaml"), "w") as f:
            yaml.dump(config, f)
    else:
        streamlit.warning("User already exists!")
    return is_user_new


def add_user_form():
    with streamlit.form("new_user_form"):
        streamlit.write("Add New User")
        name = streamlit.text_input("Full name", max_chars=50)
        username = streamlit.text_input("Username", max_chars=20)
        email = streamlit.text_input("Email address")
        password = streamlit.text_input(
            "Password", type="password", help="Password should be at least 8 characters"
        )
        re_password = streamlit.text_input(
            "Re-enter password", type="password"
        )
        if streamlit.form_submit_button(
            "Add User",
            args=(email, password, re_password)
        ) and validate_fields(email, password, re_password):
            if update_credentials(username, email, name, hash_generator(password)):
                with streamlit.spinner("Adding credentials ..."):
                    sleep(1)
                    streamlit.success("User has been created!")
                    sleep(2)
                streamlit.switch_page(streamlit.Page("main.py"))


add_user_form()
