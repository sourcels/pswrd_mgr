import os, sys, shutil, json, pickle
from typing import Optional, Dict, List

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QStyle, QDesktopWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QPushButton, QListWidget, QLabel, QListWidgetItem, QTreeView, QScrollArea, QMenu, QMessageBox, QColorDialog, QDialog, QSpinBox, QCheckBox
from PyQt5.QtCore import Qt, QDir, QFile, QUrl, QSize
from PyQt5.QtGui import QIcon, QPixmap, QFont, QColor, QStandardItemModel, QStandardItem

from config import Config
from messages import QuestionMessage

class SettingsWindow(QDialog):
    def __init__(self, parent: QWidget = None):
        super(SettingsWindow, self).__init__(parent)

        self.build()
        self.load_function()

    def build(self):
        self.main_layoutV = QVBoxLayout()
        self.setLayout(self.main_layoutV)

        self.main_app_label = QLabel()
        self.main_app_label.setAlignment(Qt.AlignCenter)
        self.main_layoutV.addWidget(self.main_app_label)


        self.window_fixed_resolution_layoutH = QHBoxLayout()
        self.main_layoutV.addLayout(self.window_fixed_resolution_layoutH)
        self.window_fixed_resolution_layoutH.addStretch()

        self.window_fixed_resolution_label = QLabel()
        self.window_fixed_resolution_layoutH.addWidget(self.window_fixed_resolution_label)

        self.window_fixed_resolution_input = QCheckBox()
        self.window_fixed_resolution_input.stateChanged.connect(self.input_changed)
        self.window_fixed_resolution_layoutH.addWidget(self.window_fixed_resolution_input)
        self.window_fixed_resolution_layoutH.addStretch()


        self.window_auto_resolution_layoutH = QHBoxLayout()
        self.main_layoutV.addLayout(self.window_auto_resolution_layoutH)
        self.window_auto_resolution_layoutH.addStretch()

        self.window_auto_resolution_label = QLabel()
        self.window_auto_resolution_layoutH.addWidget(self.window_auto_resolution_label)

        self.window_auto_resolution_input = QCheckBox()
        self.window_auto_resolution_input.stateChanged.connect(self.input_changed)
        self.window_auto_resolution_layoutH.addWidget(self.window_auto_resolution_input)
        self.window_auto_resolution_layoutH.addStretch()


        self.window_resolution_layoutH = QHBoxLayout()
        self.main_layoutV.addLayout(self.window_resolution_layoutH)
        self.window_resolution_layoutH.addStretch()

        self.window_resolution_label = QLabel()
        self.window_resolution_layoutH.addWidget(self.window_resolution_label)

        self.window_resolution_width_input = QSpinBox()
        self.window_resolution_width_input.setRange(800, 4096)
        self.window_resolution_width_input.valueChanged.connect(self.input_changed)
        self.window_resolution_layoutH.addWidget(self.window_resolution_width_input)

        self.window_resolution_height_input = QSpinBox()
        self.window_resolution_height_input.setRange(600, 2160)
        self.window_resolution_height_input.valueChanged.connect(self.input_changed)
        self.window_resolution_layoutH.addWidget(self.window_resolution_height_input)
        self.window_resolution_layoutH.addStretch()


        self.font_size_layoutH = QHBoxLayout()
        self.main_layoutV.addLayout(self.font_size_layoutH)
        self.font_size_layoutH.addStretch()

        self.font_size_label = QLabel()
        self.font_size_layoutH.addWidget(self.font_size_label)

        self.font_size_input = QSpinBox()
        self.font_size_input.setRange(4, 20)
        self.font_size_input.valueChanged.connect(self.input_changed)
        self.font_size_layoutH.addWidget(self.font_size_input)
        self.font_size_layoutH.addStretch()


        self.folder_color_layoutH = QHBoxLayout()
        self.main_layoutV.addLayout(self.folder_color_layoutH)
        self.folder_color_layoutH.addStretch()

        self.folder_color_label = QLabel()
        self.folder_color_layoutH.addWidget(self.folder_color_label)

        self.folder_color_output = QLabel()
        self.folder_color_output.setFixedSize(25, 25)
        self.folder_color_layoutH.addWidget(self.folder_color_output)

        self.folder_color_input = QPushButton()
        self.folder_color_input.setObjectName("foldercolor")
        self.folder_color_input.clicked.connect(self.choose_folder_color_function)
        self.folder_color_layoutH.addWidget(self.folder_color_input)
        self.folder_color_layoutH.addStretch()


        self.credential_color_layoutH = QHBoxLayout()
        self.main_layoutV.addLayout(self.credential_color_layoutH)
        self.credential_color_layoutH.addStretch()

        self.credential_color_label = QLabel()
        self.credential_color_layoutH.addWidget(self.credential_color_label)

        self.credential_color_output = QLabel()
        self.credential_color_output.setFixedSize(25, 25)
        self.credential_color_layoutH.addWidget(self.credential_color_output)

        self.credential_color_input = QPushButton()
        self.credential_color_input.setObjectName("credcolor")
        self.credential_color_input.clicked.connect(self.choose_credential_color_function)
        self.credential_color_layoutH.addWidget(self.credential_color_input)

        self.random_password_generator_label = QLabel()
        self.random_password_generator_label.setAlignment(Qt.AlignCenter)
        self.main_layoutV.addWidget(self.random_password_generator_label)
        self.credential_color_layoutH.addStretch()


        self.password_length_layoutH = QHBoxLayout()
        self.main_layoutV.addLayout(self.password_length_layoutH)
        self.password_length_layoutH.addStretch()

        self.password_length_label = QLabel()
        self.password_length_layoutH.addWidget(self.password_length_label)

        self.password_length_input = QSpinBox()
        self.password_length_input.setRange(1, 124)
        self.password_length_input.valueChanged.connect(self.input_changed)
        self.password_length_layoutH.addWidget(self.password_length_input)
        self.password_length_layoutH.addStretch()


        self.only_digits_layoutH = QHBoxLayout()
        self.main_layoutV.addLayout(self.only_digits_layoutH)
        self.only_digits_layoutH.addStretch()

        self.only_digits_label = QLabel()
        self.only_digits_layoutH.addWidget(self.only_digits_label)

        self.only_digits_input = QCheckBox()
        self.only_digits_input.stateChanged.connect(self.input_changed)
        self.only_digits_layoutH.addWidget(self.only_digits_input)
        self.only_digits_layoutH.addStretch()


        self.include_special_characters_layoutH = QHBoxLayout()
        self.main_layoutV.addLayout(self.include_special_characters_layoutH)
        self.include_special_characters_layoutH.addStretch()

        self.include_special_characters_label = QLabel()
        self.include_special_characters_layoutH.addWidget(self.include_special_characters_label)

        self.include_special_characters_input = QCheckBox()
        self.include_special_characters_input.stateChanged.connect(self.input_changed)
        self.include_special_characters_layoutH.addWidget(self.include_special_characters_input)
        self.include_special_characters_layoutH.addStretch()


        self.action_layoutH = QHBoxLayout()
        self.main_layoutV.addLayout(self.action_layoutH)
        self.action_layoutH.addStretch()

        self.save_button = QPushButton()
        self.save_button.setObjectName("save")
        self.save_button.clicked.connect(self.save_function)
        self.action_layoutH.addWidget(self.save_button)

        self.cancel_button = QPushButton()
        self.cancel_button.setObjectName("cancel")
        self.cancel_button.clicked.connect(self.cancel_function)
        self.action_layoutH.addWidget(self.cancel_button)
        self.action_layoutH.addStretch()

    def input_changed(self):
        self.save_button.setEnabled(True)

    def choose_folder_color_function(self):
        temp_color = QColorDialog.getColor(self.folder_color, self)
        if temp_color.isValid() and temp_color.getRgb() != self.folder_color.getRgb():
            self.folder_color = temp_color
            self.folder_color_output.setStyleSheet("background-color: " + self.folder_color.name())
            self.input_changed()

    def choose_credential_color_function(self):
        temp_color = QColorDialog.getColor(self.cred_color, self)
        if temp_color.isValid() and temp_color.getRgb() != self.cred_color.getRgb():
            self.cred_color = temp_color
            self.credential_color_output.setStyleSheet("background-color: " + self.cred_color.name())
            self.input_changed()

    def save_function(self):
        self.config_dict["window_fixed_resolution"] = self.window_fixed_resolution_input.isChecked()
        self.config_dict["window_auto_resolution"] = self.window_auto_resolution_input.isChecked()
        self.config_dict["window_width"] = self.window_resolution_width_input.value()
        self.config_dict["window_height"] = self.window_resolution_height_input.value()
        self.config_dict["font_size"] = self.font_size_input.value()
        self.config_dict["folder_color"] = self.folder_color.getRgb()
        self.config_dict["credential_color"] = self.cred_color.getRgb()
        self.config_dict["password_length"] = self.password_length_input.value()
        self.config_dict["only_digits"] = self.only_digits_input.isChecked()
        self.config_dict["include_special_characters"] = self.include_special_characters_input.isChecked()

        config = Config()
        config.write_config_function(self.config_dict)
        
        self.accept()

    def cancel_function(self):
        if self.save_button.isEnabled():
            question = QuestionMessage(self, "Cancel", "Cancel changes", "Are you sure to discard changes?")
            if question.exec_() == QMessageBox.Yes:
                self.reject()
        else:
            self.reject()

    def load_function(self):
        config = Config()
        self.config_dict = config.config_dict

        self.setWindowTitle("Credential Manager Settings")
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.main_app_label.setText("|" + "App settings" + "|")
        self.window_fixed_resolution_label.setText("Fixed window resolution")
        self.window_fixed_resolution_input.setChecked(self.config_dict["window_fixed_resolution"])
        self.window_auto_resolution_label.setText("Auto window resolution:")
        self.window_auto_resolution_input.setChecked(self.config_dict["window_auto_resolution"])
        self.window_resolution_label.setText("Window resolution (width, height)")
        self.window_resolution_width_input.setValue(self.config_dict["window_width"])
        self.window_resolution_height_input.setValue(self.config_dict["window_height"])
        self.font_size = self.config_dict["font_size"]
        self.folder_color = QColor(*self.config_dict["folder_color"])
        self.cred_color = QColor(*self.config_dict["credential_color"])
        self.font_size_label.setText("Font Size:")
        self.font_size_input.setValue(self.font_size)
        self.folder_color_label.setText("Folder Color:")
        self.folder_color_input.setText("Choose color...")
        self.folder_color_output.setStyleSheet("background-color: " + self.folder_color.name())
        self.credential_color_label.setText("Credential Color:")
        self.credential_color_input.setText("Choose color...")
        self.credential_color_output.setStyleSheet("background-color: " + self.cred_color.name())
        self.random_password_generator_label.setText("|" + "Password Generator settings" + "|")
        self.password_length_label.setText("Password Length:")
        self.password_length_input.setValue(self.config_dict["password_length"])
        self.only_digits_label.setText("Include only digits:")
        self.only_digits_input.setChecked(self.config_dict["only_digits"])
        self.include_special_characters_label.setText("Include special characters:")
        self.include_special_characters_input.setChecked(self.config_dict["include_special_characters"])
        self.save_button.setText("Save")
        self.save_button.setEnabled(False)
        self.cancel_button.setText("Cancel")
        font = self.font()
        font.setPointSize(self.config_dict["font_size"])
        QApplication.instance().setFont(font)