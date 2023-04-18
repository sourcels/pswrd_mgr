import os, sys, shutil, json, pickle
from typing import Optional, Dict, List

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QStyle, QDesktopWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QPushButton, QListWidget, QLabel, QListWidgetItem, QTreeView, QScrollArea, QMenu, QMessageBox, QColorDialog, QDialog, QTabWidget
from PyQt5.QtCore import Qt, QDir, QFile, QUrl, QSize
from PyQt5.QtGui import QIcon, QPixmap, QFont, QColor, QStandardItemModel, QStandardItem

from credential_widget import CredentialWidget

class CredentialTabs(QTabWidget):
    def __init__(self, parent: QWidget = None):
        super(CredentialTabs, self).__init__(parent)

        self.build()

    def build(self):
        self.setTabsClosable(True)
        self.setMovable(True)

        self.tabCloseRequested.connect(self.close_tab)

    def append_welcome_tab(self):
        main_widget = QWidget()
        main_layoutV = QVBoxLayout()
        main_widget.setLayout(main_layoutV)
        self.append_tab(main_widget, self.style().standardIcon(QStyle.SP_MessageBoxInformation), "Welcome!")

    def append_tab(self, tab_widget, icon_tab, tab_name):
        self.addTab(tab_widget, icon_tab, tab_name)
        self.setCurrentWidget(tab_widget)

    def close_tab(self, index):
        self.removeTab(index)