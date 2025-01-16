from datetime import datetime
user_name = input("Введите имя:")

titleList = []


title1 = input("Выберите действие:\n 1) содать заголовок 2) пропустить\n")

while title1 != "2":
    title2 = input("Введите подзаголовок или оставье строку пустой:")
    titleList.append(title2)
    title1 = input("Выберите действие: 1) содать заголовок 2) пропустить\n")

content = input("Добавьте описание:")




#titleListRes = str(titleList)[1:-1]#в строку и убирает скобки (решил убрать т.к. и без этого норм выглядит)

#Главный список:
glNote = {"user_name": user_name,
          "Tltles": titleList,
          "Content": content,
          }
#Основной цикл для ввода даты и вывода на экран введенной до этого информации:

try :
    data_view = int(input("Выберите формат даты: \n 1)11-11-2011 \n 2)11-jan-2024 \n 3)11-11\n"))
except ValueError:
    print("Правильный номер формата даты.")
    data_view = int(input("Выберите формат даты: \n 1)11-11-2011 \n 2)11-jan-2024 \n 3)11-11\n"))


if data_view == 1:
    print("Имя пользователя:", user_name)
    print("Заметка:", titleList)
    print("Описание:", content)

    current_date = datetime.now()# Получаем текущую дату

    while True:# Основной блок программы
        try:
            # Запрашиваем дату дедлайна у пользователя
            data_off1 = input("Введите дату дедлайна (в формате день-месяц-год, например 25-12-2024): ")

            deadline_date = datetime.strptime(data_off1, "%d-%m-%Y")# Преобразуем строку с датой в объект datetime
            time_difference = deadline_date - current_date # Вычисляем разницу между текущей датой и дедлайном
            days_difference = time_difference.days

            if days_difference < 0:# Проверяем статус дедлайна и выводим соответствующее сообщение
                print(f"Внимание! Дедлайн истёк {abs(days_difference):02d} дней назад.")#abs-модуль
                status = "Дедлайн истек!"
            elif days_difference == 0:
                print("Дедлайн сегодня!")
                status = "Дедлайн сегодня!"
            else:
                print(f"До дедлайна осталось {days_difference:02d} дней.")
                status = "Активно!"

            # Прерываем цикл после успешной обработки даты
            break

        except ValueError:
            # Обработка ошибки неверного формата даты
            print("Ошибка! Пожалуйста, введите дату в правильном формате (день-месяц-год).")
            print("Пример: 25-12-2024")
        except Exception as e:
            # Обработка прочих ошибок
            print(f"Произошла непредвиденная ошибка: {str(e)}")
            print("Пожалуйста, попробуйте снова.")

    correct_status = input("Выберите новый статус заметки:\n 1.выполнено\n"
                           " 2.в процессе\n 3.отложено\n 4.Оставить текущий\n")
    while correct_status == 1 or 2 or 3 or 4:
        correct_status = input("Выберите новый статус заметки:\n 1.выполнено\n"
                               " 2.в процессе\n 3.отложено\n 4.Оставить текущий\n")
        if correct_status == "1":
            corr_status = "Выполнено!"
            status = corr_status
            print(status)
        elif correct_status == "2":
            corr_status = "В процессе"
            status = corr_status
            print(status)
        elif correct_status == "3":
            corr_status = "Отложено"
            status = corr_status
            print(status)
        elif correct_status == "4":
            print(status)
        break


    print("Дата создания:", current_date)
    print("Дата завершения:", data_off1)
    print("Cтатус заметки:", status)
    glNote["DateStart"] = str(current_date)
    glNote["DateOff"] = data_off1
    glNote["Status"] = status
    print(glNote)

