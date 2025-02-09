import streamlit as st
import io

st.title("🎤 تسجيل الصوت وتشغيله")

# تسجيل الصوت باستخدام st.audio_input
audio_file = st.audio_input("اضغط للتسجيل:")

if audio_file is not None:
    # قراءة الصوت من الملف المسجل
    audio_bytes = audio_file.read()

    # عرض الصوت مباشرة بعد التسجيل
    st.audio(audio_bytes, format="audio/wav")

    # حفظ الصوت إلى ملف محلي
    with open("recorded_audio.wav", "wb") as f:
        f.write(audio_bytes)

    st.success("✅ تم حفظ الصوت بنجاح!")

    # عرض الصوت المحفوظ للتأكد
    st.audio("recorded_audio.wav", format="audio/wav")
