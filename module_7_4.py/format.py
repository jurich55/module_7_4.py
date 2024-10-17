
# Домашнее задание по теме "Форматирование строк".
# Использование %:
team1_num = 10
team2_num = 11
print('В команте Мастера кода участников: %s' % (team1_num))
print("Итого сегодня в командах участников: %s и %s!" % (team1_num, team2_num))

# Использование format():
score_2 = 39
team1_time = 715.7
print("Команда Волшебники данных решила задач: {0}!".format(score_2))
print(" Волшебники данных решили задачи за {} с!".format(team1_time))

# Использование f-строк:
score_1 = 39
score_2 = 35
print(f'Команды решили {score_1} и {score_2} задач.')
challenge_result = 'победа команды "Мастера кода"'
print(f'Результат битвы: {challenge_result}!')
tasks_total = 210
time_avg = 151.5
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')