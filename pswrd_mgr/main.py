import os, sys, shutil, json, pickle
from typing import Optional, Dict, List

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QStyle, QDesktopWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QPushButton, QListWidget, QLabel, QListWidgetItem, QTreeView, QScrollArea, QMenu, QMessageBox, QColorDialog, QDialog, QTabWidget
from PyQt5.QtCore import Qt, QDir, QFile, QUrl, QSize
from PyQt5.QtGui import QIcon, QPixmap, QFont, QColor, QStandardItemModel, QStandardItem

from credential_tabs import CredentialTabs
from credential_list import CredentialList, CredentialItem
from messages import ErrorMessage
from config import Config
from settings import SettingsWindow

class Main(QMainWindow):
    def __init__(self, parent: QWidget = None) -> None:
        super(Main, self).__init__(parent)

        self.build()

    def build(self) -> None:
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        self.main_layoutH = QHBoxLayout()
        self.main_widget.setLayout(self.main_layoutH)

        self.selection_layoutV = QVBoxLayout()
        self.main_layoutH.addLayout(self.selection_layoutV)

        self.settings_button = QPushButton()
        self.settings_button.setObjectName("settings")
        self.settings_button.clicked.connect(self.exec_settings)
        self.selection_layoutV.addWidget(self.settings_button)

        self.cred_list = CredentialList(self)
        self.selection_layoutV.addWidget(self.cred_list)

        self.quick_action_layout = QHBoxLayout()
        self.selection_layoutV.addLayout(self.quick_action_layout)

        self.create_folder_button = QPushButton()
        self.create_folder_button.setObjectName("create_f")
        self.quick_action_layout.addWidget(self.create_folder_button)

        self.create_cred_button = QPushButton()
        self.create_cred_button.setObjectName("create_f")
        self.quick_action_layout.addWidget(self.create_cred_button)

        self.cred_tabs = CredentialTabs(self)
        self.main_layoutH.addWidget(self.cred_tabs)
        self.load_config(True)

    def exec_settings(self):
        if SettingsWindow(self).exec_() == QDialog.Accepted:
            self.load_config()

    def load_config(self, start_up = False):
        config = Config()

        self.setWindowTitle(config.config_dict["window_title"])
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_TitleBarMenuButton))
        if config.config_dict["window_auto_resolution"]:
            size_object = QDesktopWidget().screenGeometry(-1)
            width = int(size_object.width() / 3)
            height = int(size_object.height() / 2)
        else:
            width = config.config_dict["window_width"]
            height = config.config_dict["window_height"]

        if config.config_dict["window_fixed_resolution"]:
            self.setFixedSize(width, height)
        else:
            self.setMinimumSize(0, 0)
            self.setMaximumSize(16777215, 16777215)
            self.resize(width, height)

        if config.config_dict["show_welcome_tab_on_start"] and start_up:
            self.cred_tabs.append_welcome_tab()

        self.settings_button.setText("Settings")
        self.create_folder_button.setText("Create Folder")
        self.create_cred_button.setText("Create Credential")

        font = self.font()
        font.setPointSize(config.config_dict["font_size"])
        QApplication.instance().setFont(font)

        self.cred_list.load_creds(config)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())