user_name = input("Введите имя:")
Title1 = input("Введите заголовок:")
Title2 = input("Введите подзаголовок:")
Title3 = input("Введите подзаголовок №2:")
content = input("Добавьте описание:")
status = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")

TitleList = []

TitleList.append(Title1+ " "+Title2+ " "+Title3)
TitleListRes = str(TitleList)[1:-1]#в строку и убирает скобки

GlNote = {"user_name": user_name,
          "Tltles": TitleListRes,
          "Content": content,
          }

data_view = int(input("Выберите формат даты: \n1)11-11-2011 \n2)11-jan-2024 \n3)11-11 \n4)11-jan\n"))

if data_view == 1:
    data1 = input("Введите дату начала:")
    data_off1 = input("Введите дату дедлайна:")
    print("Имя пользователя:", user_name)
    print("Заметка:", TitleListRes)
    print("Описание:", content)
    print("Дата создания:", data1)
    print("Дата завершения:", data_off1)
    GlNote["DateStart"]= data1
    GlNote["DateOff"] = data_off1
    GlNote["Status"] = status
    print(GlNote)

if data_view == 2:
    data2 = input("Введите дату начала:")
    data_off2 = input("Введите дату дедлайна:")
    print("Имя пользователя:", user_name)
    print("Заметка:", TitleListRes)
    print("Описание:", content)
    print("Дата создания:", data2)
    print("Дата завершения:", data_off2)
    GlNote["DateStart"]= data2
    GlNote["DateOff"] = data_off2
    GlNote["Status"] = status
    print(GlNote)


if data_view == 3:
    data3 = input("Введите дату начала(чч:мм:гг):")
    data_off3 = input("Введите дату дедлайна:(чч:мм:гг):")
    print("Имя пользователя:", user_name)
    print("Заметка:", TitleListRes)
    print("Описание:", content)
    print("Дата создания:", data3[0:5])
    print("Дата завершения:", data_off3[0:5])
    GlNote["DateStart"]= data3
    GlNote["DateOff"] = data_off3
    GlNote["Status"] = status
    print(GlNote)


elif data_view == 4:
    data4 = input("Введите дату начала(чч:мм:гг):")
    data_off4 = input("Введите дату дедлайна:(чч:мм:гг):")
    print("Имя пользователя:", user_name)
    print("Заметка:", TitleListRes)
    print("Описание:", content)
    print("Дата создания:", data4[0:6])
    print("Дата завершения:", data_off4[0:6])
    GlNote["DateStart"]= data4
    GlNote["DateOff"] = data_off4
    GlNote["Status"] = status
    print(GlNote)
