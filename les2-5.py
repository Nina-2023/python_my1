my_list = [7, 5, 3, 3, 2]

while True:
    new_element = int(input('Введите новый элемент рейтинга: '))
    for index, element in enumerate(my_list):
        if new_element > element:
            my_list.insert(index, new_element)
            break
    else:
        my_list.append(new_element)
    print(my_list)