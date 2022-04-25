import datetime

date_time = datetime.datetime.now()
t = date_time.time()
time_format = '%H:%M'

print('Приветствую', 'пользователь,', 'сейчас', f'{t:{time_format}}', sep=' ', end='\n')
user_parameters = input('Пожалуйста введите свой ник,пол (муж или жен), и ваш возраст.'
                        'Разделите их используя пробел ')

z_parameters = user_parameters.split(sep=None, maxsplit=-1)
nickname, sex, age = z_parameters
age = int(age)

if "admin" in nickname:
    print('"Привет, повелитель!"')
if 10 < age < 14 and sex == 'муж' or age > 30 and sex == 'муж':
    print('Советую Вам посмотреть "StarWars" или \'Мандалорец\'')
elif 22 < age < 32 and sex == "жен":
    print('Советую Вам посмотреть "Трансформеры"')
elif age < 16 and sex == 'жен':
    print('Советую Вам посмотреть "Инсургент"')
elif nickname == 'Женя':
    print('Советую Вам посмотреть \'TENET\'')
elif age < 11 and sex == 'муж':
    print('Советую Вам посмотреть "TMNT"')
else:
    print('К сожалению', nickname, 'на сегодня нет подходящей рекоммендации.', sep=' ')
# Хоть в задании и нет такого требования, но пустое сообщение без рекоммендации не радует.
if nickname == 'Guido':
    print('Огромное спасибо!')
