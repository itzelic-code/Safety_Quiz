import openai
import streamlit as st

with st.sidebar:
    st.image("image/q_logo.png", width=200, output_format="PNG")
    st.text("saramin@gmail.com")

# 제목
c30, c32 = st.columns([0.5, 3])

with c30:
    st.image("image/chart.png", width=90)

with c32:
    st.title("중대재해상황 프로세스")
    st.caption("중대재해상황에서의 작업 진행과정")

st.image("image/플로우차트예시.jpeg")
