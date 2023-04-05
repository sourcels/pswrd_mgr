import os, sys, shutil, json, pickle
from typing import Optional, Dict, List

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QStyle, QDesktopWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QPushButton, QListWidget, QLabel, QListWidgetItem, QTreeView, QScrollArea, QMenu, QMessageBox, QColorDialog, QDialog, QSpinBox, QCheckBox
from PyQt5.QtCore import Qt, QDir, QFile, QUrl, QSize
from PyQt5.QtGui import QIcon, QPixmap, QFont, QColor, QStandardItemModel, QStandardItem

from config import DEFAULT_CONFIG

class SettingsWindow(QDialog):
    def __init__(self, parent: QWidget = None, config_dict = DEFAULT_CONFIG):
        super(SettingsWindow, self).__init__(parent)

        self.config_dict = config_dict

        self.build()
        self.load()
        self.exec_()

    def build(self):
        self.main_layoutV = QVBoxLayout()
        self.setLayout(self.main_layoutV)

        self.main_app_label = QLabel()
        self.main_app_label.setAlignment(Qt.AlignCenter)
        self.main_layoutV.addWidget(self.main_app_label)

        self.font_size_layout = QHBoxLayout()
        self.main_layoutV.addLayout(self.font_size_layout)

        self.font_size_label = QLabel()
        self.font_size_layout.addWidget(self.font_size_label)

        self.font_size_input = QSpinBox()
        self.font_size_input.setRange(4, 20)
        self.font_size_layout.addWidget(self.font_size_input)

        self.folder_color_layout = QHBoxLayout()
        self.main_layoutV.addLayout(self.folder_color_layout)

        self.folder_color_label = QLabel()
        self.folder_color_layout.addWidget(self.folder_color_label)

        self.folder_color_input = QPushButton()
        self.folder_color_input.setObjectName("foldercolor")
        self.folder_color_input.clicked.connect(self.choose_color)
        self.folder_color_layout.addWidget(self.folder_color_input)

        self.credential_color_layout = QHBoxLayout()
        self.main_layoutV.addLayout(self.credential_color_layout)

        self.credential_color_label = QLabel()
        self.credential_color_layout.addWidget(self.credential_color_label)

        self.credential_color_input = QPushButton()
        self.credential_color_input.setObjectName("credcolor")
        self.credential_color_input.clicked.connect(self.choose_color)
        self.credential_color_layout.addWidget(self.credential_color_input)

        self.random_password_generator_label = QLabel()
        self.random_password_generator_label.setAlignment(Qt.AlignCenter)
        self.main_layoutV.addWidget(self.random_password_generator_label)

        self.password_length_layout = QHBoxLayout()
        self.main_layoutV.addLayout(self.password_length_layout)

        self.password_length_label = QLabel()
        self.password_length_layout.addWidget(self.password_length_label)

        self.password_length_input = QSpinBox()
        self.password_length_input.setRange(1, 100)
        self.password_length_layout.addWidget(self.password_length_input)

        self.only_digits_layout = QHBoxLayout()
        self.main_layoutV.addLayout(self.only_digits_layout)

        self.only_digits_label = QLabel()
        self.only_digits_layout.addWidget(self.only_digits_label)

        self.only_digits_input = QCheckBox()
        self.only_digits_layout.addWidget(self.only_digits_input)

        self.include_special_characters_layout = QHBoxLayout()
        self.main_layoutV.addLayout(self.include_special_characters_layout)

        self.include_special_characters_label = QLabel()
        self.include_special_characters_layout.addWidget(self.include_special_characters_label)

        self.include_special_characters_input = QCheckBox()
        self.include_special_characters_layout.addWidget(self.include_special_characters_input)


    def choose_color(self):
        sender = self.sender()
        sender_name = sender.objectName()
        if sender_name == "foldercolor":
            self.folder_color = QColorDialog.getColor(self.folder_color, self).getRgb()
        elif sender_name == "credcolor":
            self.cred_color = QColorDialog.getColor(self.cred_color, self).getRgb()

    def load(self):
        self.setWindowTitle("Credential Manager Settings")
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.main_app_label.setText("App settings")
        self.font_size = self.config_dict["font_size"]
        self.folder_color = QColor(*self.config_dict["folder_color"])
        self.cred_color = QColor(*self.config_dict["credential_color"])
        self.font_size_label.setText("Font Size:")
        self.font_size_input.setValue(self.font_size)
        self.folder_color_label.setText("Folder Color:")
        self.folder_color_input.setText("Choose color...")
        self.credential_color_label.setText("Credential Color:")
        self.credential_color_input.setText("Choose color...")
        self.random_password_generator_label.setText("Password Generator settings")
        self.password_length_label.setText("Password Length:")
        self.password_length_input.setValue(self.config_dict["password_length"])
        self.only_digits_label.setText("Include only digits:")
        self.only_digits_input.setChecked(self.config_dict["only_digits"])
        self.include_special_characters_label.setText("Include special characters:")
        self.include_special_characters_input.setChecked(self.config_dict["include_special_characters"])