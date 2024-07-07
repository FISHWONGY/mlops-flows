import streamlit as st

from settings import app_config


# def creds_entered():
#     if (
#         st.session_state["user"].strip() == app_config.MLFLOW_TRACKING_USERNAME
#         and st.session_state["passwd"].strip() == app_config.MLFLOW_TRACKING_PASSWORD
#     ):
#         st.session_state["authenticated"] = True
#     else:
#         st.session_state["authenticated"] = False
#         if not st.session_state["user"]:
#             st.warning("Please enter a username")
#         elif not st.session_state["passwd"]:
#             st.warning("Please enter a password")
#         st.error("Invalid username or password")
#
#
# def authenticate_user():
#     if "authenticated" not in st.session_state:
#         st.text_input(label="Username: ", value="", key="user", on_change=creds_entered)
#         st.text_input(
#             label="Password: ",
#             value="",
#             key="passwd",
#             type="password",
#             on_change=creds_entered,
#         )
#         return False
#     else:
#         if st.session_state["authenticated"]:
#             return True
#         else:
#             st.text_input(
#                 label="Username: ", value="", key="user", on_change=creds_entered
#             )
#             st.text_input(
#                 label="Password: ",
#                 value="",
#                 key="passwd",
#                 type="password",
#                 on_change=creds_entered,
#             )
#             return False


def creds_entered():
    if (
        st.session_state["user"].strip() == app_config.MLFLOW_TRACKING_USERNAME
        and st.session_state["passwd"].strip() == app_config.MLFLOW_TRACKING_PASSWORD
    ):
        st.session_state["authenticated"] = True
    else:
        st.session_state["authenticated"] = False
        if not st.session_state["passwd"]:
            st.warning("Please enter a password")
        if not st.session_state["user"]:
            st.warning("Please enter a username")
        st.error("Invalid username or password")


def authenticate_user():
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False
    if "user" not in st.session_state:
        st.session_state["user"] = ""
    if "passwd" not in st.session_state:
        st.session_state["passwd"] = ""

    if not st.session_state["authenticated"]:
        st.text_input(label="Username: ", value=st.session_state["user"], key="user")
        st.text_input(
            label="Password: ",
            value=st.session_state["passwd"],
            key="passwd",
            type="password",
        )
        if st.button("Login"):
            creds_entered()
        return False
    else:
        return True
