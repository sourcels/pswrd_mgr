import os, sys, shutil, json
from typing import Optional, Dict, List

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QStyle, QDesktopWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QPushButton, QListWidget, QLabel, QListWidgetItem, QTreeView, QScrollArea
from PyQt5.QtCore import Qt, QDir, QFile, QUrl, QSize
from PyQt5.QtGui import QIcon, QPixmap, QFont, QColor, QStandardItemModel, QStandardItem

class CredentialWidget(QWidget):
    def __init__(self):
        super(CredentialWidget, self).__init__()

    def build(self):
        ...

    def init_cred(self):
        ...