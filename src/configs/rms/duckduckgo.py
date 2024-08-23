from knowledge_storm.rm import DuckDuckGoSearchRM


class DuckDuckGoSearch:
    def __init__(self, engine_args):
        self.rm = DuckDuckGoSearchRM(k=engine_args.search_top_k)
