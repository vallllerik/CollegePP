def check_lists(list1):
    if len(list1) > 1:
        list2 = sorted(list1)
        if list1 == list2:
            print("Да")
        else:
            print("Нет")
    else:
        print("Нет")


list1 = [1, 2, 3, 4, 5]
check_lists(list1)
list2 = [1, 3, 4, 5]
check_lists(list2)
list3 = [1]
check_lists(list3)

