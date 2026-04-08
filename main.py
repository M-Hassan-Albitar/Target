import streamlit as st
from arabic_support import support_arabic_text
from datetime import datetime
import functions

support_arabic_text()


def clean_data(branch_num):
    data = functions.read_json()
    branch_data = []
    all_branches_list = data["Branches"]
    branch_target = all_branches_list[branch_num]["Target"]
    branch_residual = all_branches_list[branch_num]["Residual"]
    target_percentage = all_branches_list[branch_num]["Percentage"]
    branch_data.append(branch_target)
    branch_data.append(branch_residual)
    branch_data.append(target_percentage)
    return branch_data


abha = clean_data(0)
albaha = clean_data(1)
jizan = clean_data(2)
khamis = clean_data(3)
najran = clean_data(4)

branches = ["اختر الفرع", "أبها", "خميس مشيط", "جيزان", "نجران", "الباحة"]

# Get current date and time
now = datetime.now()
today_date = now.strftime("%A, %d/%m/%Y")
today = now.strftime("%d")
current_time = now.strftime("%H:%M:%S")

THIS_MONTH = 30
RESIDUAL_DAY = THIS_MONTH - int(today)
ITEM_PRICE = 500

st.set_page_config(page_title="Alfakhera-south", layout="centered")
st.title("الفاخرة للخياطة الرجالية", text_alignment="center")
st.subheader('المنطقة الجنوبية', text_alignment="center")
st.markdown(f'<p>{today_date} - {current_time}</p>', unsafe_allow_html=True)
# Custom CSS for different backgrounds
st.markdown("""
    <style>
    .box1 {
        background-color: orange;
        text-align: center;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .box2 {
        background-color: red;
        text-align: center;
        padding: 20px;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)
branch_name = st.selectbox("", options=branches, key="choice")
match branch_name:
    case "أبها":
        password = st.text_input("", key="password", type="password", placeholder="اكتب الباسورد الخاص بفرعك")
        if password == "M1":
            st.info("أشرف ✅")
            # First text section
            st.markdown('<div class="box1">'
                        '<h3>التارجت</h3>'
                        f'<h2>"{abha[0]}"</h2>'
                        '</div>', unsafe_allow_html=True)

            # Second text section
            st.markdown('<div class="box2">'
                        '<h3>المتبقي على التارجت</h3>'
                        f'<h5>{abha[2]}</h5>'
                        f'<h2>"{abha[1]}"</h2>'
                        f'<h2>معدل الثياب اليومي لتحقيق التارجت</h2>'
                        f'<h2>"{int(abha[1]) / RESIDUAL_DAY / ITEM_PRICE}"</h2>'
                        '</div>', unsafe_allow_html=True)
    case "خميس مشيط":
        password = st.text_input("", key="password", type="password", placeholder="اكتب الباسورد الخاص بفرعك")
        if password == "H2":
            st.info("ممدوح أبوجامع ✅")
            # First text section
            st.markdown('<div class="box1">'
                        '<h3>التارجت</h3>'
                        f'<h2>"{khamis[0]}"</h2>'
                        '</div>', unsafe_allow_html=True)

            # Second text section
            st.markdown('<div class="box2">'
                        '<h3>المتبقي على التارجت</h3>'
                        f'<h5>{khamis[2]}</h5>'
                        f'<h2>"{khamis[1]}"</h2>'
                        '</div>', unsafe_allow_html=True)

    case "جيزان":
        password = st.text_input("", key="password", type="password", placeholder="اكتب الباسورد الخاص بفرعك")
        if password == "A3":
            st.info("أحمد عاطف ✅")
            # First text section
            st.markdown('<div class="box1">'
                        '<h3>التارجت</h3>'
                        f'<h2>"{jizan[0]}"</h2>'
                        '</div>', unsafe_allow_html=True)

            # Second text section
            st.markdown('<div class="box2">'
                        '<h3>المتبقي على التارجت</h3>'
                        f'<h5>{jizan[2]}</h5>'
                        f'<h2>"{jizan[1]}"</h2>'
                        '</div>', unsafe_allow_html=True)

    case "نجران":
        password = st.text_input("", key="password", type="password", placeholder="اكتب الباسورد الخاص بفرعك")
        if password == "A4":
            st.info("أسامة نورالدين ✅")
            # First text section
            st.markdown('<div class="box1">'
                        '<h3>التارجت</h3>'
                        f'<h2>"{najran[0]}"</h2>'
                        '</div>', unsafe_allow_html=True)

            # Second text section
            st.markdown('<div class="box2">'
                        '<h3>المتبقي على التارجت</h3>'
                        f'<h5>{najran[2]}</h5>'
                        f'<h2>"{najran[1]}"</h2>'
                        '</div>', unsafe_allow_html=True)

    case "الباحة":
        password = st.text_input("", key="password", type="password", placeholder="اكتب الباسورد الخاص بفرعك")
        if password == "Y5":
            st.info("Albaha ✅")
            # First text section
            st.markdown('<div class="box1">'
                        '<h3>التارجت</h3>'
                        f'<h2>"{albaha[0]}"</h2>'
                        '</div>', unsafe_allow_html=True)

            # Second text section
            st.markdown('<div class="box2">'
                        '<h3>المتبقي على التارجت</h3>'
                        f'<h5>{albaha[2]}</h5>'
                        f'<h2>"{albaha[1]}"</h2>'
                        '</div>', unsafe_allow_html=True)
