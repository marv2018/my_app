import sys

from PyQt5.QtWidgets import QApplication
from my_app.resources.view.main_window import MainWindow
from my_app.meta_info import __app_version__, __app_name__

class App(QApplication):
    def __init__(self, sys_argv):
        self.setApplicationVersion(__app_version__)
        self.setApplicationDisplayName(f"{__app_name__} {__app_version__}")

        QApplication.__init__(self, sys_argv)
        self.main_view = MainWindow()


if __name__ == "__main__":
    app = App(sys.argv)
    sys.exit(app.exec_())
