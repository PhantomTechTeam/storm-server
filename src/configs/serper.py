from knowledge_storm.rm import SerperRM
from os import getenv
class Serper:
    def __init__(self, query_params):
        self.api_key = os.getenv("SERPER_API_KEY")
        self.query_params = query_params
        self.rm = SerperRM(serper_search_api_key=os.getenv("SERPER_API_KEY"), query_params=query_params)
