def fibonacci():
    a, b = 0, 1
    while True:  # Генератор работает бесконечно
        yield a
        a, b = b, a + b

# Пример использования генератора
fib_gen = fibonacci()
for _ in range(10):  # Выведем первые 10 чисел Фибоначчи
    print(next(fib_gen))

if __name__ == "__main__":
    print(f"{__file__} executed as script.")
