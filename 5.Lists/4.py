def teacher_info():
    information_list = []
    while True:
        lastname = input('Lastname: ')
        position = input('Position: ')
        students_all_groups = input('Amount of students: ').split(',')
        new_list = [lastname, position, students_all_groups]
        information_list.append(new_list)
        print(information_list)


teacher_info()