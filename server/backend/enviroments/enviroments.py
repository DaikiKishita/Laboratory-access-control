import os
from dotenv import load_dotenv


load_dotenv()
host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv("db")
webhook=os.getenv("webhook")