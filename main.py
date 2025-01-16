


def match(text, alphabet=set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')):
    return not alphabet.isdisjoint(text.lower())

name=input("Введите имя ")
if match(name)==True:
    print("Здравствуйте "+name)
else:
    print("Hello " + name)
