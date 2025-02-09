import sounddevice as sd
import streamlit as st
from scipy.io.wavfile import write
import numpy as np

st.title("🎤 تسجيل الصوت وحفظه")

# إعداد متغيرات للتسجيل
duration = st.slider("حدد مدة التسجيل (بالثواني):", min_value=1, max_value=10, value=5)
sample_rate = 44100  # معدل العينة (عدد العينات في الثانية)

if st.button("🔴 بدء التسجيل"):
    st.info("جارٍ التسجيل... تحدث الآن 🎙️")

    # تسجيل الصوت
    try:
        recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, dtype="int16")
        sd.wait()  # انتظر حتى انتهاء التسجيل
        st.success("✅ تم التسجيل!")

        # حفظ الملف بصيغة WAV
        write("recorded_audio.wav", sample_rate, recording)
        st.success("✅ تم حفظ الملف باسم recorded_audio.wav!")

        # تشغيل الملف المحفوظ
        st.audio("recorded_audio.wav", format="audio/wav")
    except Exception as e:
        st.error(f"⚠️ حدث خطأ أثناء التسجيل: {e}")
