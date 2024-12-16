grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

#Создаем новый лист в который запишем среднее значение элементов из "grades"
average_score = []
#Создаем пустой словарь под связь ученик : средний бал
student_score = {}

#Циклом перебераем список "grades" вычисляя среднии значения и добавляя их в новый лист
for grade in grades:
    average_score.append(sum(grade)/len(grade))

#Изменяем тип множества на лист
students = list(students)

#Сортируем список по алфавиту
students.sort()

#Циклом проходимся по индексам списка "students" ограниченным его длинной
#Собираем словарь из значений двух списков с одинаковым индексом
for i in range(0, len(students)):
    student_score[students[i]] = average_score[i]

#Выводим значения в терминал через цикл
for student, score in student_score.items():
    print(f'Студент: {student}\nСредний балл: {score}\n')



