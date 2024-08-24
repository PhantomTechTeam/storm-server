from os import environ
from knowledge_storm.lm import ClaudeModel
from ..storm import lm_configs


class Anthropic:
    def __init__(self):
        self.lm_configs = lm_configs
        self.simulator_lm = environ.get("ANTHROPIC_SIMULATOR_LM")
        self.asker_lm = environ.get("ANTHROPIC_ASKER_LM")
        self.gen_lm = environ.get("ANTHROPIC_GEN_LM")
        self.article_gen_lm = environ.get("ANTHROPIC_ARTICLE_GEN_LM")
        self.polish_lm = environ.get("ANTHROPIC_POLISH_LM")
        self.claude_kwargs = {
            "api_key": environ.get("ANTHROPIC_API_KEY"),
            "temperature": 1.0,
            "top_p": 0.9,
        }

        if not self.claude_kwargs["api_key"]:
            raise ValueError("ANTHROPIC_API_KEY environment variable is not set")

        self.conv_simulator_lm = ClaudeModel(
            model=self.simulator_lm, max_tokens=500, **self.claude_kwargs
        )
        self.question_asker_lm = ClaudeModel(
            model=self.asker_lm, max_tokens=500, **self.claude_kwargs
        )
        self.outline_gen_lm = ClaudeModel(
            model=self.gen_lm, max_tokens=400, **self.claude_kwargs
        )
        self.article_gen_lm = ClaudeModel(
            model=self.article_gen_lm, max_tokens=700, **self.claude_kwargs
        )
        self.article_polish_lm = ClaudeModel(
            model=self.polish_lm, max_tokens=4000, **self.claude_kwargs
        )

        lm_configs.set_conv_simulator_lm(self.conv_simulator_lm)
        lm_configs.set_question_asker_lm(self.question_asker_lm)
        lm_configs.set_outline_gen_lm(self.outline_gen_lm)
        lm_configs.set_article_gen_lm(self.article_gen_lm)
        lm_configs.set_article_polish_lm(self.article_polish_lm)
