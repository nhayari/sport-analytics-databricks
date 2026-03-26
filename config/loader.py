import os

#  !! by défaut  dev !!
env = os.getenv("ENV", "dev")  

if env == "prod":
    from .prod import *
else:
    from .dev import *