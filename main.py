import os
from pixela import Pixela
from dotenv import load_dotenv

load_dotenv()

pixela_username = os.getenv("pixela_username")
pixela_token = os.getenv("pixela_token")

pixela = Pixela(pixela_username, pixela_token)

print(pixela.create_user())