string_1 = input("введите первую строку: ")
string_2 = input("введите вторую строку: ")

def two_str(string1, string2):

    if string1 == string2:
        print(1)
    elif len(string1)>len(string2):
        print(2)
    elif string2 == "learn":
        print(3)

two_str(string_1,string_2)    