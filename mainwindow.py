from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMainWindow, QToolBar

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Custom MainWindow")

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)

        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        menu_bar.addMenu("Window")
        menu_bar.addMenu("Setting")
        menu_bar.addMenu("Help")


        # Working with toolbars
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)

        #Add the quit action to the toolbar
        toolbar.addAction(quit_action)

        action1 = QAction("Some Action", self)
        action1.setStatusTip("Status message for some action") #tooltip
        action1.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action1)

        action2 = QAction(QIcon("start.png"), "Some other action", self)
        action2.setStatusTip("Status message for some other action")
        action2.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action2)

    def quit_app(self):
        self.app.quit()

    def toolbar_button_click(self):
        print("action triggered")