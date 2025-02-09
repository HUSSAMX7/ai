import streamlit as st

# عنوان التطبيق
st.title("🎤 تسجيل الصوت في Streamlit")

# استخدام st.audio_input لتسجيل الصوت
audio_file = st.audio_input("اضغط للتسجيل:")

if audio_file is not None:
    # عرض مشغل الصوت للمستخدم
    st.audio(audio_file, format="audio/wav")
    
    # حفظ الملف الصوتي
    with open("recorded_audio.wav", "wb") as f:
        f.write(audio_file.read())

    st.success("✅ تم تسجيل الصوت وحفظه!")
