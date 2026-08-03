import time
import streamlit as st
from streamlit_autorefresh import st_autorefresh
from datetime import datetime
from dashboard import render_target_dashboard, show_chart
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
# Get data
MAIN_DATA_URL = os.getenv("MAIN_DATA_URL")


def load_data():
    fresh_url = f"{MAIN_DATA_URL}&t={int(time.time())}"
    return pd.read_csv(fresh_url)


st_autorefresh(interval=10000, key="refresh")

# Date and time
# Get current date and time
now = datetime.now()
today_date = now.strftime("%A, %d/%m/%Y")
today = now.strftime("%d")
month_name = now.month
current_time = now.strftime("%H:%M:%S")


# ===============================
#   ABHA main page
# ===============================
def abha_main():
    df = load_data()
    st.divider()
    render_target_dashboard(
        month_name=month_name,
        target=int(df.loc[df["Branches"] == "ABHA", "Target"].iloc[0].replace(",", "")),
        achieved=int(df.loc[df["Branches"] == "ABHA", "Achieved"].iloc[0].replace(",", "")),
    )
    show_chart(old_df_name=df, branch_name="ABHA")


# ===============================
#   ALBAHA main page
# ===============================
def albaha_main():
    df = load_data()
    st.divider()
    render_target_dashboard(
        month_name=month_name,
        target=int(df.loc[df["Branches"] == "ALBAHA", "Target"].iloc[0].replace(",", "")),
        achieved=int(df.loc[df["Branches"] == "ALBAHA", "Achieved"].iloc[0].replace(",", "")),
    )

    show_chart(old_df_name=df, branch_name="ALBAHA")


# ===============================
#   JAZAN main page
# ===============================
def jazan_main():
    df = load_data()
    st.divider()
    render_target_dashboard(
        month_name=month_name,
        target=int(df.loc[df["Branches"] == "JAZAN", "Target"].iloc[0].replace(",", "")),
        achieved=int(df.loc[df["Branches"] == "JAZAN", "Achieved"].iloc[0].replace(",", "")),
    )

    show_chart(old_df_name=df, branch_name="JAZAN")


# ===============================
#   KHAMIS main page
# ===============================
def khamis_main():
    df = load_data()
    st.divider()
    render_target_dashboard(
        month_name=month_name,
        target=int(df.loc[df["Branches"] == "KHAMIS", "Target"].iloc[0].replace(",", "")),
        achieved=int(df.loc[df["Branches"] == "KHAMIS", "Achieved"].iloc[0].replace(",", "")),
    )

    show_chart(old_df_name=df, branch_name="KHAMIS")


# ===============================
#   NAJRAN main page
# ===============================
def najran_main():
    df = load_data()
    st.divider()
    render_target_dashboard(
        month_name=month_name,
        target=int(df.loc[df["Branches"] == "NAJRAN", "Target"].iloc[0].replace(",", "")),
        achieved=int(df.loc[df["Branches"] == "NAJRAN", "Achieved"].iloc[0].replace(",", "")),
    )

    show_chart(old_df_name=df, branch_name="NAJRAN")
