my_list = []

n = int(input('Введите количество элементов: '))

for i in range(n):
    element = input('Введите элемент: ')
    my_list.append(element)

for i in range(0, len(my_list)-1, 2):
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]

print(my_list)