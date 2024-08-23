from knowledge_storm.rm import SearXNG
import os


class SearXNGRM:
    def __init__(self, engine_args):
        self.rm = SearXNG(
            searxng_api_url=os.getenv("SEARXNG_API_URL"),
            searxng_api_key=os.getenv("SEARXNG_API_KEY"),
            k=engine_args.search_top_k,
        )
