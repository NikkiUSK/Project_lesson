completed_homework = 12
hours_spent = 1.5
minute_spent = hours_spent * 60
course = 'Python'
homework_time_spent = hours_spent/completed_homework
homework_time_spent_min = minute_spent/completed_homework

print(f"Курс: {course}\nВсего задач: {completed_homework}")
print(f"Затрачено часов: {hours_spent}")
print(f"Среднее время выполнения: {homework_time_spent} часа ({homework_time_spent_min} минут)")