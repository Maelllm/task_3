import sys

sys.tracebacklimit = 0  # Исключаем сообщение о трассировке
try:
    age = int(input("Enter your age"))
except ValueError:
    print("Please enter number")
try:
    if age == 21:
        print("You should visit Holland.")
    elif age > 21:
        print("You should visit Vietnam.")
    else:
        print("Travell everywehere")
except NameError:
    print("")  # Исключаем излишнее описание ошибки при выполнение условий
