def print_stack(stack):
    print("Стек сейчас:", stack)

def run_program(file_path):
    stack = []

    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]

    i = 0
    while i < len(lines):
        line = lines[i]
        parts = line.split()
        command = parts[0].upper()

        print(f"Выполняем команду: {line}")

        if command == "PUSH":
            if len(parts) != 2:
                raise RuntimeError(f"[строка {i}] PUSH без аргумента")
            value = int(parts[1])
            stack.insert(0, value)

        elif command == "POP":
            if not stack:
                raise RuntimeError(f"[строка {i}] POP с пустого стека")
            stack.pop(0)

        elif command == "ADD":
            if len(stack) < 2:
                raise RuntimeError(f"[строка {i}] недостаточно элементов для ADD")
            a = stack.pop(0)
            b = stack.pop(0)
            stack.insert(0, a + b)

        elif command == "SUB":
            if len(stack) < 2:
                raise RuntimeError(f"[строка {i}] недостаточно элементов для SUB")
            a = stack.pop(0)
            b = stack.pop(0)
            stack.insert(0, b - a)

        elif command == "MULT":
            if len(stack) < 2:
                raise RuntimeError(f"[строка {i}] недостаточно элементов для MULT")
            a = stack.pop(0)
            b = stack.pop(0)
            stack.insert(0, a * b)

        elif command == "GET":
            if len(parts) != 2:
                raise RuntimeError(f"[строка {i}] GET без индекса")
            index = int(parts[1])
            if 0 <= index < len(stack):
                stack.insert(0, stack[index])
            else:
                raise RuntimeError(f"[строка {i}] индекс вне диапазона стека: {index}")

        elif command == "PRINT":
            if not stack:
                raise RuntimeError(f"[строка {i}] стек пустой при PRINT")
            print("Результат PRINT:", stack[0])

        elif command == "JUMP":
            if len(parts) != 2:
                raise RuntimeError(f"[строка {i}] JUMP без индекса")
            target = int(parts[1])
            if 0 <= target < len(lines):
                i = target
                continue  # перескакиваем, не увеличиваем i
            else:
                raise RuntimeError(f"[строка {i}] JUMP в недопустимую строку: {target}")

        elif command == "JUMP_REL":
            if len(parts) != 2:
                raise RuntimeError(f"[строка {i}] JUMP_REL без аргумента")
            offset = int(parts[1])
            target = i + offset
            if 0 <= target < len(lines):
                i = target
                continue
            else:
                raise RuntimeError(f"[строка {i}] JUMP_REL прыжок вне допустимого диапазона: {target}")

        elif command == "JUMP_IF_EQ":
            if len(parts) != 2:
                raise RuntimeError(f"[строка {i}] JUMP_IF_EQ без индекса")
            if len(stack) < 2:
                raise RuntimeError(f"[строка {i}] недостаточно элементов для JUMP_IF_EQ")
            target = int(parts[1])
            a = stack.pop(0)
            b = stack.pop(0)
            if a == b:
                if 0 <= target < len(lines):
                    i = target
                    continue
                else:
                    raise RuntimeError(f"[строка {i}] JUMP_IF_EQ в недопустимую строку: {target}")

        elif command == "JUMP_IF_LT":
            if len(parts) != 2:
                raise RuntimeError(f"[строка {i}] JUMP_IF_LT без индекса")
            if len(stack) < 2:
                raise RuntimeError(f"[строка {i}] недостаточно элементов для JUMP_IF_LT")
            target = int(parts[1])
            a = stack.pop(0)
            b = stack.pop(0)
            if a < b:
                if 0 <= target < len(lines):
                    i = target
                    continue
                else:
                    raise RuntimeError(f"[строка {i}] JUMP_IF_LT в недопустимую строку: {target}")

        elif command == "JUMP_IF_GT":
            if len(parts) != 2:
                raise RuntimeError(f"[строка {i}] JUMP_IF_GT без индекса")
            if len(stack) < 2:
                raise RuntimeError(f"[строка {i}] недостаточно элементов для JUMP_IF_GT")
            target = int(parts[1])
            a = stack.pop(0)
            b = stack.pop(0)
            if a > b:
                if 0 <= target < len(lines):
                    i = target
                    continue
                else:
                    raise RuntimeError(f"[строка {i}] JUMP_IF_GT в недопустимую строку: {target}")

        else:
            raise RuntimeError(f"[строка {i}] неизвестная команда: {command}")

        print_stack(stack)
        i += 1

# Точка входа
if __name__ == "__main__":
    run_program("program.txt")
