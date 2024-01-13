import openai
import streamlit as st

with st.sidebar:
    st.image("image/q_logo.png", width=200, output_format="PNG")
    st.text("saramin@gmail.com")

c30, c32 = st.columns([0.5, 3])

with c30:

    # st.caption("")
    st.image("image/tit.png", width=90)

with c32:

    st.title("중대재해처벌법")
    st.caption("이 웹사이트는 중대재해처벌법에 대해 교육하기 위해 사람인안전지도사무소에서 만들었습니다.")


tabMain, tabHowto, tabWBS = st.tabs(["Main", "How to", "WBS"])

with tabMain:
    st.write("메인텝입니다.")

with tabHowto:
    st.write("사용법텝입니다.")

with tabWBS:
    st.write("개발이정표입니다.")