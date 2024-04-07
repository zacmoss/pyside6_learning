from PySide6.QtWidgets import QApplication
from text_edit_widget import TextEditWidget
import sys

app = QApplication(sys.argv)

widget = TextEditWidget()
widget.show()

app.exec()