import random
import string
from collections import Counter


def input_data():
    """Ввод данных вручную."""
    global data
    data = input("Введите текст: ")


def generate_data():
    """Генерация случайного текста."""
    global data
    length = random.randint(50, 200)
    data = ''.join(random.choices(string.ascii_letters + string.punctuation + ' ', k=length))
    print(f"Сгенерированный текст: {data}")


def analyze_data(data):
    """Анализ данных и частотный анализ текста."""
    total_chars = len(data)
    if total_chars == 0:
        return {}

    frequency = Counter(data)
    frequency_analysis = {char: count / total_chars for char, count in frequency.items()}

    return frequency_analysis


def output_result(result):
    """Вывод результата анализа."""
    if not result:
        print("Нет результатов для отображения.")
        return

    print("Частотный анализ текста:")
    for char, freq in result.items():
        print(f"'{char}': {freq:.4f}")

# Основное меню остается без изменений