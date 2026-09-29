from calculator import add, subtract, multiply, divide, power, square_root


def main() -> None:
    """Точка входа: простой консольный калькулятор.

    Пример запуска:
        python main.py
    """
    print("Простой калькулятор")
    print("Операции: +, -, *, /, **, sqrt")
    print("Для выхода введите 'q'")

    while True:
        op = input("Операция: ").strip()
        if op == "q":
            break

        try:
            if op == "sqrt":
                a = float(input("Число: "))
                print("Результат:", square_root(a))
                continue

            a = float(input("Первое число: "))
            b = float(input("Второе число: "))

            if op == "+":
                print("Результат:", add(a, b))
            elif op == "-":
                print("Результат:", subtract(a, b))
            elif op == "*":
                print("Результат:", multiply(a, b))
            elif op == "/":
                print("Результат:", divide(a, b))
            elif op == "**":
                print("Результат:", power(a, b))
            else:
                print("Неизвестная операция")
        except ValueError as e:
            print("Ошибка:", e)


if __name__ == "__main__":
    main()