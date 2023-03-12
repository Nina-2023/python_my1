#List

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
seasons = ['Зима', 'Весна', 'Лето', 'Осень']

month = int(input('Введите месяц от 1 до 12: '))

if month in months:
    season_index = (month - 1) // 3
    print(f'Этот месяц относится к {seasons[season_index]}')
else:
    print('Введите правильное число для месяца')

#Dict

months = {1:'Зима', 2:'Зима', 3:'Весна', 4:'Весна', 5:'Весна'}