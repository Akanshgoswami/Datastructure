import json
import sys

class Settings:
    available_settings = {
        "node_name",
        "node_is_master",
        "node_version",
        "node_host",
        "node_port",
        "node_slaves"
    }

    def __init__(self):
        try:
            settings_config = sys.argv[1]
        except IndexError as exec:
            print("No config found ", exec)
            return
        print(settings_config)

settings = Settings()







