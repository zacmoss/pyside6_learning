from PySide6.QtWidgets import QApplication
from image_widget import ImageWidget
import sys

app = QApplication(sys.argv)

widget = ImageWidget()
widget.show()

app.exec()