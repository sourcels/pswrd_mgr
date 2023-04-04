from PyQt5.QtWidgets import QMessageBox, QWidget

class ErrorMessage(QMessageBox):
    def __init__(self, parent: QWidget = None, error_title: str = "", error_text: str = "", error_description: str = "") -> None:
        super(ErrorMessage, self).__init__(parent)

        self.setIcon(QMessageBox.Critical)
        self.setWindowTitle("Error " + error_title)
        self.setText(error_text)
        self.setInformativeText(error_description)
        self.exec_()