import streamlit as st
import hashlib
from arabic_support import support_arabic_text
from dashboard import render_target_dashboard, show_chart
import pandas as pd
from datetime import datetime

# import matplotlib
# matplotlib.use('TkAgg')  # Or 'QtAgg' 'TkAgg'
# import matplotlib.pyplot as plt

# Style = .streamlit/config.toml

# Data
DATA_URL = "https://docs.google.com/spreadsheets/d/"
SHEET_ID = "1Tpy43YMZbZctCq9a0NNrx1jMTJcRsOoDiYMVnj73r64"

# Arabic Support
support_arabic_text()

# ---------------------------
# RTL + input alignment CSS
# ---------------------------
st.markdown("""
    <style>
    body {
        direction: rtl;
        text-align: right;
    }

    /* Align text inside input fields */
    .stTextInput input {
        text-align: right;
    }

    /* Align labels */
    h3, label {
        text-align: right !important;
        width: 100%;
    }

    /* Button alignment */
    .stButton button {
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# Date and time
# Get current date and time
now = datetime.now()
today_date = now.strftime("%A, %d/%m/%Y")
today = now.strftime("%d")
month_name = now.strftime("%m-%Y")
current_time = now.strftime("%H:%M:%S")

# Get data
df = pd.read_csv(DATA_URL + SHEET_ID + "/export?format=csv")


# ---------------------------
# Fake database (replace later)
# ---------------------------
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


USERS_DB = {
    "admin": hash_password("1234"),
    "user1": hash_password("pass"),
    "Ka": hash_password("M1"),
    "L": hash_password("Y5"),
    "G": hash_password("A3"),
    "Kb": hash_password("H2"),
    "W": hash_password("A4"),
}

# ---------------------------
# Session state init
# ---------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""


# ---------------------------
# Login function
# ---------------------------
def login(username, password):
    hashed = hash_password(password)
    if username in USERS_DB and USERS_DB[username] == hashed:
        st.session_state.logged_in = True
        st.session_state.username = username
        return True
    return False


# ---------------------------
# Logout function
# ---------------------------
def logout():
    st.session_state.logged_in = False
    st.session_state.username = ""


# ---------------------------
# UI
# ---------------------------
st.set_page_config(page_title="الفاخرة - المنطقة الجنوبية", layout="centered")

if not st.session_state.logged_in:
    # Title
    st.markdown(
        "<h2 style='text-align: center;'>الفاخرة للخياطة الرجالية - المنطقة الجنوبية</h2>",
        unsafe_allow_html=True
    )

    st.write("")

    # Login form
    with st.form("login_form"):
        username = st.text_input("اسم المستخدم :")
        password = st.text_input("كلمة المرور :", type="password")
        submit = st.form_submit_button("دخول")

    if submit:
        if login(username, password):
            st.success("تم تسجيل الدخول بنجاح")
            st.rerun()
        else:
            st.error("اسم المستخدم أو كلمة المرور غير صحيحة")

else:
    # Logged-in view
    st.success(f"مرحباً، {st.session_state.username}")

    st.markdown("<h3>### 🎉 تم تسجيل الدخول إلى النظام</h3>", unsafe_allow_html=True, )

    # Example protected content
    match st.session_state.username:
        case "Ka":
            st.divider()
            render_target_dashboard(
                month_name=month_name,
                target=int(df.loc[df["Branches"] == "ABHA", "Target"].iloc[0].replace(",", "")),
                achieved=int(df.loc[df["Branches"] == "ABHA", "Achieved"].iloc[0].replace(",", "")),
            )
            show_chart(old_df_name=df, branch_name="ABHA")
        case "L":
            st.divider()
            render_target_dashboard(
                month_name=month_name,
                target=int(df.loc[df["Branches"] == "ALBAHA", "Target"].iloc[0].replace(",", "")),
                achieved=int(df.loc[df["Branches"] == "ALBAHA", "Achieved"].iloc[0].replace(",", "")),
            )

            show_chart(old_df_name=df, branch_name="ALBAHA")
        case "G":
            st.divider()
            render_target_dashboard(
                month_name=month_name,
                target=int(df.loc[df["Branches"] == "JAZAN", "Target"].iloc[0].replace(",", "")),
                achieved=int(df.loc[df["Branches"] == "JAZAN", "Achieved"].iloc[0].replace(",", "")),
            )

            show_chart(old_df_name=df, branch_name="JAZAN")
        case "Kb":
            st.divider()
            render_target_dashboard(
                month_name=month_name,
                target=int(df.loc[df["Branches"] == "KHAMIS", "Target"].iloc[0].replace(",", "")),
                achieved=int(df.loc[df["Branches"] == "KHAMIS", "Achieved"].iloc[0].replace(",", "")),
            )

            show_chart(old_df_name=df, branch_name="KHAMIS")
        case "W":
            st.divider()
            render_target_dashboard(
                month_name=month_name,
                target=int(df.loc[df["Branches"] == "NAJRAN", "Target"].iloc[0].replace(",", "")),
                achieved=int(df.loc[df["Branches"] == "NAJRAN", "Achieved"].iloc[0].replace(",", "")),
            )

            show_chart(old_df_name=df, branch_name="NAJRAN")

    # Logout button
    if st.button("تسجيل الخروج"):
        logout()
        st.rerun()
