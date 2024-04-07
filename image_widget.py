from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton

class ImageWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLabelImageDemo")

        image_label = QLabel()
        image_label.setPixmap(QPixmap("ragnarokship.jpg"))

        layout = QVBoxLayout()
        layout.addWidget(image_label)

        self.setLayout(layout)