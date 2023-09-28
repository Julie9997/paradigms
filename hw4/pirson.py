from random import randint
from typing import List
from math import sqrt


def pearson_correlation(numbers_1: List[float], numbers_2: List[float]):

    # Проверка на соответствие длины массивов
    if len(numbers_1) != len(numbers_2):
        raise ValueError("Массивы должны быть одинаковой длины")

    n = len(numbers_1)

    # Средние значения для каждого массива
    mean_1 = sum(numbers_1) / n
    mean_2 = sum(numbers_2) / n

    # Вычисление ковариации и дисперсии для массивов
    covariance = sum((numbers_1[i] - mean_1) * (numbers_2[i] - mean_2) for i in range(n))
    variance_numbers_1 = sum((x - mean_1) ** 2 for x in numbers_1)
    variance_numbers_2 = sum((y - mean_2) ** 2 for y in numbers_2)

    # Корреляция Пирсона
    correlation = covariance / (sqrt(variance_numbers_1) * sqrt(variance_numbers_2))

    return round(correlation)


num_1 = [randint(0, 100) for i in range(5)]
num_2 = [randint(0, 100) for i in range(5)]

print(num_1)
print(num_2)
correlation = pearson_correlation(num_1, num_2)
print(f"Корреляция Пирсона: {correlation}")