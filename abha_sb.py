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
st.markdown("##### إدارة العملاء + بحث + تصنيف + واتساب")

# ------------------ رابط البيانات ------------------
CSV_URL = "https://docs.google.com/spreadsheets/d/1_L0xc0j3jKnbcolXI-88493Elb_SW8SpZNafkdbMj7E/export?format=csv"


# ------------------ تحميل البيانات ------------------
@st.cache_data(ttl=30)
def load_data():
    df = pd.read_csv(CSV_URL)

    # تنظيف رقم الجوال
    df["رقم الجوال"] = df["رقم الجوال"].astype(str).str.replace(" ", "")

    # تحويل المشتريات إلى رقم
    df["قيمة المشتريات"] = (
        df["قيمة المشتريات"]
        .astype(str)
        .str.replace(",", "")
        .astype(float)
    )

    # تصنيف العملاء
    VIP_THRESHOLD = 5000
    df["تصنيف العميل"] = df["قيمة المشتريات"].apply(
        lambda x: "VIP ⭐" if x >= VIP_THRESHOLD else "عادي"
    )

    return df


df = load_data()

# ------------------ البحث ------------------
st.markdown("### 🔎 بحث")

search = st.text_input("ابحث بالاسم أو رقم الجوال")

filtered_df = df.copy()

if search:
    search = search.lower()
    filtered_df = df[
        df.astype(str)
        .apply(lambda row: row.str.lower().str.contains(search).any(), axis=1)
    ]

# ------------------ الفلاتر ------------------
col1, col2, col3 = st.columns(3)

with col1:
    min_val, max_val = st.slider(
        "نطاق المشتريات",
        int(df["قيمة المشتريات"].min()),
        int(df["قيمة المشتريات"].max()),
        (
            int(df["قيمة المشتريات"].min()),
            int(df["قيمة المشتريات"].max())
        )
    )

with col2:
    sort_option = st.selectbox(
        "ترتيب",
        ["بدون", "الأعلى", "الأقل"]
    )

with col3:
    category_filter = st.selectbox(
        "تصنيف العملاء",
        ["الكل", "VIP ⭐", "عادي"]
    )

# تطبيق الفلاتر
filtered_df = filtered_df[
    filtered_df["قيمة المشتريات"].between(min_val, max_val)
]

if category_filter != "الكل":
    filtered_df = filtered_df[
        filtered_df["تصنيف العميل"] == category_filter
        ]

if sort_option == "الأعلى":
    filtered_df = filtered_df.sort_values(by="قيمة المشتريات", ascending=False)
elif sort_option == "الأقل":
    filtered_df = filtered_df.sort_values(by="قيمة المشتريات", ascending=True)


# ------------------ واتساب فردي ------------------
def create_whatsapp_link(phone):
    phone = str(phone)

    if phone.startswith("0"):
        phone = "966" + phone[1:]

    message = f"مرحبا ، عندنا عروض وأقمشة جديدة في الفاخرة للخياطة الرجالية "
    encoded_message = urllib.parse.quote(message)

    return f"https://wa.me/{phone}?text={encoded_message}"


# ------------------ رسالة جماعية ------------------
st.markdown("### 📢 رسالة جماعية")

bulk_message = st.text_area(
    "اكتب الرسالة",
    "مرحبا، عندنا عروض خاصة لك 🔥"
)


def create_bulk_links(df, message):
    links = []

    for _, row in df.iterrows():
        phone = str(row["رقم الجوال"])

        if phone.startswith("0"):
            phone = "966" + phone[1:]

        # تخصيص الرسالة حسب التصنيف
        if row["تصنيف العميل"] == "VIP ⭐":
            msg = f"{message} 💎 عميلنا المميز "
        else:
            msg = f"{message}"

        text = urllib.parse.quote(msg)
        link = f"https://wa.me/{phone}?text={text}"

        links.append(link)

    return links


if st.button("🚀 تجهيز روابط الإرسال"):
    links = create_bulk_links(filtered_df, bulk_message)

    st.success(f"تم إنشاء {len(links)} رابط")

    for link in links:
        st.markdown(f"[فتح واتساب]({link})")

# ------------------ المؤشرات ------------------
st.markdown("### 📊 ملخص")

c1, c2, c3 = st.columns(3)

c1.metric("عدد العملاء", len(filtered_df))

total_purchases = filtered_df["قيمة المشتريات"].sum()
c2.metric("إجمالي المشتريات", int(total_purchases))

avg_purchases = filtered_df["قيمة المشتريات"].mean()
c3.metric("متوسط الشراء", round(avg_purchases, 2))

# ------------------ عرض البيانات ------------------
st.markdown("### 📋 بيانات العملاء")

for _, row in filtered_df.iterrows():
    col1, col2, col3, col4, col5 = st.columns([3, 2, 2, 2, 2])

    col2.write(row["رقم الجوال"])
    col3.write(f"{int(row['قيمة المشتريات'])} ريال")
    col4.write(row["تصنيف العميل"])

    whatsapp_link = create_whatsapp_link(
        row["رقم الجوال"],
    )

    col5.link_button("📲 واتساب", whatsapp_link)

# ------------------ تحديث ------------------
if st.button("🔄 تحديث البيانات"):
    st.cache_data.clear()
    st.rerun()