if data_view == 2:
    print("Имя пользователя:", user_name)
    print("Заметка:", titleList)
    print("Описание:", content)
    data2 = datetime.now()# Получаем текущую дату

    # Основной блок программы
    while True:
        try:
            # Запрашиваем дату дедлайна у пользователя
            data_off2 = input("Введите дату дедлайна (в формате день-месяц-год, например 25-jan-2024): ")

            # Преобразуем строку с датой в объект datetime
            deadline_date = datetime.strptime(data_off2, "%d-%b-%Y")
            # Вычисляем разницу между текущей датой и дедлайном
            time_difference = deadline_date - data2
            days_difference = time_difference.days
            # Проверяем статус дедлайна и выводим соответствующее сообщение
            if days_difference < 0:
                print(f"Внимание! Дедлайн истёк {abs(days_difference):02d} дней назад.")
                status = "Дедлайн истек!"

            elif days_difference == 0:
                print("Дедлайн сегодня!")
                status = "Дедлайн сегодня!"
            else:
                print(f"До дедлайна осталось {days_difference:02d} дней.")
                status = "Активно!"

            break

        except ValueError:
            # Обработка ошибки неверного формата даты
            print("Ошибка! Пожалуйста, введите дату в правильном формате (день-месяц-год).")
            print("Пример: 25-jan-2024")
        except Exception as e:
            # Обработка прочих ошибок
            print(f"Произошла непредвиденная ошибка: {str(e)}")
            print("Пожалуйста, попробуйте снова.")

    correct_status = input("Выберите новый статус заметки:\n 1.выполнено\n"
                           " 2.в процессе\n 3.отложено\n 4.Оставить текущий\n")
    while correct_status == 1 or 2 or 3 or 4:
        correct_status = input("Выберите новый статус заметки:\n 1.выполнено\n"
                               " 2.в процессе\n 3.отложено\n 4.Оставить текущий\n")
        if correct_status == "1":
            corr_status = "Выполнено!"
            status = corr_status
            print(status)
        elif correct_status == "2":
            corr_status = "В процессе"
            status = corr_status
            print(status)
        elif correct_status == "3":
            corr_status = "Отложено"
            status = corr_status
            print(status)
        elif correct_status == "4":
            print(status)
        break

    print("Дата создания:", data2)
    print("Дата завершения:", data_off2)
    print("Cтатус заметки:", status)
    glNote["DateStart"]= str(data2)
    glNote["DateOff"] = data_off2
    glNote["Status"] = status
    print(glNote)


if data_view == 3:
    print("Имя пользователя:", user_name)
    print("Заметка:", titleList)
    print("Описание:", content)

    data3 = datetime.now()  # Получаем дату
    current_year = data3.year  # Получаем год


    while True:
        try:

            date_off3_str = input("Введите дату дедлайна (в формате день-месяц, например 25-01): ")
            day_str, month_str = date_off3_str.split("-")# Разбиваем введенную строку на день и месяц
            full_date_str = f"{day_str}-{month_str}-{current_year}"# Создаем строку с полной датой, включая текущий год
            data_off3 = datetime.strptime(full_date_str, "%d-%m-%Y")

            # Вычисляем разницу между текущей датой и дедлайном
            time_difference = data_off3 - data3
            days_difference = time_difference.days

            # Проверяем статус дедлайна
            if days_difference < 0:
                print(f"Внимание! Дедлайн истёк {abs(days_difference):02d} дней назад.")
                status = "Дедлайн истек!"
            elif days_difference == 0:
                print("Дедлайн сегодня!")
                status = "Дедлайн сегодня!"
            else:
                print(f"До дедлайна осталось {days_difference:02d} дней.")
                status = "Активно!"



        except ValueError as e:
            # Обработка ошибки неверного формата даты
            print("Ошибка! Пожалуйста, введите дату в правильном формате (день-месяц).")
            print("Пример: 25-01")
            print(f"Техническая информация об ошибке: {str(e)}")  # для отладки
        except Exception as e:
            # Обработка прочих ошибок
            print(f"Произошла непредвиденная ошибка: {str(e)}")
            print("Пожалуйста, попробуйте снова.")

    correct_status = input("Выберите новый статус заметки:\n 1.выполнено\n 2.в процессе\n 3.отложено\n 4.Оставить текущий\n")
    while correct_status == 1 or 2 or 3 or 4:
        correct_status = input("Выберите новый статус заметки:\n 1.выполнено\n"
                               " 2.в процессе\n 3.отложено\n 4.Оставить текущий\n")
        if correct_status == "1":
            corr_status = "Выполнено!"
            status = corr_status
            print(status)
        elif correct_status == "2":
            corr_status = "В процессе"
            status = corr_status
            print(status)
        elif correct_status == "3":
            corr_status = "Отложено"
            status = corr_status
            print(status)
        elif correct_status == "4":
            print(status)
        break


    print("Дата создания:", full_date_str)
    print("Дата завершения:", data_off3)
    print("Cтатус заметки:", status)
    glNote["DateStart"] = full_date_str
    glNote["DateOff"] = data_off3
    glNote["Status"] = status
    print(glNote)
