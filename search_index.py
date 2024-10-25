# import meilisearch
from meilisearch import Client
import pandas as pd

# meilisearch 객체 생성
host = 'http://localhost:7700/'
key = 'aSampleMasterKey'
client = Client(host, key)

# 회사 검색
def search_company(query):
    return client.index('nasdaq').search(query)

class SearchResult:
    def __init__(self, item):
        self.item = item

    @property
    def symbol(self):
        return self.item['Symbol']
    @property
    def name(self):
        return self.item['Name']

    def __str__(self):
        return f"symbol : {self.symbol}, Name : {self.name}"


# 현재의 모듈에서 실행함
if __name__ == "__main__":
    # search_word = "AAPL"
    search_word = "MicroSoft"
    # result = search_company(search_word)
    # print(result)
    hits = search_company(search_word)['hits']
    # print(hits)
    # hits : Symbol, Name의 값이 들어있는 리스트 자료구조
    search_results = [SearchResult(hit) for hit in hits]
    # print(search_results)

    for s in search_results:
        print(s)
