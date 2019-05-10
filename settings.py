# settings.py
import os
from pathlib import Path  # python3 only
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


CLIENT_SECRET = os.getenv('CLIENT_SECRET')
CLIENT_ID = os.getenv('CLIENT_ID')
USER_AGENT = os.getenv('USER_AGENT')
