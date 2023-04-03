import os, sys, shutil, json
from typing import Optional, Dict, List

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QStyle, QDesktopWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QPushButton, QListWidget, QLabel, QListWidgetItem, QTreeView, QScrollArea, QMenu
from PyQt5.QtCore import Qt, QDir, QFile, QUrl, QSize
from PyQt5.QtGui import QIcon, QPixmap, QFont, QColor, QStandardItemModel, QStandardItem

from credential_widget import CredentialWidget

class StandardItem(QStandardItem):
    def __init__(self, txt='', font_size=12, set_bold=False, color=QColor(0, 0, 0)):
        super(StandardItem, self).__init__()
        font_style = QFont('Open Sans', font_size)
        font_style.setBold(set_bold)

        self.setEditable(False)
        self.setForeground(color)
        self.setFont(font_style)
        self.setText(txt)

class CredentialList(QTreeView):
    def __init__(self):
        super(CredentialList, self).__init__()

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


class Main(QMainWindow):
    def __init__(self, parent: QWidget = None) -> None:
        super(Main, self).__init__(parent)

        self.build()

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

        self.cred_list = CredentialList()

        # ----
        test = StandardItem("test", 12, False, QColor(0, 0, 0))
        test1 = StandardItem("test1", 12, False, QColor(0, 0, 0))
        test.appendRow(test1)
        self.cred_list.canvas.appendRow(test)
        # ----

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())