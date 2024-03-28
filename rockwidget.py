from PySide6.QtWidgets import QPushButton, QWidget, QHBoxLayout, QVBoxLayout

class RockWidget(QWidget):
    def __init__(self):
        super().__init__() # super is used to call methods from the parent class (QWidget)
        self.setWindowTitle("RockWidget")

        button1 = QPushButton("Button1")
        button1.clicked.connect(self.button1_clicked)
        button2 = QPushButton("Button2")
        button2.clicked.connect(self.button2_clicked)

        #widget_layout = QHBoxLayout() #Layout Horizontal
        widget_layout = QVBoxLayout() #Layout Vertical
        widget_layout.addWidget(button1)
        widget_layout.addWidget(button2)
        self.setLayout(widget_layout)

    def button1_clicked(self):
        print("Button1 Clicked")

    def button2_clicked(self):
        print("Button2 Clicked")