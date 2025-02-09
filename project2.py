import streamlit as st
import tempfile
import whisper
import google.generativeai as genai
import io
from gtts import gTTS
import os
import librosa

# إعداد مفتاح Gemini API وتحميل النموذج
genai.configure(api_key="AIzaSyBROCzAVfRpwNJuj6urgfcyfWb86os9h6E")
gemini_model = genai.GenerativeModel("gemini-1.5-flash")

st.title("تسجيل الصوت وتحويله إلى نص وإرسال الرد")
st.write("سجل رسالة صوتية، وسيتم تحويلها إلى نص باستخدام Whisper ثم إرسالها إلى Gemini للحصول على رد. بعد ذلك، يتم تحويل الرد إلى صوت.")

# استخدام st.audio_input لتسجيل الصوت
recorder_audio = st.audio_input("Record a voice message")

if recorder_audio:
    # عرض الملف الصوتي المسجل للمستخدم
    st.audio(recorder_audio)

    # حفظ الملف الصوتي في ملف مؤقت بصيغة WAV
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        temp_audio.write(recorder_audio.read())
        temp_file_path = temp_audio.name

    st.info("جارٍ تحويل الصوت إلى نص باستخدام Whisper...")

    # تحميل نموذج Whisper (اختر النموذج المناسب: base, small, medium, ...)
    model = whisper.load_model("base")

    # تحميل الملف الصوتي باستخدام librosa وتحويله إلى معدل 16kHz
    audio_data, sr = librosa.load(temp_file_path, sr=16000)

    # تمرير المصفوفة الناتجة إلى نموذج Whisper
    result = model.transcribe(audio_data)
    text = result["text"].strip()

    st.subheader("النص المحول:")
    st.write(text)

    # إنشاء prompt لإرساله إلى Gemini API
    prompt = (
        f"{text}. "
        "أجب على السؤال بطريقة مختصرة. "
        "إذا كان السؤال يتعلق بك، فأجب أن من ساعد في تطويرك هو شركة ريناد المجد. "
        "إذا لم يكن السؤال مفهومًا، اطلب من السائل إعادة صياغة السؤال لأنه غير مفهوم."
    )

    st.info("جارٍ الحصول على رد من Gemini API...")
    response = gemini_model.generate_content(prompt)
    gemini_text = response.text.strip()

    st.subheader("رد Gemini:")
    st.write(gemini_text)

    # تحويل رد Gemini إلى صوت باستخدام gTTS
    st.info("جارٍ تحويل رد Gemini إلى صوت...")
    tts = gTTS(text=gemini_text, lang="ar")
    tts_buffer = io.BytesIO()
    tts.write_to_fp(tts_buffer)
    tts_buffer.seek(0)
    st.audio(tts_buffer, format="audio/mp3")

    # حذف الملف المؤقت بعد الانتهاء
    os.remove(temp_file_path)
