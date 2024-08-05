from os import environ
from .storm import lm_configs
from knowledge_storm.lm import OpenAIModel


def setup_openai_kwargs():
    openai_kwargs = {
        "api_key": environ.get("OPENAI_API_KEY"),
        "temperature": 1.0,
        "top_p": 0.9,
    }
    return openai_kwargs


def setup_gpt_3_5(openai_kwargs):
    gpt_35 = OpenAIModel(
        model="gpt-3.5-turbo",
        max_tokens=environ.get("OPEN_AI_GPT35_MAX_TOKENS"),
        **openai_kwargs
    )
    lm_configs.set_conv_simulator_lm(gpt_35)
    lm_configs.set_question_asker_lm(gpt_35)
    lm_configs.set_outline_gen_lm(gpt_35)
    lm_configs.set_article_gen_lm(gpt_35)
    lm_configs.set_article_polish_lm(gpt_35)


def setup_mix_gpt(openai_kwargs):
    gpt_35 = OpenAIModel(model="gpt-3.5-turbo", max_tokens=500, **openai_kwargs)
    gpt_4 = OpenAIModel(model="gpt-4-o", max_tokens=3000, **openai_kwargs)
    lm_configs.set_conv_simulator_lm(gpt_35)
    lm_configs.set_question_asker_lm(gpt_35)
    lm_configs.set_outline_gen_lm(gpt_4)
    lm_configs.set_article_gen_lm(gpt_4)
    lm_configs.set_article_polish_lm(gpt_4)
