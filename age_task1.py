

try:
    age = float(input("Введите Ваш возраст: "))

    if age < 7:
        print ("учиться в детском саду")
    elif 7 <= age <= 17:
        print ("учиться в школе")
    elif 17 < age <= 22:
        print("учиться в институте")
    elif 22< age <= 60:
        print("учиться на работе")
    elif age > 60:
        print ("учиться на пенсии")

except ValueError:
    print("Введено не число")