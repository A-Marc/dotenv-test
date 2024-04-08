from dotenv import load_dotenv
import os 
load_dotenv()
key = os.getenv("API_KEY")
print(key)
