from os import environ
from knowledge_storm.lm import ClaudeModel


class Anthropic:
    def __init__(self, lm_configs):
        self.anthropic_api_key = environ.get("ANTHROPIC_API_KEY")
        self.simulator_lm = environ.get("ANTHROPIC_SIMULATOR_LM")
        self.asker_lm = environ.get("ANTHROPIC_ASKER_LM")
        self.gen_lm = environ.get("ANTHROPIC_GEN_LM")
        self.article_gen_lm = environ.get("ANTHROPIC_ARTICLE_GEN_LM")
        self.polish_lm = environ.get("ANTHROPIC_POLISH_LM")
        claude_kwargs = {
            "api_key": self.anthropic_api_key,
            "temperature": 1.0,
            "top_p": 0.9,
        }

        conv_simulator_lm = ClaudeModel(
            model=self.conv_simulator_lm, max_tokens=500, **claude_kwargs
        )
        question_asker_lm = ClaudeModel(
            model=self.question_asker_lm, max_tokens=500, **claude_kwargs
        )
        outline_gen_lm = ClaudeModel(
            model=self.outline_gen_lm, max_tokens=400, **claude_kwargs
        )
        article_gen_lm = ClaudeModel(
            model=self.article_gen_lm, max_tokens=700, **claude_kwargs
        )
        article_polish_lm = ClaudeModel(
            model=self.article_polish_lm, max_tokens=4000, **claude_kwargs
        )

        lm_configs.set_conv_simulator_lm(conv_simulator_lm)
        lm_configs.set_question_asker_lm(question_asker_lm)
        lm_configs.set_outline_gen_lm(outline_gen_lm)
        lm_configs.set_article_gen_lm(article_gen_lm)
        lm_configs.set_article_polish_lm(article_polish_lm)
