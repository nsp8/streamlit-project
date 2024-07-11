from time import sleep
import streamlit


def show_success_spinner(spinner_text: str, success_message: str) -> None:
    """
    Show spinner with a text message on successful action
    :param spinner_text: text to show alongside spinner
    :param success_message: text to show message below the spinner
    :return:
    """
    with streamlit.spinner(spinner_text):
        sleep(1)
        streamlit.success(success_message)
        sleep(2)


def show_header(header_text: str = "Data Tool") -> None:
    """Show header of the page"""
    streamlit.header(header_text, divider="rainbow")
