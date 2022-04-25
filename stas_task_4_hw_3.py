import math

earth_parameters = input('Введите количество_земных_дней и количество_часов ')
earth_parameters = earth_parameters.replace(' ', '')
e_days, e_hours = earth_parameters.split(sep=',')
e_days = int(e_days)
e_hours = int(e_hours)
e_complete_day = math.fsum([24, 3 / 60, 56.5554 / 3600])
m_complete_day = math.fsum([24, 39 / 60, 35.244 / 3600])
seconds_e_days = e_days * e_complete_day * 3600
seconds_e_hours = e_hours * 3600
total_e_seconds = seconds_e_days + seconds_e_hours
delta = e_complete_day / m_complete_day
total_m_seconds = total_e_seconds * delta
m_days = round(total_m_seconds / 3600 / m_complete_day, 2)

print('Это приблизительно', m_days, 'марсианских солов', sep=' ')
