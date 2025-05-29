import streamlit as st

def handle_button_click(button_name):
   st.session_state.last_action = button_name
   st.toast(f"{button_name} clicked!")




def handle_copy(data_type):
   st.toast(f"Copying {data_type} data...")




def clear_media(media_type):
   st.toast(f"Clearing {media_type} media...")




def handle_cleaning(action):
   st.toast(f"Performing {action} on D drive...")




def run_utility(utility_name):
   st.toast(f"Running utility: {utility_name}")