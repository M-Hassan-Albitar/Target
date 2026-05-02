import streamlit as st


# import pandas as pd
# import plotly.express as px

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
    card("المعدل التقريبي اليومي المطلوب", f"{daily_needed:.1f} ريال / يوم")

    # ---------------------------
    # Progress Bar
    # ---------------------------
    st.progress(min(percent / 100, 1.0))
    st.write(f"📈 نسبة الإنجاز: {percent:.1f}%")

    # ---------------------------
    # Chart (optional)
    # ---------------------------
    # if daily_history:
    #     df = pd.DataFrame({
    #         "اليوم": list(range(1, len(daily_history) + 1)),
    #         "المبيعات": daily_history
    #     })
    #
    #     fig = px.line(df, x="اليوم", y="المبيعات", markers=True,
    #                   title="📊 التقدم اليومي")
    #     st.plotly_chart(fig, use_container_width=True)
