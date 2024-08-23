from knowledge_storm.rm import YouRM
from os import getenv


class You:
    def __init__(self, engine_args):
        self.rm = YouRM(ydc_api_key=getenv("YDC_API_KEY"), k=engine_args.search_top_k)
