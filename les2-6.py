[
(1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
(2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
(3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
]

products = []

while True:
    product = {}
    product_number = int(input('Введите номер товара: '))
    product_name = input('Введите название товара: ')
    product_price = int(input('Введите цену товара: '))
    product_quantity = int(input('Введите количество товара: '))
    product_unit = input('Введите единицу измерения товара: ')

    product['название'] = product_name
    product['цена'] = product_price
    product['количество'] = product_quantity