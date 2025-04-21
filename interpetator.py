def print_stack(stack):
    print("Стек сейчас:", stack)

def run_program(file_path):
    stack = []

    with open(file_path, 'r') as file:
        for line_num, line in enumerate(file, start=1):
            line = line.strip()
            if not line:
                continue

            parts = line.split()
            command = parts[0].upper()

            print(f"Выполняем команду: {line}")

            if command == "PUSH":
                if len(parts) != 2:
                    raise ValueError(f"[строка {line_num}] PUSH без числа")
                value = int(parts[1])  # если не int — упадёт сам
                stack.insert(0, value)

            elif command == "POP":
                if not stack:
                    raise RuntimeError(f"[строка {line_num}] POP с пустого стека")
                stack.pop(0)

            elif command == "ADD":
                if len(stack) < 2:
                    raise RuntimeError(f"[строка {line_num}] Мало элементов для ADD")
                a = stack.pop(0)
                b = stack.pop(0)
                stack.insert(0, a + b)

            elif command == "SUB":
                if len(stack) < 2:
                    raise RuntimeError(f"[строка {line_num}] Мало элементов для SUB")
                a = stack.pop(0)
                b = stack.pop(0)
                stack.insert(0, b - a)

            elif command == "MULT":
                if len(stack) < 2:
                    raise RuntimeError(f"[строка {line_num}] Мало элементов для MULT")
                a = stack.pop(0)
                b = stack.pop(0)
                stack.insert(0, a * b)

            elif command == "GET":
                if len(parts) != 2:
                    raise ValueError(f"[строка {line_num}] GET без индекса")
                index = int(parts[1])  # если не число — упадёт сам
                if not (0 <= index < len(stack)):
                    raise IndexError(f"[строка {line_num}] Индекс {index} вне диапазона стека")
                value = stack[index]
                stack.insert(0, value)

            elif command == "PRINT":
                if not stack:
                    raise RuntimeError(f"[строка {line_num}] PRINT с пустого стека")
                print("Результат PRINT:", stack[0])

            else:
                raise ValueError(f"[строка {line_num}] Неизвестная команда: {command}")

            print_stack(stack)

# Точка входа
if __name__ == "__main__":
    run_program("program.txt")
