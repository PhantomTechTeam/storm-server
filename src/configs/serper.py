from knowledge_storm.rm import SerperRM
from os import getenv
def setup_you_rm(engine_args, query_params):
    rm = SerperRM(serper_search_api_key=os.getenv("SERPER_API_KEY"), query_params=query_params)
    return rm
