import pytest
from random import choice as random_choice
from api.client import FileReader

@pytest.fixture(params=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
def test_data(request):

    """Фикстура для выбора 50 случайных локаций из csv-файла"""

    filereader = FileReader("settlements.csv")
    file = filereader.read()
    test_l = []

    while len(test_l) < 10:
        rand = random_choice(file)
        if rand not in test_l:
            test_l.append(rand)

    return test_l[request.param]



