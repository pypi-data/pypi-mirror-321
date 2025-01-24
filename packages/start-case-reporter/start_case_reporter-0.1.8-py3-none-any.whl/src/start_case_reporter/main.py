import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QHBoxLayout


def prepare_form_data(prefix, fullname, position):
    print(f"Prefix: {prefix}, Full Name: {fullname}, Position: {position}")


class MainApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Case Reporter")
        self.setGeometry(100, 100, 500, 100)

        layout = QVBoxLayout()

        person_1 = QHBoxLayout()
        self.txt_prefix_1 = QLineEdit(self)
        self.txt_prefix_1.setPlaceholderText("คำนำหน้า")
        self.txt_fullname_1 = QLineEdit(self)
        self.txt_fullname_1.setPlaceholderText("ชื่อ - นามสกุล")
        self.txt_position_1 = QLineEdit(self)
        self.txt_position_1.setPlaceholderText("ตำแหน่ง")

        person_1.addWidget(self.txt_prefix_1)
        person_1.addWidget(self.txt_fullname_1)
        person_1.addWidget(self.txt_position_1)

        person_1.setSpacing(10)

        submit_button = QPushButton("Start process", self)
        submit_button.clicked.connect(self.on_submit_click)

        layout.addLayout(person_1)
        layout.addWidget(submit_button)

        self.setLayout(layout)

    def on_submit_click(self):
        txt_prefix_1 = self.txt_prefix_1.text()
        txt_fullname_1 = self.txt_fullname_1.text()
        txt_position_1 = self.txt_position_1.text()
        prepare_form_data(txt_prefix_1, txt_fullname_1, txt_position_1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
