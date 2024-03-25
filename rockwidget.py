from PySide6.QtWidgets import QPushButton, QWidget, QHBoxLayout, QVBoxLayout

class RockWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RockWidget")

        button1 = QPushButton("Button1")
        button1.clicked.connect(self.button1_clicked)
        button2 = QPushButton("Button2")
        button2.clicked.connect(self.button2_clicked)

        #widget_layout = QHBoxLayout() #Horizontal
        widget_layout = QVBoxLayout() #Vertical
        widget_layout.addWidget(button1)
        widget_layout.addwidget(button2)
        self.setLayout(widget_layout)