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

# print(toggl.projects)
print([client["name"] for client in toggl.clients])
print([project["name"] for project in toggl.active_projects])
print([tag["name"] for tag in toggl.tags])

# print(pixela.get_graphs())