import pickle, os, json
from cryptography.fernet import Fernet

class Config:
    def __init__(self):
        home_dir = os.path.expanduser('~')
        mgr_dir = os.path.join(home_dir, ".cred_mgr")
        os.makedirs(mgr_dir) if not os.path.exists(mgr_dir) else ...
        config_file = os.path.join(mgr_dir, "config.dat")
        self.config_dict = {
            "font_size": 10,
            "folder_color": (255, 0, 0),
            "credential_color": (0, 255, 0),
            "password_length": 16,
            "only_digits": False,
            "include_special_characters": True
        }
        # color = QColorDialog.getColor()
        # if color.isValid():
        #     print("Выбранный цвет:", color.getRgb())
        try:
            with open(file=config_file, mode="rb") as config:
                self.config_dict = pickle.load(config)
        except FileNotFoundError:
            with open(file=config_file, mode="xb") as config:
                pickle.dump(self.config_dict, config, protocol = 5)
        except EOFError:
            ErrorMessage(self, "file corrupted", "Can't read file. File would be replaced by new file.")
            os.remove(config_file)
            with open(file=config_file, mode="xb") as config:
                pickle.dump(self.config_dict, config, protocol = 2)
        except pickle.UnpicklingError:
            ErrorMessage(self, "file corrupted", "Can't read file. File would be replaced by new file.")
            os.remove(config_file)
            with open(file=config_file, mode="xb") as config:
                pickle.dump(self.config_dict, config, protocol = 2)