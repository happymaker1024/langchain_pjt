import yfinance as yf
import pandas as pd

class Stock:
    # 생성자
    def __init__(self, symbol):
        self.symbol = symbol
        self.ticker = yf.Ticker(symbol)

    # 회사 정보 수집 함수(메서드), 마크다운을 변형
    def get_basic_info(self):
        basic_info = pd.DataFrame.from_dict(self.ticker.info, orient='index', columns=["Value"])
        basic_info = basic_info.loc[['longName', 'marketCap', 'industry', 'sector', 'fullTimeEmployees', 'currentPrice', 'enterpriseValue']].to_markdown()
        return basic_info

    # 재무제표 수집 함수
    def get_financial_statement(self):
        income_stmt = self.ticker.income_stmt.loc[['Total Revenue', 'Gross Profit',  \
                                                   'Operating Income', 'Net Income']].to_markdown()
        balance_sheet = self.ticker.balance_sheet.loc[['Total Assets', \
                                                       'Total Liabilities Net Minority Interest', \
                                                         'Stockholders Equity']].to_markdown()
        cash_flow = self.ticker.cash_flow.loc[['Operating Cash Flow', \
                                                'Investing Cash Flow', 'Financing Cash Flow']].to_markdown()
        return f"""
            ### 손익계산서
            {income_stmt} 
            ### 대차대조표
            {balance_sheet}
            ### 현금 흐름
            {cash_flow}
            """

    # 주식 거래량

# 현재의 모듈에서 실행함
if __name__ == "__main__":

    symbol = "AAPL"
    stock = Stock(symbol)
    # print(stock.symbol)
    # print(stock.ticker)
    # print(type(stock.ticker))
    # print(stock.get_basic_info())
    print(stock.get_financial_statement())



