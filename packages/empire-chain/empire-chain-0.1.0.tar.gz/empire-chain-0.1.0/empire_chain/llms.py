from openai import OpenAI
from anthropic import Anthropic

class LLM:
    def __init__(self, model: str):
        self.model = model

    def generate(self, prompt: str) -> str:
        pass

class OpenAILLM(LLM):
    def __init__(self, model: str):
        super().__init__(model)
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def generate(self, prompt: str) -> str:
        response = self.client.chat.completions.create(model=self.model, messages=[{"role": "user", "content": prompt}])
        return response.choices[0].message.content

class AnthropicLLM(LLM):
    def __init__(self, model: str):
        super().__init__(model)
        self.client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    def generate(self, prompt: str) -> str:
        response = self.client.messages.create(model=self.model, messages=[{"role": "user", "content": prompt}])
        return response.content[0].text