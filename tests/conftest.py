import pytest
from random import choice as random_choice
from api.client import FileReader

@pytest.fixture
def test_data():
    """Выбор 10 случайных наборов из файла"""

    # Считывание информации из csv-файла
    filereader = FileReader("settlements.csv")
    file = filereader.read()

    # Выбор 10 случайных наборов данных и помещаем их в список res
    # При заполнении списка проводится проверка на уникальность выбранного набора
    res = []
    i = 0
    while i < 10:

        rand = random_choice(file)

        if rand not in res:
            res.append(rand)
            i += 1


    return res



