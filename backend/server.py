from threading import Thread

import json

class Server:
    def __init__(self) -> None:
        try:
            print("Loading data.json")
        except (json.decoder.JSONDecodeError, FileNotFoundError):
            print("data.json is empty. Setting up data.json")
            self.setup()