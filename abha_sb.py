import streamlit as st
import pandas as pd
import urllib.parse

# ------------------ إعداد الصفحة ------------------
st.set_page_config(page_title="العملاء")

st.markdown("""
<style>
html, body, [class*="css"]  {
    direction: rtl;
    text-align: right;
}
.block-container {
    padding: 2rem 3rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown("### 📇 شاشة العملاء")
st.markdown("##### إدارة العملاء + بحث سريع + واتساب")

# ------------------ رابط Google Sheets CSV ------------------
CSV_URL = "https://docs.google.com/spreadsheets/d/1_L0xc0j3jKnbcolXI-88493Elb_SW8SpZNafkdbMj7E/export?format=csv"


# ------------------ تحميل البيانات ------------------
@st.cache_data(ttl=30)
def load_data():
    df = pd.read_csv(CSV_URL)
    return df


df = load_data()

# ------------------ البحث ------------------
st.markdown("### 🔎 بحث سريع")

search = st.text_input(
    "ابحث بالاسم أو رقم الجوال",
    placeholder="اكتب أي شيء..."
)

filtered_df = df.copy()

if search:
    search = search.lower()
    filtered_df = df[
        df.astype(str)
        .apply(lambda row: row.str.lower().str.contains(search).any(), axis=1)
    ]

# ------------------ الفلاتر ------------------
# col1, col2 = st.columns(2)

# with col1:
#     min_val, max_val = st.slider(
#         "نطاق المشتريات",
#         int(df["قيمة المشتريات"].min()),
#         int(df["قيمة المشتريات"].max()),
#         (int(df["قيمة المشتريات"].min()), int(df["قيمة المشتريات"].max()))
#     )

# with col2:
sort_option = st.selectbox(
    "ترتيب",
    ["بدون", "الأعلى", "الأقل"]
)

# filtered_df = filtered_df[
#     filtered_df["قيمة المشتريات"].between(min_val, max_val)
# ]

if sort_option == "الأعلى":
    filtered_df = filtered_df.sort_values(by="قيمة المشتريات", ascending=False)
elif sort_option == "الأقل":
    filtered_df = filtered_df.sort_values(by="قيمة المشتريات", ascending=True)


# ------------------ دالة واتساب ------------------
def create_whatsapp_link(phone, name, amount):
    phone = str(phone)

    # تحويل الرقم السعودي
    if phone.startswith("0"):
        phone = "966" + phone[1:]

    message = f"مرحبا ياشيخ {name} \n  وحشتنا ياغالي شرفنا في الفاخرة للخياطة لأحدث الأقمشة وأقوى العروض"
    encoded_message = urllib.parse.quote(message)

    return f"https://wa.me/{phone}?text={encoded_message}"


# ------------------ المؤشرات ------------------
st.markdown("### 📊 ملخص")

c1, c2, c3 = st.columns(3)

c1.metric("عدد العملاء", len(filtered_df))
total_purchases = filtered_df["قيمة المشتريات"].str.replace(",", "").astype(int).sum()
c2.metric("إجمالي المشتريات", int(total_purchases))
raw_value = filtered_df['قيمة المشتريات'].iloc[0]

# 1. Replace comma and convert the single string to a float
numeric_value = float(raw_value.replace(',', ''))

# 2. Use the numerical value (no mean() needed if it's only one value)
c3.metric(
    "متوسط الشراء",
    round(numeric_value, 2)
)

# ------------------ عرض البيانات ------------------
st.markdown("### 📋 بيانات العملاء")

for i, row in filtered_df.iterrows():
    col1, col2, col3, col4 = st.columns([3, 2, 2, 2])

    col1.write(row["اسم العميل"])
    col2.write(row["رقم الجوال"])
    col3.write(f"{row['قيمة المشتريات']} ريال")

    whatsapp_link = create_whatsapp_link(
        row["رقم الجوال"],
        row["اسم العميل"],
        row["قيمة المشتريات"]
    )

    col4.link_button("📲 واتساب", whatsapp_link)

# # ------------------ تحميل ------------------
# st.markdown("### 📥 تحميل البيانات")
#
# csv = filtered_df.to_csv(index=False).encode('utf-8')
# st.download_button(
#     "⬇️ تحميل CSV",
#     csv,
#     "customers.csv",
#     "text/csv"
# )
#
# ------------------ تحديث ------------------
if st.button("🔄 تحديث البيانات"):
    st.cache_data.clear()
    st.rerun()

# # ------------------ الفوتر ------------------
# st.markdown("---")
# st.markdown("تصميم وانشاء محمد عبدالقادر - مشرف المنطقة الجنوبية")
