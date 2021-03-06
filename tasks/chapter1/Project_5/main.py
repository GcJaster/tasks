"""Во многих странах в стоимость стеклотары закладывается определенный депозит,
чтобы стимулировать покупателей напитков сдавать пустые бутылки.
Допустим, бутылки объемом 1 литр и меньше стоят $0,10, а бутылки большего объема – $0,25.
Напишите программу, запрашивающую у пользователя количество бутылок каждого размера.
На экране должна отобразиться сумма, которую можно выручить, если сдать всю имеющуюся посуду.
Отформатируйте вывод так, чтобы сумма включала два знака после запятой и дополнялась слева символом доллара."""

dp_for_small = 0.10
dp_for_large = 0.25

count_small_bottle = int(input('Введите количество бутылок объёмом <=1 литра: '))
count_large_bottle = int(input('Введите количество бутылок объёмом =>1 литра: '))

total_amount = (dp_for_small * count_small_bottle) + (dp_for_large * count_large_bottle)

print('Итого вы можете получить: $%.2f' % total_amount)
