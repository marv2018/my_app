from PyQt5.QtWidgets import QMainWindow
from resources.view.main_window_ui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        # Show the form
        self.show()
