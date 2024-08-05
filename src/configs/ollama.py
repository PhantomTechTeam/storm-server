import os
from knowledge_storm import OllamaClient
class OllamaConfig: 
    def __init__(self):
        self.model = os.environ.get("OLLAMA_MODEL", "llama3:8b")
        self.port = os.environ.get("OLLAMA_PORT", 11434)
        self.url = os.environ.get("OLLAMA_URL", "http://localhost")
        self.ollama_kwargs = {
            "model": self.model,
            "port": self.port,
            "url": self.url,
            "stop":  ("\n\n---",) 
        }
        conv_simulator_lm = OllamaClient(max_tokens=500, **self.ollama_kwargs)
        question_asker_lm = OllamaClient(max_tokens=500, **self.ollama_kwargs)
        outline_gen_lm = OllamaClient(max_tokens=400, **self.ollama_kwargs)
        article_gen_lm = OllamaClient(max_tokens=700, **self.ollama_kwargs)
        article_polish_lm = OllamaClient(max_tokens=4000, **self.ollama_kwargs)
