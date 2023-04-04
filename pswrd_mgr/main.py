import os, sys, shutil, json, pickle
from typing import Optional, Dict, List

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QStyle, QDesktopWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QPushButton, QListWidget, QLabel, QListWidgetItem, QTreeView, QScrollArea, QMenu, QMessageBox, QColorDialog
from PyQt5.QtCore import Qt, QDir, QFile, QUrl, QSize
from PyQt5.QtGui import QIcon, QPixmap, QFont, QColor, QStandardItemModel, QStandardItem

from credential_widget import CredentialWidget
from credential_list import CredentialList, CredentialItem

class ErrorMessage(QMessageBox):
    def __init__(self, parent: QWidget = None, error_title: str = "", error_text: str = "", error_description: str = "") -> None:
        super(ErrorMessage, self).__init__(parent)

        self.setIcon(QMessageBox.Critical)
        self.setWindowTitle("Error " + error_title)
        self.setText(error_text)
        self.setInformativeText(error_description)
        self.exec_()


class Main(QMainWindow):
    def __init__(self, parent: QWidget = None) -> None:
        super(Main, self).__init__(parent)

        self.build()
        self.load_config()
        self.load_creds()

    def build(self) -> None:
        self.setWindowTitle("Credential Manager")
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_TitleBarMenuButton))
        size_object = QDesktopWidget().screenGeometry(-1)
        self.resize(int(size_object.width() / 3), int(size_object.height() / 2))

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        self.main_layoutH = QHBoxLayout()
        self.main_widget.setLayout(self.main_layoutH)

        self.selection_layoutV = QVBoxLayout()
        self.main_layoutH.addLayout(self.selection_layoutV)

        self.cred_list = CredentialList(self)

        self.selection_layoutV.addWidget(self.cred_list)

        self.quick_action_layout = QHBoxLayout()
        self.selection_layoutV.addLayout(self.quick_action_layout)

        self.create_folder_button = QPushButton()
        self.create_folder_button.setText("Create Folder")
        self.quick_action_layout.addWidget(self.create_folder_button)

        self.create_cred_button = QPushButton()
        self.create_cred_button.setText("Create Credential")
        self.quick_action_layout.addWidget(self.create_cred_button)

        self.action_layoutV = QVBoxLayout()
        self.main_layoutH.addLayout(self.action_layoutV)

        self.name_bar = QLabel()
        self.name_bar.setText("Choose credential...")
        self.action_layoutV.addWidget(self.name_bar)

        self.action_widget = CredentialWidget()
        self.action_widget.setHidden(True)
        self.action_layoutV.addWidget(self.action_widget)

    def load_config(self):
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
        font = self.font()
        font.setPointSize(10)
        QApplication.instance().setFont(font)

    def load_creds(self):
        test_folder = CredentialItem("Folder", 12, False, QColor(*self.config_dict["folder_color"]))
        self.cred_list.canvas.appendRow(test_folder)

        test1 = CredentialItem("Credential", 12, False, QColor(*self.config_dict["credential_color"]))
        test_folder.appendRow(test1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())