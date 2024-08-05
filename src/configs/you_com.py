from knowledge_storm.rm import YouRM
from os import getenv


def setup_you_rm(engine_args):
    rm = YouRM(ydc_api_key=getenv("YDC_API_KEY"), k=engine_args.search_top_k)
    return rm
