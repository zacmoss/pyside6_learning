#import sys
#from PySide6.QtWidgets import QApplication, QPushButton
#from button_holder import ButtonHolder

#from PySide6.QtCore import Qt
#from PySide6.QtWidgets import QApplication, QSlider

"""
app = QApplication(sys.argv)

window = ButtonHolder()
window.show()

# Start event loop
app.exec()
"""

"""
def button_clicked(data):
    print("You clicked the button, didn't you! checked : ", data)

app = QApplication()
button = QPushButton("Press Me")
button.setCheckable(True)

button.clicked.connect(button_clicked)

button.show()
app.exec()
"""

""""
def respond_to_slider(data):
    print("slider moved to:", data)

app = QApplication()
slider = QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(25)

slider.valueChanged.connect(respond_to_slider)
slider.show()
app.exec()
"""

from PySide6.QtWidgets import QApplication
from rockwidget import RockWidget
import sys

app = QApplication(sys.argv)

widget = RockWidget()
widget.show()
app.exec()