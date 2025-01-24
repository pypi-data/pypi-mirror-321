class NumberIterator:
    def __init__(self, limit):
        self.current = 10  # Начинаем с 10
        self.limit = limit  # Указанный предел

    def __iter__(self):
        return self  # Возвращаем сам объект итератора

    def __next__(self):
        if self.current > self.limit:  # Когда достигнут предел
            raise StopIteration
        current_number = self.current
        self.current += 1  # Увеличиваем текущее число
        return current_number

# Пример использования
limit = 25
iterator = NumberIterator(limit)
for num in iterator:
    print(num)

if __name__ == "__main__":
    print(f"{__file__} executed as script.")