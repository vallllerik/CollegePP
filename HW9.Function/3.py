def exam(number_of_students):
    for i in range(0, number_of_students):
        score = int(input('Enter your score: '))
        if score > 50:
            print('Допущен')
        else:
            print('Вы отчислены')


exam(int(input('Enter number of students')))