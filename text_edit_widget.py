from PySide6.QtWidgets import QWidget, QTextEdit, QHBoxLayout, QVBoxLayout, QPushButton

class TextEditWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QTextEditDemo")

        self.text_edit = QTextEdit()

        #Buttons
        copy_button = QPushButton("Copy")
        copy_button.clicked.connect(self.text_edit.copy) #Connect directly to QTextEdit slot

        cut_button = QPushButton("Cut")
        cut_button.clicked.connect(self.text_edit.cut)

        paste_button = QPushButton("Paste")
        paste_button.clicked.connect(self.text_edit.paste)

        undo_button = QPushButton("Undo")
        undo_button.clicked.connect(self.text_edit.undo)

        redo_button = QPushButton("Redo")
        redo_button.clicked.connect(self.text_edit.redo)

        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.text_edit.clear)


        h_layout = QHBoxLayout()
        h_layout.addWidget(copy_button)
        h_layout.addWidget(cut_button)
        h_layout.addWidget(paste_button)
        h_layout.addWidget(undo_button)
        h_layout.addWidget(redo_button)
        h_layout.addWidget(clear_button)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout) # stacks buttons bar (h_layout) on top of the editor window
        v_layout.addWidget(self.text_edit) # editor window

        self.setLayout(v_layout)