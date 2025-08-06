# Дает имя и пароль на ввод и проверяет, совпадают ли они, прежде чем пропустить дальше
def main():
    # Дает 3 попытки на отгадывание пароля
    attempts = 3
    while attempts > 0:
        
        # Спрашивает имя и пароль для входа
        name = input("Enter your name (type nothing if you want to stay anonymous): ").strip().title()
        if name == "":
            name = "Misterious User"
    
        password = input("Enter the password: ").strip()
        if password == "":
            exit()
    
        # Пропускает дальше при вводе верного пароля
        elif secret1(password):
            print("Access allowed. Welcome,", name)
            after()
            break
    
        # Пишет кол-во оставшихся попыток
        else:
            attempts -= 1
            print(f"Access denied. Remaining attempts: {attempts}")
    
    # При истрачивании всех попыток закрывает программу
    else:
        print("Too many fails. Exiting...")


# Запускает калькулятор или некоторые маленькие строки кода в зависимости от ввода
def after():
    after = input("What can I do for you? ").strip().lower()
    
    # Запускает калькулятор
    if after == "math":
        print("Calc.exe is running. Available math symbols: +, -, *, /, **, //, %")
        
        result = calc()
        if result == int(result):
            print(int(result))
        else:
            print(round(result, 2))

    # Выходит из программы
    elif after == "exit":
        print("Exiting...")
    
    # Выходит из программы, если написать "nothing"
    elif after == "nothing":
        print("Ok")

    # Выходит из программы, если буквально ничего не написать
    elif after == "":
        print("...")
    
    else:
        print("nuh uh")

# Проверяет совпадение пароля
def secret1(a):
    return a == "123"

# Запускает калькулятор
def calc():
    import re
    
    sentence = input("Enter your math sentence (with only two numbers): ").strip()
    
    number1, symbol, number2 = sentence.split(" ")

    try:
        number1 = float(number1)
    except ValueError:
        print("Your first number is not acceptable. Try again.")
        return calc()
    
    try:
        number2 = float(number2)
    except ValueError:
        print("Your second number is not acceptable. Try again.")
        return calc()
    
    if re.search(r"^.+(\+)?|(-)?|(\*)?|(\*\*)?|(/)?|(//)?|(%)?$", symbol):
        if symbol == "+":
            return number1 + number2
        elif symbol == "-":
            return number1 - number2
        elif symbol == "*":
            return number1 * number2
        elif symbol == "**":
            return number1 ** number2
        elif symbol == "/":
            return number1 / number2
        elif symbol == "//":
            return number1 // number2
        elif symbol == "%":
            return number1 % number2   
        else:
            print("Your math symbol is not acceptable. Try again.")
            return calc()


if __name__ == "__main__":
    main()
    # after()