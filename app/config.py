import os
from dotenv import load_dotenv

# Load environmental variables from .env
load_dotenv()

class Config:
    
    # SECRET_KEY
    SECRET_KEY = os.getenv('SECRET_KEY') or "TEST_SECRET_KEY_IBVL_PIP12"

    # OUTPUT_FOLDER
    OUTPUT_FOLDER = os.getenv('OUTPUT_FOLDER', 'output')
    # OUTPUT_FOLDER = os.path.join(os.getcwd(), os.getenv('OUTPUT_FOLDER', 'output'))

    # Ensure output folder exists
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)