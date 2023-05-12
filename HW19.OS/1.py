import os

def system_parametrs():
    os_name = os.name
    computer_name = os.uname().nodename
    user_name = os.getlogin()
    return print("Операционная система - {0},\nИмя компьютера - {1},\nИмя пользователя - {2}".format(os_name, computer_name, user_name))

system_parametrs()
