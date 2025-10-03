import streamlit as st
from chatbot import setup_model, get_response
import os

st.set_page_config(page_title="EduBot Santai - Gemini AI", page_icon="📚")

# Load CSS eksternal
if os.path.exists("style.css"):
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.markdown(
    f"""
    <div style="display: flex; align-items: center; margin-top: 10px;">
        <span style="font-size:16px;">👨‍🏫 EduBot Santai Ni Luh Ketut Linda Kusumawati</span>
    </div>
    """,
    unsafe_allow_html=True
)

st.title("📚 Teman Belajar Santai bareng Gemini")
st.markdown(
    f"""
    Hai 👋 aku **EduBot**, asisten belajar santai.  
    Kamu bisa nanya apa aja tentang pelajaran (kayak matematika, basis data, AI, dll)  
    dan aku bakal jelasin dengan bahasa yang gampang dimengerti, kayak lagi ngobrol sama temen. 😉
    """,
    unsafe_allow_html=True
)
# Ambil API Key dari secrets
api_key = st.secrets["GEMINI_API_KEY"]

# Setup model sekali saja
#if "model" not in st.session_state:
#    st.session_state.model = setup_model(api_key)

# Simpan history chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Tombol clear chat
if st.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# Cek file avatar
user_avatar = "user.png" if os.path.exists("user.png") else "👤"
bot_avatar = "bot.png" if os.path.exists("bot.png") else "🤖"

# Tampilkan riwayat chat
for role, msg in st.session_state.messages:
    if role == "user":
        st.chat_message("user", avatar=user_avatar).markdown(msg)
    else:
        st.chat_message("assistant", avatar=bot_avatar).markdown(msg)

# Input chat user
if user_input := st.chat_input("Type your message..."):
    st.session_state.messages.append(("user", user_input))
    st.chat_message("user", avatar=user_avatar).markdown(user_input)

    #bot_reply = get_response(st.session_state.model, user_input)
    bot_reply = get_response(api_key, user_input)
    st.session_state.messages.append(("assistant", bot_reply))
    st.chat_message("assistant", avatar=bot_avatar).markdown(bot_reply)
