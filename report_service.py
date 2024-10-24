# 필요한 패키지 임폴트
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
# stock 정보를 객체로 모듈화해서 불러오기
from stock_info import Stock

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

# gpt model 객체 생성
# llm = ChatOpenAI(model="gpt-4o", api_key=api_key, temperature=0)
llm = ChatOpenAI(model="gpt-3.5-turbo-0125", api_key=api_key, temperature=0)

# llm에 질문하고, 레포트 생성함.
def investment_report(company, symbol):
    system_prompt = """
        Want assistance provided by qualified individuals enabled with experience on understanding charts using technical analysis tools while interpreting macroeconomic environment prevailing across world consequently assisting customers acquire long term advantages requires clear verdicts therefore seeking same through informed predictions written down precisely! First statement contains following content- “Can you tell us what future stock market looks like based upon current conditions ?".
        """
    user_prompt = """
        {company}에 주식을 투자해도 될까요? 마크다운 형식의 투자보고서를 한글로 작성해 주세요.
        야래의 기본 정보, 재무제표를 참고해 마크다운 형식의 투자 보고서를 한글로 작성해 주세요.

        기본정보:
        {basic_info}

        재무제표:
        {finacial_statement}
        """
    # 프롬프트 객체 생성
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("user", user_prompt)
    ])
    # 파서 객체 생성
    output_parser = StrOutputParser()

    chain = prompt | llm | output_parser

    # company, symbol로 llm에 요청하기

    stock = Stock(symbol)
    req_value = {
        "company":company,
        # 기본정보 :  basic_info
        "basic_info": stock.get_basic_info(),
        # 재무제표: finacial_statement
        "finacial_statement" : stock.get_financial_statement()
                }

    response = chain.invoke(req_value)
    # llm 결과 리턴함
    return response


if __name__ == "__main__":
    company = "Apple Inc"
    symbol = "AAPL"
    res = investment_report(company, symbol)

    print(res)