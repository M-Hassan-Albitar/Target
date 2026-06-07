import streamlit as st
import hashlib
from arabic_support import support_arabic_text
import customers
from pages.branches_homepages import abha_main, albaha_main, jazan_main, khamis_main, najran_main
import os
from dotenv import load_dotenv
from whatsSender import whats_sender

load_dotenv()
# Data
ABHA_CSV_URL = os.getenv("ABHA_CSV_URL")
ALBAHA_CSV_URL = os.getenv("ALBAHA_CSV_URL")
JAZAN_CSV_URL = os.getenv("JAZAN_CSV_URL")
KHAMIS_CSV_URL = os.getenv("KHAMIS_CSV_URL")
NAJRAN_CSV_URL = os.getenv("NAJRAN_CSV_URL")

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

    st.markdown("### 🎉 تم تسجيل الدخول إلى النظام")

    # Example protected content
    match st.session_state.username:
        case "Ka":

            main_page = st.Page(abha_main, title="الصفحة الرئيسية")
            analyze_page = st.Page(lambda: customers.c_analyze(ABHA_CSV_URL), title="العملاء")

            # Create navigation and run it
            pg = st.navigation([main_page, analyze_page])
            pg.run()

        case "L":
            main_page = st.Page(albaha_main, title="الصفحة الرئيسية")
            analyze_page = st.Page(lambda: customers.c_analyze(ALBAHA_CSV_URL), title="العملاء")

            # Create navigation and run it
            pg = st.navigation([main_page, analyze_page])
            pg.run()
        case "G":
            main_page = st.Page(jazan_main, title="الصفحة الرئيسية")
            analyze_page = st.Page(lambda: customers.c_analyze(JAZAN_CSV_URL), title="العملاء")

            # Create navigation and run it
            pg = st.navigation([main_page, analyze_page])
            pg.run()
        case "Kb":
            main_page = st.Page(khamis_main, title="الصفحة الرئيسية")
            analyze_page = st.Page(lambda: customers.c_analyze(KHAMIS_CSV_URL), title="العملاء")
            whatsapp_page = st.Page(whats_sender, title="رسائل لتسليم الثياب")
            # Create navigation and run it
            pg = st.navigation([main_page, analyze_page, whatsapp_page])
            pg.run()
        case "W":
            main_page = st.Page(najran_main, title="الصفحة الرئيسية")
            analyze_page = st.Page(lambda: customers.c_analyze(NAJRAN_CSV_URL), title="العملاء")

            # Create navigation and run it
            pg = st.navigation([main_page, analyze_page])
            pg.run()

    # Logout button
    if st.button("تسجيل الخروج"):
        logout()

        st.rerun()
