import streamlit as st
import io
from pydub import AudioSegment

# التأكد من تثبيت مكتبة pydub و ffmpeg قبل الاستخدام:
# pip install pydub

st.title("🎤 تسجيل الصوت وتشغيله")

# تسجيل الصوت باستخدام st.audio_input
audio_file = st.audio_input("اضغط للتسجيل:")

if audio_file is not None:
    # قراءة الملف الصوتي من المستخدم
    audio_bytes = audio_file.read()
    
    # عرض الصوت مباشرة للمستخدم
    st.audio(audio_bytes, format="audio/wav")

    # تحويل الصوت باستخدام pydub إذا لزم الأمر
    try:
        audio = AudioSegment.from_file(io.BytesIO(audio_bytes), format="wav")
        audio.export("recorded_audio.wav", format="wav")
        st.success("✅ تم حفظ الملف الصوتي بنجاح!")
    except Exception as e:
        st.error(f"⚠️ خطأ أثناء حفظ الملف الصوتي: {e}")

    # تشغيل الصوت المحفوظ للتأكد
    try:
        st.audio("recorded_audio.wav", format="audio/wav")
    except Exception as e:
        st.error(f"⚠️ خطأ أثناء تشغيل الملف المحفوظ: {e}")
