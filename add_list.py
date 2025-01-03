user_name = input("Введите имя:")
Title1 = input("Введите заголовок:")
Title2 = input("Введите подзаголовок:")
Title3 = input("Введите подзаголовок №2:")
content = input("Добавьте описание:")
TitleList = []
data_vid = int(input("Выберите формат даты: \n1)11-11-2011 \n2)11-jan-2024 \n3)11-11 \n4)11-jan\n"))


TitleList.append(Title1 + " " + Title2 + " " + Title3)
TitleListRes = str(TitleList)[1:-1]

if data_vid == 1:
    data1 = input("Введите дату начала:")
    data_off1 = input("Введите дату завершения:")
    print("Имя пользователя:", user_name)
    print("Заметка:", TitleListRes)
    print("Описание:", content)
    print("Дата создания:", data1)
    print("Дата завершения:", data_off1)

if data_vid == 2:
    data2 = input("Введите дату начала:")
    data_off2 = input("Введите дату завершения:")
    print("Имя пользователя:", user_name)
    print("Заметка:", TitleListRes)
    print("Описание:", content)
    print("Дата создания:", data2)
    print("Дата завершения:", data_off2)

if data_vid == 3:
    data3 = input("Введите дату начала(чч:мм:гг):")
    data_off3 = input("Введите дату завершения(чч:мм:гг):")
    print("Имя пользователя:", user_name)
    print("Заметка:", TitleListRes)
    print("Описание:", content)
    print("Дата создания:", data3[0:5])
    print("Дата завершения:", data_off3[0:5])

elif data_vid == 4:
    data4 = input("Введите дату начала(чч:мм:гг):")
    data_off4 = input("Введите дату завершения(чч:мм:гг):")
    print("Имя пользователя:", user_name)
    print("Заметка:", TitleListRes)
    print("Описание:", content)
    print("Дата создания:", data4[0:6])
    print("Дата завершения:", data_off4[0:6])
