import os, sys, shutil, json
from typing import Optional, Dict, List

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QStyle, QDesktopWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QPushButton, QListWidget, QLabel, QListWidgetItem, QTreeView, QScrollArea, QMenu
from PyQt5.QtCore import Qt, QDir, QFile, QUrl, QSize
from PyQt5.QtGui import QIcon, QPixmap, QFont, QColor, QStandardItemModel, QStandardItem

class CredentialItem(QStandardItem):
    def __init__(self, txt='', font_size=12, set_bold=False, color=QColor(0, 0, 0)):
        super(CredentialItem, self).__init__()
        font_style = QFont('Open Sans', font_size)
        font_style.setBold(set_bold)

        self.setEditable(False)
        self.setForeground(color)
        self.setFont(font_style)
        self.setText(txt)

class CredentialList(QTreeView):
    def __init__(self, parent: QWidget):
        super(CredentialList, self).__init__(parent)

        self.setHeaderHidden(True)

        self.model_obj = QStandardItemModel()
        self.canvas = self.model_obj.invisibleRootItem()
        self.setModel(self.model_obj)

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.openMenu)

        self.clicked.connect(self.clicked_function)
        self.doubleClicked.connect(self.double_clicked_function)

    def clicked_function(self, val):
        print("clicked " + val.data())

    def double_clicked_function(self, val):
        print("double clicked", val.data())

    def delete_all(self):
        self.model_obj.removeRows(0, self.model_obj.rowCount())

    def openMenu(self, position):
        indexes = self.selectedIndexes()
        if len(indexes) > 0:
            level = 0
            index = indexes[0]
            while index.parent().isValid():
                index = index.parent()
                level += 1
        
        menu = QMenu()
        if level == 0:
            menu.addAction(self.tr("Edit 1"))
        elif level == 1:
            menu.addAction(self.tr("Edit 2"))
        elif level == 2:
            menu.addAction(self.tr("Edit 3"))
        
        menu.exec_(self.viewport().mapToGlobal(position))