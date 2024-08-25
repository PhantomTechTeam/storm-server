from os import environ
from ..storm import lm_configs
from knowledge_storm.lm import OpenAIModel


class OpenAI:
    def __init__(self):
        self.lm_configs = lm_configs

    def setup_gpt_3_5(self, openai_kwargs):
        gpt_35 = OpenAIModel(
            model="gpt-3.5-turbo",
            max_tokens=int(environ.get("OPEN_AI_GPT35_MAX_TOKENS")),
            **openai_kwargs
        )
        self.lm_configs.set_conv_simulator_lm(gpt_35)
        self.lm_configs.set_question_asker_lm(gpt_35)
        self.lm_configs.set_outline_gen_lm(gpt_35)
        self.lm_configs.set_article_gen_lm(gpt_35)
        self.lm_configs.set_article_polish_lm(gpt_35)

    def setup_mix_gpt(self, openai_kwargs):
        gpt_35 = OpenAIModel(model="gpt-3.5-turbo", max_tokens=500, **openai_kwargs)
        gpt_4 = OpenAIModel(model="gpt-4-o", max_tokens=3000, **openai_kwargs)
        self.lm_configs.set_conv_simulator_lm(gpt_35)
        self.lm_configs.set_question_asker_lm(gpt_35)
        self.lm_configs.set_outline_gen_lm(gpt_4)
        self.lm_configs.set_article_gen_lm(gpt_4)
        self.lm_configs.set_article_polish_lm(gpt_4)

    def setup_gpt_4_o(self, openai_kwargs=None):
        gpt_4 = OpenAIModel(model="gpt-4-o", max_tokens=3000, **openai_kwargs)
        self.lm_configs.set_conv_simulator_lm(gpt_4)
        self.lm_configs.set_question_asker_lm(gpt_4)
        self.lm_configs.set_outline_gen_lm(gpt_4)
        self.lm_configs.set_article_gen_lm(gpt_4)
        self.lm_configs.set_article_polish_lm(gpt_4)