import streamlit as st
import pandas as pd
import base64


# Set background GIF
def set_bg_gif(gif_file):
    import base64
    with open(gif_file, "rb") as f:
        data_url = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/gif;base64,{data_url}");
            background-repeat: no-repeat;
            background-size: cover;
            background-position: center center;
            background-attachment: fixed;
        }}

        @media only screen and (max-width: 768px) {{
            .stApp {{
                background-size: cover;
                background-position: top;
                background-attachment: scroll;
            }}
        }}
        </style>
        """,
        unsafe_allow_html=True
    )



# Apply background
set_bg_gif("background.gif")

# Title
st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("\n\n<h1 style='text-align: center; color: white;'>We cordially invite you to the Civil Get Away - 2025</h1>", unsafe_allow_html=True)

# Load Excel
try:
    df = pd.read_excel("Trial today.xlsx", engine="openpyxl")
except FileNotFoundError:
    st.error("Excel file not found!")

# Input field
emp_id = st.text_input("Enter Employee ID")

# Search
if st.button("Search"):
    if emp_id.strip() == "":
        st.warning("Please enter an Employee ID.")
    else:
        df["Employee_ID"] = df["Employee_ID"].astype(str)
        result = df[df["Employee_ID"] == emp_id.strip()]

        if not result.empty:
            emp_name = result.iloc[0]["Employee_Name"]
            team = result.iloc[0]["Team_Name"]
            st.success(f"Employee Name: {emp_name}\n\nTeam: {team}")
        else:
            st.error("No employee found with this ID.")
