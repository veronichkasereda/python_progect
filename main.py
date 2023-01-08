import sys

import sys
import sqlite3
from PyQt5.Qt import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
from Desine_demo import Ui_Dialog


class MyWidget(QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_cliced_button)
        self.comboBox.currentTextChanged.connect(self.run)
        self.comboBox_2.currentTextChanged.connect(self.on_combobox_func1)
        self.comboBox.addItems(["Выбор предмета", "Планиметрия", "Тригонометрия"])
        self.comboBox_2.addItems(["Выбор формулы"])

    def run(self, text):
        self.current_text = text
        if self.current_text == "Планиметрия":
            self.comboBox_2.addItems(
                ["площадь прямоугольника", "площадь круга", "площадь трапеции",
                                  "площадь ромба", "площадь параллелограмма", "площадь прямоугольного треугольника",
                                  "площадь треугольника", "площадь квадрата"]
                                 )
        elif self.current_text == "Тригонометрия":
            self.comboBox_2.addItems(
                ["косинус", "синус", "тангенс", "котангенс"]
            )

    def on_combobox_func1(self, text1):
        self.current_text1 = text1

    def on_cliced_button(self, text1):
        with sqlite3.connect("Geometry.db") as db:
            cursor = db.cursor()
            result = cursor.execute(
                "SELECT picture FROM geometry WHERE name = ?", [self.current_text1]
            ).fetchall()
        self.get_picture(str(*result)[2:-3])

    def get_picture(self, resultat):
        self.title = "Image Viewer"
        self.setWindowTitle(self.title)

        label = QLabel(self)
        pixmap = QPixmap(str(f"pictures\{resultat}"))
        label.setPixmap(pixmap)
        self.setCentralWidget(label)
        self.resize(pixmap.width(), pixmap.height())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
