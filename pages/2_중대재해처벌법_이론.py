import openai
import streamlit as st

with st.sidebar:
    st.image("image/q_logo.png", width=200, output_format="PNG")
    st.text("saramin@gmail.com")

# 제목
c30, c32 = st.columns([0.5, 3])

with c30:
    st.image("image/book.png", width=90)

with c32:
    st.title("중대재해처벌법 이론")
    st.caption("중대재해처벌법이란 무엇이며, 우리는 중대재해 발생시 어떤 조치를 해야하는가.")

# Markdown 파일 열기
with open("image/중대재해이론.md", "r") as file:
    file_content = file.read()
st.markdown(file_content, unsafe_allow_html=False, help=None)