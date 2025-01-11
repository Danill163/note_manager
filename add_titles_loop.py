user_name = input("Введите имя:")

titleList = []

title1 = input("Выберите действие: 1) содать заголовок 2) пропустить\n")
while title1 != "2":
    title2 = input("Введите подзаголовок или оставье строку пустой:")
    titleList.append(title2)
    title1 = input("Выберите действие: 1) содать заголовок 2) пропустить\n")

content = input("Добавьте описание:")
status = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")


#titleListRes = str(titleList)[1:-1]#в строку и убирает скобки (решил убрать т.к. и без этого норм выглядит)

#Главный список:
glNote = {"user_name": user_name,
          "Tltles": titleList,
          "Content": content,
          }
#Основной цикл для ввода даты и вывода на экран введенной до этого информации:
data_view = int(input("Выберите формат даты: \n1)11-11-2011 \n2)11-jan-2024 \n3)11-11 \n4)11-jan\n"))

if data_view == 1:
    data1 = input("Введите дату начала:")
    data_off1 = input("Введите дату дедлайна:")
    print("Имя пользователя:", user_name)
    print("Заметка:", titleList)
    print("Описание:", content)
    print("Дата создания:", data1)
    print("Дата завершения:", data_off1)
    glNote["DateStart"]= data1
    glNote["DateOff"] = data_off1
    glNote["Status"] = status
    print(glNote)

if data_view == 2:
    data2 = input("Введите дату начала:")
    data_off2 = input("Введите дату дедлайна:")
    print("Имя пользователя:", user_name)
    print("Заметка:", titleList)
    print("Описание:", content)
    print("Дата создания:", data2)
    print("Дата завершения:", data_off2)
    glNote["DateStart"]= data2
    glNote["DateOff"] = data_off2
    glNote["Status"] = status
    print(glNote)


if data_view == 3:
    data3 = input("Введите дату начала(чч:мм:гг):")
    data_off3 = input("Введите дату дедлайна:(чч:мм:гг):")
    print("Имя пользователя:", user_name)
    print("Заметка:", titleList)
    print("Описание:", content)
    print("Дата создания:", data3[0:5])
    print("Дата завершения:", data_off3[0:5])
    glNote["DateStart"]= data3
    glNote["DateOff"] = data_off3
    glNote["Status"] = status
    print(glNote)


elif data_view == 4:
    data4 = input("Введите дату начала(чч:мм:гг):")
    data_off4 = input("Введите дату дедлайна:(чч:мм:гг):")
    print("Имя пользователя:", user_name)
    print("Заметка:", titleList)
    print("Описание:", content)
    print("Дата создания:", data4[0:6])
    print("Дата завершения:", data_off4[0:6])
    glNote["DateStart"]= data4
    glNote["DateOff"] = data_off4
    glNote["Status"] = status
    print(glNote)
