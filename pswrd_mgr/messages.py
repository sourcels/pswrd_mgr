from PyQt5.QtWidgets import QMessageBox, QWidget

class ErrorMessage(QMessageBox):
    def __init__(self, parent: QWidget = None, error_title: str = "", error_text: str = "", error_description: str = "") -> None:
        super(ErrorMessage, self).__init__(parent)

        self.setIcon(QMessageBox.Critical)
        self.setWindowTitle("Error " + error_title)
        self.setText(error_text)
        self.setInformativeText(error_description)
        self.setStandardButtons(QMessageBox.Ok)
        self.exec_()

class QuestionMessage(QMessageBox):
    def __init__(self, parent: QWidget = None, question_title: str = "", question_text: str = "", question_description: str = "") -> None:
        super(QuestionMessage, self).__init__(parent)

        self.setIcon(QMessageBox.Question)
        self.setWindowTitle(question_title)
        self.setText(question_text)
        self.setInformativeText(question_description)
        self.setStandardButtons(QMessageBox.Yes | QMessageBox.No)