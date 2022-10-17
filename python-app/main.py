import calendar

print('Добро пожаловать в супер календарь\n')

year = int(input('Пожалуйства введите год: '))
month = int(input('Введеите номер любого месяца ')) 

print(calendar.month(year,month))

print('Всего хорошего!')