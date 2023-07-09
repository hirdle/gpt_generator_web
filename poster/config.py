from dotenv import load_dotenv
import os

load_dotenv()

API_TOKEN_OPENAI = os.getenv('API_TOKEN_OPENAI')
API_TOKEN_TELEGRAM = os.getenv('API_TOKEN_TELEGRAM')
API_TOKEN_VK = os.getenv('API_TOKEN_VK')