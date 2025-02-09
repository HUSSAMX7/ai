import streamlit as st
import io

st.title("🎤 تسجيل الصوت وتشغيله")

# استخدام st.audio_input لتسجيل الصوت
audio_file = st.audio_input("اضغط للتسجيل:")

if audio_file is not None:
    # قراءة الصوت في BytesIO لتجنب مشاكل الحفظ
    audio_bytes = io.BytesIO(audio_file.read())

    # عرض الصوت المسجل
    st.audio(audio_bytes, format="audio/wav")

    # حفظ الملف الصوتي محليًا للتأكد من أنه يعمل
    with open("recorded_audio.wav", "wb") as f:
        f.write(audio_bytes.getvalue())

    st.success("✅ تم تسجيل الصوت وحفظه بنجاح!")
