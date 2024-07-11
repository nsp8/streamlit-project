import streamlit
from admin.logout import get_username_from_session

if "logged_in" not in streamlit.session_state:
    streamlit.session_state.logged_in = ""

if "user_sessions" not in streamlit.session_state:
    streamlit.session_state.user_sessions = dict()


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
    if get_username_from_session() == "nsp8":
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
            # TODO: add "delete user" page and logic when DB is integrated
            logout_page
        ]
    pages = streamlit.navigation(
        {
            "Visualization": [world_map_page, additional_page],
            "Account": account_management_pages,
        }
    )
    streamlit.set_page_config(
        page_title="Multi-page Streamlit App", page_icon="🚀"
    )
else:
    pages = streamlit.navigation({"Account": [login_page]})

pages.run()
