from PySide6.QtWidgets import QApplication
from combo_box import Widget
import sys

app = QApplication(sys.argv)

# Set stylesheet on entire application
#app.setStyleSheet("QPushButton{color: red ; background-color : white;}")

# Open the css styles file and read in the css-alike styling code
with open('styles/style.css', 'r') as f:
    style = f.read()
    # Set the stylesheet of the application
    app.setStyleSheet(style)

widget = Widget()
widget.show()

app.exec()