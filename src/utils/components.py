from time import sleep
import streamlit


def show_success_spinner(spinner_text: str, success_message: str) -> None:
    with streamlit.spinner(spinner_text):
        sleep(1)
        streamlit.success(success_message)
        sleep(2)


def show_header(header_text: str = "Data Tool") -> None:
    streamlit.header(header_text, divider="rainbow")
