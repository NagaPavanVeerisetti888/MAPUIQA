from dotenv import load_dotenv
import os

#  Load environment variables from .env file
load_dotenv()

# Configuration class to encapsulate environment variables
class Config:
    BASE_URL = os.getenv('BASE_URL', 'https://map-dev-ui.azurewebsites.net/')
    BROWSER = os.getenv('BROWSER', 'chrome')