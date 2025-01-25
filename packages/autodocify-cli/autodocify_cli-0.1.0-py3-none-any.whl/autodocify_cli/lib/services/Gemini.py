import google.generativeai as genai
from autodocify_cli.core.settings import settings


class GeminiService:
    def __init__(self, prompt):
        self.prompt = prompt
        genai.configure(api_key=settings.GEMINI_API_KEY)
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction="You are a professional software developer",
        )

    def run(self) -> None:
        response = self.model.generate_content(self.prompt)
        return response.text
