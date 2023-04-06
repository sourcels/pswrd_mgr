import pickle, os, json
from cryptography.fernet import Fernet
from messages import ErrorMessage

DEFAULT_CONFIG = {
    "window_fixed_resolution": False,
    "window_auto_resolution": True,
    "window_width": 800,
    "window_height": 600,
    "font_size": 10,
    "folder_color": (255, 0, 0),
    "credential_color": (255, 255, 0),
    "password_length": 16,
    "only_digits": False,
    "include_special_characters": True
}

class Config:
    def __init__(self):

        self.config_dict = self.read_config_function()

    def read_config_function(self):
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
                pickle.dump(config_dict, config, protocol = 2)
        except pickle.UnpicklingError or MemoryError or EOFError:
            ErrorMessage(None, "file corrupted", "Can't read file. File would be replaced by new file.")
            with open(file=config_file, mode="wb") as config:
                pickle.dump(config_dict, config, protocol = 2)

        return config_dict

    def write_config_function(self, dict_to_save):
        home_dir = os.path.expanduser('~')
        mgr_dir = os.path.join(home_dir, ".cred_mgr")
        os.makedirs(mgr_dir) if not os.path.exists(mgr_dir) else ...
        config_file = os.path.join(mgr_dir, "config.dat")
        try:
            with open(file=config_file, mode="xb") as config:
                pickle.dump(dict_to_save, config, protocol = 2)
        except FileExistsError:
            with open(file=config_file, mode="wb") as config:
                pickle.dump(dict_to_save, config, protocol = 2)