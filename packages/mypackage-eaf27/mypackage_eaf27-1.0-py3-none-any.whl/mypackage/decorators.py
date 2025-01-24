import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Засекаем время начала выполнения
        result = func(*args, **kwargs)  # Выполняем функцию
        end_time = time.time()  # Засекаем время окончания выполнения
        elapsed_time = end_time - start_time  # Вычисляем затраченное время
        print(f"{elapsed_time:.3f} seconds")  # Выводим время с точностью до тысячных
        return result  # Возвращаем результат выполнения функции
    return wrapper

@timeit
def slow_sum(a, b, *, delay):
    time.sleep(delay)  # Имитация долгого выполнения
    return a + b

# Пример вызова
result = slow_sum(2, 2, delay=1)
print(result)  # Выводим результат выполнения функции

if __name__ == "__main__":
    print(f"{__file__} executed as script.")