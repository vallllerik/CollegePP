from PyQt5 import QtWidgets, QtGui, QtCore
import sys

class Login(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()

        layout = QtWidgets.QVBoxLayout()

        self.welcome_label = QtWidgets.QLabel('Добро пожаловать!')
        self.login_button = QtWidgets.QPushButton('Вход')
        self.register_button = QtWidgets.QPushButton('Регистрация')

        self.login_button.clicked.connect(self.login)
        self.register_button.clicked.connect(self.register)

        layout.addWidget(self.welcome_label)
        layout.addWidget(self.login_button)
        layout.addWidget(self.register_button)

        self.setLayout(layout)

    def login(self):
        login, password, ok = self.show_login_dialog()
        if ok:
            # Код проверки логина и пароля
            self.chat_window = ChatWindow()
            self.chat_window.show()
            self.close()

    def register(self):
        login, password, ok = self.show_login_dialog()
        if ok:
            # Код добавления нового аккаунта в базу данных
            self.chat_window = ChatWindow()
            self.chat_window.show()
            self.close()

    def show_login_dialog(self):
        login, password, ok = '', '', False
        dialog = QtWidgets.QDialog()
        layout = QtWidgets.QVBoxLayout()

        login_label = QtWidgets.QLabel('Логин:')
        login_edit = QtWidgets.QLineEdit()
        password_label = QtWidgets.QLabel('Пароль:')
        password_edit = QtWidgets.QLineEdit()
        password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)

        button_box.accepted.connect(dialog.accept)
        button_box.rejected.connect(dialog.reject)

        layout.addWidget(login_label)
        layout.addWidget(login_edit)
        layout.addWidget(password_label)
        layout.addWidget(password_edit)
        layout.addWidget(button_box)

        dialog.setLayout(layout)

        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            login = login_edit.text()
            password = password_edit.text()
            ok = True

        return login, password, ok



class Register(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()

        layout = QtWidgets.QVBoxLayout()

        self.login_label = QtWidgets.QLabel('Логин:')
        self.login_edit = QtWidgets.QLineEdit() #виджет для ввода логина и пароля, а также подтверждения пароля
        self.password_label = QtWidgets.QLabel('Пароль:')
        self.password_edit = QtWidgets.QLineEdit()
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_confirmation_label = QtWidgets.QLabel('Подтверждение пароля:')
        self.password_confirmation_edit = QtWidgets.QLineEdit()
        self.password_confirmation_edit.setEchoMode(QtWidgets.QLineEdit.Password)

        self.register_button = QtWidgets.QPushButton('Зарегистрироваться')

        self.register_button.clicked.connect(self.register)

        layout.addWidget(self.login_label)
        layout.addWidget(self.login_edit)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_edit)
        layout.addWidget(self.password_confirmation_label)
        layout.addWidget(self.password_confirmation_edit)
        layout.addWidget(self.register_button)

        self.setLayout(layout)

    def register(self):
        # Код регистрации нового пользователя
        self.switch_window.emit()
        self.close()

class ChatWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QtWidgets.QVBoxLayout()

        self.message_box = QtWidgets.QTextEdit() #виджет для отображения сообщений
        self.message_box.setReadOnly(True)

        self.input_box = QtWidgets.QTextEdit() #виджет для ввода новых сообщений
        self.send_button = QtWidgets.QPushButton('Отправить')
        self.send_button.clicked.connect(self.send_message)

        self.layout.addWidget(self.message_box)
        self.layout.addWidget(self.input_box)
        self.layout.addWidget(self.send_button)

        self.setLayout(self.layout)

    def send_message(self):
        # Код отправки сообщения
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    login_window = Login()
    login_window.show()
    sys.exit(app.exec_())


#Создать функциональность для переходов между различными окнами и обработки пользовательского ввода.
#Добавим методы для перехода между окнами. Для этого создадим функцию, которая будет скрывать текущее окно и открывать экран входа
#Используем метод setCurrentWidget объекта stackedWidget, чтобы переключаться между различными экранами.

def show_login_screen(self):
    self.stackedWidget.setCurrentWidget(self.login_screen)

#Создать анологичную ф-ю для перехода к экрану регистрации

def show_registration_screen(self):
    self.stackedWidget.setCurrentWidget(self.registration_screen)

#Метод, который будет скрывать текущее окно и открывать экран чата

def show_chat_screen(self):
    self.stackedWidget.setCurrentWidget(self.chat_screen)

#Теперь, когда мы можем переключаться между различными экранами, добавим обработчики событий для кнопок входа, регистрации и отправки сообщений в чат
#Создать для обработки событий нажатия кнопки входа

def handle_login_button(self):
    username = self.login_username_input.text()
    password = self.login_password_input.text()
    # здесь должна быть логика проверки введенных данных и авторизации пользователя
    self.show_chat_screen()


#Добавим обработчик событий для кнопки регистрации

def handle_registration_button(self):
    username = self.registration_username_input.text()
    password = self.registration_password_input.text()

    #Функция обрабатывает нажатие кнопки "Зарегистрироваться" на странице регистрации. Она получает значения, введенные пользователем в поля "Логин" и "Пароль", и должна выполнить проверку их корректности, а затем зарегистрировать пользователя в системе. Пока что эта проверка и регистрация не реализованы, вместо этого функция вызывает метод show_login_screen, который переключает отображаемую страницу на страницу авторизации.
    # здесь должна быть логика проверки введенных данных и регистрации пользователя
    #вызываем метод, чтобы переключиться на экран чата
    #Метод,  чтобы переключиться на экран входа

    self.show_login_screen()

#Добавим обработчик событий для кнопки отправки сообщения
#Создать ф-ю для обработки событий нажатия кнопки отправки сообщения
#Ф-я обрабатывает нажатие кнопки "Отправить" на странице чата. Она получает текст сообщения, введенный пользователем в поле ввода сообщения, и должна отправить его на сервер и отобразить в чате. Пока что эта функция не реализована, вместо этого она просто очищает поле ввода сообщения.

def handle_send_message_button(self):
    message = self.chat_input.text()
    # здесь должна быть логика отправки сообщения на сервер и отображения его в чате
    self.chat_input.setText('')

