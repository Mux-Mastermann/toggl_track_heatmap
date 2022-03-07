#----------------------------------- INIT --------------------------------------------#

# Importing Modules
import os
from dotenv import load_dotenv
from pixela import Pixela
from toggl import Toggl

# setup 
load_dotenv()

toggl = Toggl(os.getenv("toggl_token"))

pixela = Pixela(os.getenv("pixela_username"), os.getenv("pixela_token"))

#----------------------------------- EXEC ---------------------------------------------#

print(toggl.get_tracked_time())