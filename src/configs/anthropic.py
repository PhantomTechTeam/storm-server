from .storm import lm_configs
from os import environ
from knowledge_storm.lm import OpenAIModel, ClaudeModel

def setup_anthropic(openai_kwargs):
    gpt_4o_turbo = OpenAIModel(model="gpt-4o-turbo", max_tokens=environ.get("OPEN_AI_GPT35_MAX_TOKENS"), **openai_kwargs)
    claude = ClaudeModel(model="claude-3-sonnet-20240229", api_key=environ.get("ANTHROPIC_API_KEY"))
    lm_configs.set_conv_simulator_lm(gpt_4o_turbo)
    lm_configs.set_question_asker_lm(gpt_4o_turbo)
    lm_configs.set_outline_gen_lm(gpt_4o_turbo)

    lm_configs.set_article_gen_lm(claude)
    lm_configs.set_article_polish_lm(gpt_4o_turbo)
