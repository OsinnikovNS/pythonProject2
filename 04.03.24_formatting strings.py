# formatting strings.
team1_num, team2_num = 5, 6
score_1, score_2 = 40, 42
team1_time, team2_time = 1552.512, 2153.31451
task_total = score_1 + score_2
time_avg = (team1_time + team2_time)/task_total
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'
challenge_result = result
# ------------------------------------------------------------------
# Использование %:
print('')
print('************ Использование %: *************')
print('В команде Мастера кода участников:   %d!' % team1_num)
print('Итого сегодня в командах участников: %d и %d!' % (team1_num, team2_num))

# Использование format():
print('')
print('************ Использование format(): *************')
print('Команда Мастера кода решила задач: {0:15d}'.format(score_1))
print('Команда Волшебники данных решила задач: {0:10d}'.format(score_2))
print('Мастера кода решили задачи за -      {0} с!'.format(team1_time))
print('Волшебники данных решили задачи за - {0} с!'.format(team2_time))
print('Результат:', challenge_result)

# ------------------------------------------------------------------
# Использование f-строк:
print(f'')
print(f'{'Использование f-строк:':*^50}')
print(f'Команда Мастера кода решила задач:.{score_1:15d}')
print(f'Команда Волшебники данных решила задач: {score_2:10d}')
print(f'Мастера кода решили задачи за -      {team1_time} с!')
print(f'Волшебники данных решили задачи за - {team2_time} с!')
print(f'Результат: {challenge_result}')
