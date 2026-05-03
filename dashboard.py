import streamlit as st
import pandas as pd
import plotly.express as px


def render_target_dashboard(
        month_name: str,
        target: int,
        achieved: int,
        daily_history: list = None
):
    """
    Render stylish target dashboard.

    Parameters:
    - month_name: e.g. "ديسمبر"
    - target: total target number
    - achieved: achieved so far
    - daily_history: optional list like [10, 20, 30, ...]
    """

    remaining = max(target - achieved, 0)
    percent = (achieved / target) * 100 if target else 0

    # estimate daily requirement (simple logic)
    days_left = 31  # you can improve later dynamically
    daily_needed = remaining / days_left if days_left else 0

    # ---------------------------
    # CSS Styling
    # ---------------------------
    st.markdown("""
        <style>
        body {
            direction: rtl;
            text-align: right;
            background-color: #f5f7fb;
        }

        .title {
            text-align: center;
            font-size: 26px;
            font-weight: bold;
            margin-bottom: 20px;
        }

        .card {
            background: white;
            padding: 18px;
            border-radius: 16px;
            box-shadow: 0 6px 18px rgba(0,0,0,0.08);
            margin-bottom: 12px;
            text-align: center;
        }

        .label {
            font-size: 14px;
            color: #666;
        }

        .value {
            font-size: 22px;
            font-weight: bold;
            color: #6A5ACD;
        }
        </style>
    """, unsafe_allow_html=True)

    # ---------------------------
    # Title
    # ---------------------------
    st.markdown(f"""
        <div class="title">📊 تارجت شهر {month_name}</div>
    """, unsafe_allow_html=True)

    # ---------------------------
    # KPI Cards
    # ---------------------------
    def card(label, value):
        st.markdown(f"""
            <div class="card">
                <div class="label">{label}</div>
                <div class="value">{value}</div>
            </div>
        """, unsafe_allow_html=True)

    card("تارجت الشهر", f"{target} ريال")
    card("ماتم تحقيقه حتى الأن", f"{achieved} ريال")
    card("المتبقي", f"{remaining} ريال")
    card("التارجت اليومي المطلوب", f"{daily_needed:.1f} ريال / يوم")
    st.divider()
    # ---------------------------
    # Progress Bar
    # ---------------------------
    st.progress(min(percent / 100, 1.0))
    st.text(f"📈 نسبة الإنجاز: {percent:.1f}%")

    # ---------------------------
    # Chart (optional)
    # ---------------------------


def show_chart(old_df_name, branch_name):
    new_df = pd.DataFrame({
        "Headers": ["التارجت", "ماتم تحقيقه الى الان"],
        "Values": [int(old_df_name.loc[old_df_name["Branches"] == branch_name, "Target"].squeeze().replace(",", ""))
            , int(old_df_name.loc[old_df_name["Branches"] == branch_name, "Achieved"].squeeze().replace(",", ""))]
    })
    figure1 = px.bar(new_df, x=["التارجت", "ماتم تحقيقه الى الان"], y="Values", text="Values", color='Headers')
    return st.plotly_chart(figure1)
