def match(text, alphabet=set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')):
    return not alphabet.isdisjoint(text.lower())
name=input("Введите имя ")
age=int(input("Введите ваш возраст"))

if match(name)==True:
    print("Здравствуйте "+name)
    if age < 18:
        print("Нуно ввести данные родителя, вам меньше 18")
    else:
        print("Данные введены регистрация окончена")
        dev=int(input("Хотите заполнить профиль."+"\n"+"Нажмите 1 чтобы продолжить заполнние "+"\n"+"Нажмите 2 чтобы прекратить заполнение"+"\n"))
        match dev:
            case 1: print("Регистрация продолжается, прошу ответьте на следующик вопросы")
            case 2:  print("Регистрация завершенна"),exit()
            case _:   print("нет такого варианта действий"),exit()
        hobby=input("Введите ваши хобби через ,")
        city=input("Введите ваш город")
        print("Ваш профиль"+"\n имя: "+name+"\n возраст:",age ," \n ваши хобби: ")
        print(*hobby)
        print("\n"+"ваш город : "+ city)
else:
    print("Ошибка ведите кирилицу")
