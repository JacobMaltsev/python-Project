from PyQt5 import QtWidgets  # Основной файл программы с прописанной логикой
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox  # Импортирование необходимых виджетов из библиотеки PyQt5

import calc  # Импортирование файла интерфейса

import sys


class Calculator(QMainWindow, calc.Ui_MainWindow):  # Объявление класса Калькулятор, который наследуется от QMainWindow, в котором прописан весь основной интерфейс программы (интерфейс создан в программе QtDesigner)
    def __init__(self):
        super().__init__()  # Инициализация класса
        self.setupUi(self)

        self.add_functions()
        self.is_equal = False

    def add_functions(self):  # Добавление функции на каждую из кнопок
        self.btn_0.clicked.connect(lambda: self.write_number(self.btn_0.text()))
        self.btn_1.clicked.connect(lambda: self.write_number(self.btn_1.text()))
        self.btn_2.clicked.connect(lambda: self.write_number(self.btn_2.text()))
        self.btn_3.clicked.connect(lambda: self.write_number(self.btn_3.text()))
        self.btn_4.clicked.connect(lambda: self.write_number(self.btn_4.text()))
        self.btn_5.clicked.connect(lambda: self.write_number(self.btn_5.text()))
        self.btn_6.clicked.connect(lambda: self.write_number(self.btn_6.text()))
        self.btn_7.clicked.connect(lambda: self.write_number(self.btn_7.text()))
        self.btn_8.clicked.connect(lambda: self.write_number(self.btn_8.text()))
        self.btn_9.clicked.connect(lambda: self.write_number(self.btn_9.text()))
        self.btn_plus.clicked.connect(lambda: self.write_number(self.btn_plus.text()))
        self.btn_sub.clicked.connect(lambda: self.write_number(self.btn_sub.text()))
        self.btn_mult.clicked.connect(lambda: self.write_number(self.btn_mult.text()))
        self.btn_div.clicked.connect(lambda: self.write_number(self.btn_div.text()))
        self.btn_equal.clicked.connect(self.result)
        self.btn_reset.clicked.connect(self.reset)

    def write_number(self, number):  # Функция записи числа в textlabel
        if self.label_result.text() == "0" or self.is_equal == True:  # Проверка ввода
             self.label_result.setText(number)
             self.is_equal = False
        else:
            self.label_result.setText(self.label_result.text() + number)

    def result(self):  # Функция вывода результата
        if not self.is_equal:
            try:
                res = eval(self.label_result.text())  # Основная функция, высчитывает записанное выражение
                self.label_result.setText("Результат: " + str(res))
                self.is_equal = True
            except Exception as ex:  # Окно об ошибке при некорректном вводе данных
                error = QMessageBox()
                error.setWindowTitle("Ошибка")
                error.setText("Неверный формат введённых данных")
                error.setIcon(QMessageBox.Warning)
                error.setStandardButtons(QMessageBox.Ok | QMessageBox.Reset)
                error.buttonClicked.connect(self.popup_action)
                error.exec_()
        else:  # Окно об ошибке при некорректном вводе данных
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Сейчас это действие выполнить нельзя")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok | QMessageBox.Reset)
            error.buttonClicked.connect(self.popup_action)
            error.exec_()

    def popup_action(self, btn):  # Функция, которая вызывается из окна с ошибкой
        if btn.text() == "Reset":
            self.label_result.setText("0")
            self.is_equal = False

    def reset(self):  # Функция, обнуляющая результат
        self.label_result.setText("0")
        self.is_equal = False

app = QtWidgets.QApplication(sys.argv)
window = Calculator()
window.show()
app.exec_()