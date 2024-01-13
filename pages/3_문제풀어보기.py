import openai
import streamlit as st

with st.sidebar:
    st.image("image/q_logo.png", width=200, output_format="PNG")
    st.text("saramin@gmail.com")

# 제목
c30, c32 = st.columns([0.5, 3])

with c30:

    # st.caption("")
    st.image("image/test.png", width=90)

with c32:

    st.title("중대재해처벌법 퀴즈")
    st.caption("문제를 풀어보며 중대재해처벌법과 조치사항에 대해 이해한 것을 확인합니다.")

tabMain, tabHowto, tabWBS = st.tabs(["[1.중대재해처벌법]", "[2. 중대재해 조치사항]", "[3. 안전관리자 의무사항]"])

with tabMain:
    st.title("1. 중대재해처벌법")

    with open("image/중대재해퀴즈.md", "r") as file:
        file_content = file.read()
        st.markdown(file_content, unsafe_allow_html=False, help=None)

with tabHowto:
    st.title("2. 중대재해 상황시 조치사항")

with tabWBS:
    st.title("3. 안전관리자의 의무사항")