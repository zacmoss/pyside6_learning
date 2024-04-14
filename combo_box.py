from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QComboBox, QPushButton

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QComboBox Demo")

        self.combo_box = QComboBox(self)

        #Add planets to the combobox
        self.combo_box.addItem("Tatooine")
        self.combo_box.addItem("Utapau")
        self.combo_box.addItem("Kashhyk")
        self.combo_box.addItem("Tantis")
        self.combo_box.addItem("Coruscant")

        button_current_value = QPushButton("Current Value")
        button_current_value.clicked.connect(self.current_value)
        button_set_current = QPushButton("Set Value")
        button_set_current.clicked.connect(self.set_current)
        button_get_values = QPushButton("Get values")
        button_get_values.clicked.connect(self.get_values)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.combo_box)
        v_layout.addWidget(button_current_value)
        v_layout.addWidget(button_set_current)
        v_layout.addWidget(button_get_values)

        self.setLayout(v_layout)

    def current_value(self):
        print("Current item : ", self.combo_box.currentText(), " - current index : ", self.combo_box.currentIndex())
    
    def set_current(self):
        self.combo_box.setCurrentIndex(2)

    def get_values(self):
        for i in range(self.combo_box.count()):
            print("index [ ", i, "] : ", self.combo_box.itemText(i))