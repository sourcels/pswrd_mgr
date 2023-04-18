import os, sys, shutil, json
from typing import Optional, Dict, List

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QStyle, QDesktopWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QPushButton, QListWidget, QLabel, QListWidgetItem, QTreeView, QScrollArea, QLineEdit
from PyQt5.QtCore import Qt, QDir, QFile, QUrl, QSize
from PyQt5.QtGui import QIcon, QPixmap, QFont, QColor, QStandardItemModel, QStandardItem

DEFAULT_SAVE_ITEM = {

}

class CredentialWidget(QWidget):
    def __init__(self, parent: QWidget = None, save = DEFAULT_SAVE_ITEM):
        super(CredentialWidget, self).__init__(parent)

        self.save = save

        self.build()

    def build(self):
        self.main_layoutV = QVBoxLayout()
        self.setLayout(self.main_layoutV)
        self.append_line_edit_field("Login", "")


    def append_line_edit_field(self, text_label: str, text_input: str):
        def copy_text():
            text = line_edit_field_input.text()
            QApplication.clipboard().setText(text)
            
        line_edit_field_widget = QWidget()
        self.main_layoutV.addWidget(line_edit_field_widget)
        line_edit_field_layoutH = QHBoxLayout()
        line_edit_field_widget.setLayout(line_edit_field_layoutH)

        line_edit_field_label = QLabel()
        line_edit_field_label.setText(text_label)
        line_edit_field_layoutH.addWidget(line_edit_field_label)

        line_edit_field_input = QLineEdit()
        line_edit_field_input.setText(text_input)
        #line_edit_field_input.setMaxLength(32)
        line_edit_field_layoutH.addWidget(line_edit_field_input)

        line_edit_field_copy_button = QPushButton()
        line_edit_field_copy_button.setObjectName("")
        line_edit_field_copy_button.setIcon(self.style().standardIcon(QStyle.SP_TitleBarNormalButton))
        line_edit_field_copy_button.clicked.connect(copy_text)
        line_edit_field_layoutH.addWidget(line_edit_field_copy_button)
