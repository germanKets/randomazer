#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint


#обработка событий

def show_winner():
    if number.text() =='?':
        random_number = randint(1, 100)
        number.setText(str(random_number))
        text.setText('Победитель:')
        btn.setText('Выход')
    elif btn.text() == 'Выход':
        window.close()




#создание элементов интерфейса

app = QApplication([])
window = QWidget()
window.setWindowTitle('Рандомайзер')
window.resize(800, 600)
window.move(1, 10)

text = QLabel('Нажми, чтобы узнать победителя')
number = QLabel('?')

btn = QPushButton('Сгенерировать')
btn.clicked.connect(show_winner)

#привязка элементов к вертикальной линии
v_line = QVBoxLayout()
v_line.addWidget(text, alignment=Qt.AlignCenter)
v_line.addWidget(number, alignment=Qt.AlignCenter)
v_line.addStretch(1)
v_line.addWidget(btn, alignment=Qt.AlignCenter, stretch=2)
window.setLayout(v_line)

window.show()
app.exec()




#запуск приложения