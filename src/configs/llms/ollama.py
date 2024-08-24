from os import environ
from ..storm import lm_configs
from knowledge_storm.lm import OllamaClient


class Ollama:
    def __init__(self, ollama_kwargs=None):
        self.lm_configs = lm_configs
        self.conv_simulator_lm = OllamaClient(max_tokens=500, **ollama_kwargs)
        self.question_asker_lm = OllamaClient(max_tokens=500, **ollama_kwargs)
        self.outline_gen_lm = OllamaClient(max_tokens=400, **ollama_kwargs)
        self.article_gen_lm = OllamaClient(max_tokens=700, **ollama_kwargs)
        self.article_polish_lm = OllamaClient(max_tokens=4000, **ollama_kwargs)
        lm_configs.set_conv_simulator_lm(self.conv_simulator_lm)
        lm_configs.set_question_asker_lm(self.question_asker_lm)
        lm_configs.set_outline_gen_lm(self.outline_gen_lm)
        lm_configs.set_article_gen_lm(self.article_gen_lm)
        lm_configs.set_article_polish_lm(self.article_polish_lm)
