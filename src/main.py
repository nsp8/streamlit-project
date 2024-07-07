import streamlit

world_map_page = streamlit.Page(
    "visualization/world_map.py", title="World Map", icon="🌎"
)

additional_page = streamlit.Page(
    "visualization/page_two.py", title="Additional", icon=":material/add_circle:"
)
pages = streamlit.navigation([world_map_page, additional_page])
streamlit.set_page_config(
    page_title="Multi-page Streamlit App", page_icon="🚀"
)
pages.run()
