"""Представьте, что вы пишете программное обеспечение для автоматической кассы в магазине самообслуживания.
Одной из функций, заложенных в кассу, должен быть расчет сдачи в случае оплаты покупателем наличными.
Напишите программу, которая будет запрашивать у пользователя сумму сдачи в центах. После этого она должна рассчитать
и вывести на экран, сколько и каких монет потребуется для выдачи указанной суммы, при условии что должно быть
задействовано минимально возможное количест-во монет. Допустим, у нас есть в распоряжении монеты
достоинством в 1, 5, 10, 25 центов, а также в 1 (loonie) и 2 (toonie) канадских доллара."""

cents_per_toonie = 200
cents_per_loonie = 100
cents_per_quarter = 25
cents_per_dime = 10
cents_per_nickel = 5

cents = int(input('Введите сумму в центах: '))

print('', cents // cents_per_toonie, 'Двухдолларовых монет')
cents = cents % cents_per_toonie
print('', cents // cents_per_loonie, 'однодолларовых монет')
cents = cents % cents_per_loonie
print('', cents // cents_per_quarter, '25–центовых монет')
cents = cents % cents_per_quarter
print('', cents // cents_per_dime, '10–центовых монет')
cents = cents % cents_per_dime
print('', cents // cents_per_nickel, '5–центовых монет')
cents = cents % cents_per_nickel

print('', cents, 'центов')
