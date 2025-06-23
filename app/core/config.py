import os
from dotenv import load_dotenv

# Load environment variables from a .env file into the environment
load_dotenv()

class Settings:
    # Fetch OpenAI API key from environment variables
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")

# Create an instance of Settings to access config values throughout the app
settings = Settings()
