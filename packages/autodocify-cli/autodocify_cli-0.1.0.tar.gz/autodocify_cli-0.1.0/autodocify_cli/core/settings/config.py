import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    GEMINI_API_KEY: str
    OPENAI_API_KEY: str
    OPENAI_MODEL: str

    class Config:
        env_file = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "core\env_files", ".env"
        )

        print(env_file)
        env_file_encoding = "utf-8"


settings = Settings()
