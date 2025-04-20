def print_stack(stack):
    print("Стек сейчас:", stack)

def run_program(file_path):
    stack = []

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            parts = line.split()
            command = parts[0].upper()

            print(f"Выполняем команду: {line}")

            if command == "PUSH":
                if len(parts) != 2:
                    print("Ошибка: PUSH без числа")
                    continue
                try:
                    value = int(parts[1])
                    stack.insert(0, value)
                except ValueError:
                    print(f"Ошибка: {parts[1]} не число")

            elif command == "POP":
                if stack:
                    stack.pop(0)
                else:
                    print("Ошибка: POP с пустого стека")

            elif command == "ADD":
                if len(stack) >= 2:
                    a = stack.pop(0)
                    b = stack.pop(0)
                    stack.insert(0, a + b)
                else:
                    print("Ошибка: мало элементов для ADD")

            elif command == "SUB":
                if len(stack) >= 2:
                    a = stack.pop(0)
                    b = stack.pop(0)
                    stack.insert(0, b - a)
                else:
                    print("Ошибка: мало элементов для SUB")

            elif command == "MULT":
                if len(stack) >= 2:
                    a = stack.pop(0)
                    b = stack.pop(0)
                    stack.insert(0, a * b)
                else:
                    print("Ошибка: мало элементов для MULT")

            elif command == "GET":
                if len(parts) != 2:
                    print("Ошибка: GET без индекса")
                    continue
                try:
                    index = int(parts[1])
                    if 0 <= index < len(stack):
                        value = stack[index]
                        stack.insert(0, value)  # Просто добавляем копию в начало
                    else:
                        print(f"Ошибка: индекс {index} вне диапазона стека")
                except ValueError:
                    print(f"Ошибка: {parts[1]} не индекс")

            elif command == "PRINT":
                if stack:
                    print("Результат PRINT:", stack[0])
                else:
                    print("Ошибка: стек пустой")

            else:
                print(f"Неизвестная команда: {command}")

            print_stack(stack)

# Точка входа
if __name__ == "__main__":
    run_program("program.txt")
