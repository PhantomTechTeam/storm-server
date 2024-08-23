from knowledge_storm.rm import BraveRM
import os


class Brave:
    def __init__(self, engine_args):
        self.api_key = os.environ.get("BRAVE_API_KEY")
        self.rm = BraveRM(brave_search_api_key=self.api_key, k=engine_args.search_top_k)
