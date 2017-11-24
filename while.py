lst_names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
name = input("Введите имя: ")

def find_person(name):
 while True:
     if lst_names.pop() = name:
        print (name + "нашелся")
        break 

find_person(name)
