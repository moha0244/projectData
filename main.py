import streamlit as st
from utility import handle_button_click, handle_copy, clear_media, handle_cleaning, run_utility
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide", page_title="TTC Data Manager", initial_sidebar_state="expanded")

# Sidebar navigation
with st.sidebar:
    selected = option_menu(
        "Navigation",
        ["Main", "Copy Data", "Clear Media", "Clean D Drive", "Utilities"],
        icons=["house", "cloud-upload", "trash", "cpu", "tools"],
        menu_icon="cast",
        default_index=0,
    )
    st.markdown("""
            <style>
            div.stButton > button:first-child {
                height: 3em;
                width: 100%;
                font-size: 18px;
                margin-top: 10px;
                margin-bottom: 10px;
            }
            </style>
        """, unsafe_allow_html=True)
# Main Tab
if selected == "Main":
    st.title("Main Controls")
    col1, col2 = st.columns(2)

    with col1:

        ftv = st.selectbox(" Select FTV:", ["50002", "55001"], index=1)
        test_type = st.selectbox(" Select Test Type:", ["F", "R", "S", "T"], index=0)
        test_number = st.text_input("Test Number:", max_chars=4)

        if test_number and not test_number.isdigit():
            st.warning("Please enter only numbers")
            test_number = ""

        test_info = f"{ftv}{test_type}{test_number}"
        st.text_input(" Full Test Info:", value=test_info, disabled=True)

    with col2:
        st.markdown("### Actions")
        if st.button("Validate Test"):
            if test_number and len(test_number) == 4:
                st.success(f"Test {test_info} validated!")
            else:
                st.error("Please enter a 4-digit test number")

        button_list = [
            "Autocopy", "Check Local Data", "Launch DTS", "Launch Media Manager",
            "RAW data verify", "Data space check", "Launch TTP App", "Create Local Folder"
        ]
        for i in range(0, len(button_list), 2):
            c1, c2 = st.columns(2)
            with c1:
                if st.button(button_list[i]):
                    handle_button_click(button_list[i])
            with c2:
                if i + 1 < len(button_list) and st.button(button_list[i+1]):
                    handle_button_click(button_list[i+1])

# Copy Data
elif selected == "Copy Data":
    st.title("Data Copy Operations")
    col1, col2 = st.columns(2)
    with col1:
        if st.button(" Copy TTP Data"):
            handle_copy("TTP")
        if st.button(" Copy AFDX Files"):
            handle_copy("AFDX")
    with col2:
        if st.button("Copy IADS Data"):
            handle_copy("IADS")
        if st.button(" Copy Video Files"):
            handle_copy("Video")

# Clear Media
elif selected == "Clear Media":
    st.title(" Media Clearing")
    col1, col2 = st.columns(2)
    with col1:
        if st.button(" Clear IADS Disk"):
            clear_media("IADS")
        if st.button(" Clear Video Disk"):
            clear_media("Video")
    with col2:
        if st.button("Clear AFDX Drive"):
            clear_media("AFDX")
        if st.button(" Clear TTP Disk"):
            clear_media("TTP")

# Clean D Drive
elif selected == "Clean D Drive":
    st.title(" Clean D Drive")
    col1, col2 = st.columns(2)
    with col1:
        ftv = st.selectbox(" Select FTV:", ["50002", "55001", "55332", "55329"], index=1)
        test_type = st.selectbox(" Select Test Type:", ["F", "R", "S", "T"], index=0)
        test_number = st.text_input(" Test Number:", max_chars=4, key="clean_test_number")

        if test_number and not test_number.isdigit():
            st.warning("Please enter only numbers")
            test_number = ""

        test_info = f"{ftv}{test_type}{test_number}"
        st.text_input(" Full Test Info:", value=test_info, disabled=True, key="clean_test_info")

    with col2:
        if st.button(" Validate Test", key="validate_clean"):
            if test_number and len(test_number) == 4:
                st.success(f"Test {test_info} validated!")
            else:
                st.error("Please enter a 4-digit test number")

        # Cleaning buttons
        cleaning_buttons = [
            "Clear All", "Clear RAW", "Clear AFDX", "Clear Video",
            "Clear IADS", "Clear TTP", "Clear Other", "ClearFolder"
        ]
        for i in range(0, len(cleaning_buttons), 2):
            c1, c2 = st.columns(2)
            with c1:
                if st.button(cleaning_buttons[i], key=f"clean_{i}"):
                    handle_cleaning(cleaning_buttons[i])
            with c2:
                if i + 1 < len(cleaning_buttons):
                    if st.button(cleaning_buttons[i+1], key=f"clean_{i+1}"):
                        handle_cleaning(cleaning_buttons[i+1])

# Utility Functions
elif selected == "Utilities":
    st.title("Utility Functions")
    col1, col2 = st.columns(2)
    utilities_col1 = ["Create ICR", "GetXML from TTC Zip", "Compare MAP-ADASNO", "Compare 2 folders", "IADS test_info"]
    utilities_col2 = ["Extract Video subfiles", "Group Video files", "Change Video timestamp", "New Button 4", "New Button 5"]

    for i in range(len(utilities_col1)):
        with col1:
            if st.button(utilities_col1[i]):
                run_utility(utilities_col1[i])
        with col2:
            if i < len(utilities_col2):
                if st.button(utilities_col2[i]):
                    run_utility(utilities_col2[i])
