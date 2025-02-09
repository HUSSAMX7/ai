import streamlit as st
import whisper
import tempfile

# عنوان التطبيق
st.title("تحويل الصوت إلى نص باستخدام Whisper")

# تحميل نموذج Whisper (يمكنك اختيار النموذج المناسب مثل "base", "small", "medium", الخ.)
st.info("جارٍ تحميل نموذج Whisper...")
model = whisper.load_model("base")
st.success("تم تحميل النموذج.")

# استخدام st.audio_input لتسجيل الصوت
audio_file = st.audio_input("سجّل رسالتك الصوتية هنا")

if audio_file is not None:
    # عرض مشغل الصوت للمستخدم
    st.audio(audio_file)
    
    # حفظ الملف الصوتي مؤقتاً بصيغة WAV
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(audio_file.read())
        tmp_path = tmp.name

    st.info("جارٍ تحويل الصوت إلى نص...")
    
    # استخدام Whisper لتحويل الصوت إلى نص
    result = model.transcribe(tmp_path,fp16=False)
    transcription = result["text"].strip()

    st.subheader("النص المحول:")
    st.write(transcription)
