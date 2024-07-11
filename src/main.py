import streamlit

if "logged_in" not in streamlit.session_state:
    streamlit.session_state.logged_in = ""

if "user_sessions" not in streamlit.session_state:
    streamlit.session_state.user_sessions = dict()

from utils.user_manager import get_username_from_session

login_page = streamlit.Page(
    "admin/login.py", title="Log in", icon=":material/login:"
)

logout_page = streamlit.Page(
    "admin/logout.py", title="Log out", icon=":material/logout:"
)

world_map_page = streamlit.Page(
    "visualization/world_map.py", title="World Map", icon="🌎"
)

additional_page = streamlit.Page(
    "visualization/page_two.py", title="Additional", icon=":material/add_circle:"
)

if streamlit.session_state.logged_in:
    account_management_pages = [logout_page]
    user_control_page_name = "Account"
    if get_username_from_session() == "nsp8":
        user_control_page_name = "Account Management"
        account_management_pages = [
            streamlit.Page(
                "admin/add_user.py",
                title="Add User",
                icon=":material/person_add:"
            ),
            streamlit.Page(
                "admin/update_credentials.py",
                title="Update User",
                icon=":material/manage_accounts:"
            ),
            streamlit.Page(
                "admin/delete_user.py",
                title="Delete User",
                icon=":material/person_remove:"
            ),
            logout_page
        ]
    pages = streamlit.navigation(
        {
            "Visualization": [world_map_page, additional_page],
            user_control_page_name: account_management_pages,
        }
    )
    streamlit.set_page_config(
        page_title="Data Tool", page_icon="🚀"
    )
else:
    pages = streamlit.navigation({"Account": [login_page]})

pages.run()
