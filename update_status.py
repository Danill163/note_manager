from datetime import datetime
user_name = input("Введите имя:")

titleList = []

title1 = input("Выберите действие: 1) содать заголовок 2) пропустить\n")
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
data_view = int(input("Выберите формат даты: \n1)11-11-2011 \n2)11-jan-2024 \n3)11-11\n"))

if data_view == 1:
    print("Имя пользователя:", user_name)
    print("Заметка:", titleList)
    print("Описание:", content)
    current_date = datetime.now()# Получаем текущую дату
    # Основной блок программы
    while True:
        try:
            # Запрашиваем дату дедлайна у пользователя
            data_off1 = input("Введите дату дедлайна (в формате день-месяц-год, например 25-12-2024): ")
            # Преобразуем строку с датой в объект datetime
            deadline_date = datetime.strptime(data_off1, "%d-%m-%Y")
            # Вычисляем разницу между текущей датой и дедлайном
            time_difference = deadline_date - current_date
            days_difference = time_difference.days
            # Проверяем статус дедлайна и выводим соответствующее сообщение
            if days_difference < 0:
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
    print("Дата создания:", current_date)
    print("Дата завершения:", data_off1)
    glNote["DateStart"]= current_date
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
                status2 = "Дедлайн истек!"
            elif days_difference == 0:
                print("Дедлайн сегодня!")
                status2 = "Дедлайн сегодня!"
            else:
                print(f"До дедлайна осталось {days_difference:02d} дней.")
                status2 = "Активно!"
            # Прерываем цикл после успешной обработки даты
            break

        except ValueError:
            # Обработка ошибки неверного формата даты
            print("Ошибка! Пожалуйста, введите дату в правильном формате (день-месяц-год).")
            print("Пример: 25-jan-2024")
        except Exception as e:
            # Обработка прочих ошибок
            print(f"Произошла непредвиденная ошибка: {str(e)}")
            print("Пожалуйста, попробуйте снова.")
    print("Дата создания:", data2)
    print("Дата завершения:", data_off2)
    glNote["DateStart"]= data2
    glNote["DateOff"] = data_off2
    glNote["Status"] = status2
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


            time_difference = data_off3 - data3 # Вычисляем разницу между текущей датой и дедлайном
            days_difference = time_difference.days

            # Проверяем статус дедлайна и выводим соответствующее сообщение
            if days_difference < 0:
                print(f"Внимание! Дедлайн истёк {abs(days_difference):02d} дней назад.")
                status3 = "Дедлайн истек!"
            elif days_difference == 0:
                print("Дедлайн сегодня!")
                status3 = "Дедлайн сегодня!"
            else:
                print(f"До дедлайна осталось {days_difference:02d} дней.")
                status3 = "Активно!"
            # Прерываем цикл
            break

        except ValueError as e:
            # Обработка ошибки неверного формата даты
            print("Ошибка! Пожалуйста, введите дату в правильном формате (день-месяц).")
            print("Пример: 25-01")
            print(f"Техническая информация об ошибке: {str(e)}")  # для отладки
        except Exception as e:
            # Обработка прочих ошибок
            print(f"Произошла непредвиденная ошибка: {str(e)}")
            print("Пожалуйста, попробуйте снова.")

    print("Дата создания:", full_date_str)
    print("Дата завершения:", data_off3)
    glNote["DateStart"] = full_date_str
    glNote["DateOff"] = data_off3
    glNote["Status"] = status3
    print(glNote)




