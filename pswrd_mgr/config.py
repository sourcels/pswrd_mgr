import pickle, os, json
from cryptography.fernet import Fernet
from messages import ErrorMessage

DEFAULT_CONFIG = {
    "font_size": 10,
    "folder_color": (255, 0, 0),
    "credential_color": (255, 255, 0),
    "password_length": 16,
    "only_digits": False,
    "include_special_characters": True
}

class Config:
    def __init__(self):

        self.config_dict = self.load()

    def load(self):
        home_dir = os.path.expanduser('~')
        mgr_dir = os.path.join(home_dir, ".cred_mgr")
        os.makedirs(mgr_dir) if not os.path.exists(mgr_dir) else ...
        config_file = os.path.join(mgr_dir, "config.dat")
        config_dict = DEFAULT_CONFIG
        try:
            with open(file=config_file, mode="rb") as config:
                config_dict = pickle.load(config)
        except FileNotFoundError:
            with open(file=config_file, mode="xb") as config:
                pickle.dump(config_dict, config, protocol = 5)
        except pickle.UnpicklingError or MemoryError or EOFError:
            ErrorMessage(None, "file corrupted", "Can't read file. File would be replaced by new file.")
            #os.remove(config_file)
            with open(file=config_file, mode="wb") as config:
                pickle.dump(config_dict, config, protocol = 2)

        return config_dict