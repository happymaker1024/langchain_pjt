# streamlit run main_app.py

import streamlit as st
from report_service import investment_report

st.title("AI 투자 보고서 생성 서비스")

st.text_input("회사명", "Apple Inc")
company_list = ["AAPL: Apple Inc", 
                "APLE: Apple Hospitality REIT Inc. Common Shares"]

company = st.selectbox("검색 결과 목록", company_list)


# 회사 이름, symbol
company = "Apple Inc"
symbol = "AAPL"

st.header(f"{company} 투자보고서 생성")

if st.button("보고서 생성"):
    with st.spinner(text="진행 중..."):
        # llm을 통한 질문 및 응답 받기
        report = investment_report(company, symbol)
        st.success("완료")
    st.write(report)

