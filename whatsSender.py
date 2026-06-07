import streamlit as st
import pywhatkit
import time


def whats_sender():
    phones_text = st.text_area(
        "الأرقام (رقم في كل سطر)",
        placeholder="""
    501234567
    589876543
    545555555
    """
    )

    message = st.text_area("الرسالة")
    ik = "+966"

    if st.button("إرسال للجميع"):

        phones = [
            ik + phone.strip()
            for phone in phones_text.split("\n")
            if phone.strip()
        ]

        st.write(f"عدد الأرقام: {len(phones)}")

        for phone in phones:
            try:
                pywhatkit.sendwhatmsg_instantly(
                    phone,
                    message,
                    wait_time=10,
                    tab_close=True
                )

                st.success(f"تم الإرسال إلى {phone}")

                # انتظار بين الرسائل
                time.sleep(10)

            except Exception as e:
                st.error(f"فشل الإرسال إلى {phone}: {e}")
