import unittest

from task1 import prime_numbers
from task2 import text_stat
from task3 import roman_numerals_to_int


class TestTask1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.false_arguments = (
            [5, 1],
            [0, 0]
        )

    def test_prime_number_true_argumets(self):
        '''Ф-ция работает правильно с корректными аргументами'''
        s = prime_numbers(1, 5)
        self.assertEqual(s, [1, 2, 3, 4])

    def test_prime(self):
        '''Ф-ция возвращает пустой список с некорректными аргументами'''
        for low, high in self.false_arguments:
            with self.subTest():
                s = prime_numbers(low, high)
                self.assertEqual(s, [])

    # def test_prime_number_false_argruments(self):
    #     s = prime_numbers(5,1)
    #     self.assertEqual(s, [])
    # Демонстрирую альтернативный тест.


class TestTask3(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.true_arguments = {
            'XVI': 16,
            'X': 10,
            'CXV': 115,
            'IV': 4,
            'XM': 990,
            'MMD': 2500
        }

        cls.false_arguments = [
            'W',
            'xd',
            'YZ'
        ]

    def test_roman_numerals_to_int_true(self):
        '''Ф-ция работает правильно с корректными аргументами'''
        for rom_number, arabic_number in self.true_arguments.items():
            with self.subTest():
                s = roman_numerals_to_int(rom_number)
                self.assertEqual(s, arabic_number)

    def test_roman_numerals_to_int_false(self):
        '''Ф-ция возвращает None с некорректными аргументами'''
        for rom_number in self.false_arguments:
            with self.subTest():
                s = roman_numerals_to_int(rom_number)
                self.assertIsNone(s, None)


class TestTask2(unittest.TestCase):
    def test_text_stat_not_found(self):
        '''Функция text_stat возвращает ошибку, если файл не найден'''
        s = text_stat('random.txt')
        self.assertEqual(s, {'error': 'File not found'})

    def test_text_stat(self):
        '''Функция text_stat возвращает статистику'''
        result = {
            'letters_stat': {'a': (1, 0.008771929824561403),
                             'c': (2, 0.017543859649122806),
                             'g': (1, 0.008771929824561403),
                             'h': (1, 0.008771929824561403),
                             'n': (1, 0.008771929824561403),
                             'o': (2, 0.017543859649122806),
                             'p': (2, 0.017543859649122806),
                             'r': (2, 0.008771929824561403),
                             't': (1, 0.008771929824561403),
                             'y': (1, 0.008771929824561403),
                             'а': (67, 0.47368421052631576),
                             'б': (15, 0.13157894736842105),
                             'в': (25, 0.20175438596491227),
                             'г': (7, 0.06140350877192982),
                             'д': (12, 0.10526315789473684),
                             'е': (61, 0.39473684210526316),
                             'ё': (4, 0.03508771929824561),
                             'ж': (2, 0.017543859649122806),
                             'з': (17, 0.14912280701754385),
                             'и': (66, 0.40350877192982454),
                             'й': (7, 0.06140350877192982),
                             'к': (37, 0.2982456140350877),
                             'л': (21, 0.18421052631578946),
                             'м': (34, 0.24561403508771928),
                             'н': (60, 0.35964912280701755),
                             'о': (69, 0.42105263157894735),
                             'п': (25, 0.21929824561403508),
                             'р': (30, 0.20175438596491227),
                             'с': (44, 0.3333333333333333),
                             'т': (49, 0.3684210526315789),
                             'у': (8, 0.07017543859649122),
                             'х': (6, 0.05263157894736842),
                             'ц': (2, 0.017543859649122806),
                             'ч': (15, 0.13157894736842105),
                             'ш': (1, 0.008771929824561403),
                             'щ': (2, 0.017543859649122806),
                             'ъ': (2, 0.017543859649122806),
                             'ы': (23, 0.19298245614035087),
                             'ь': (9, 0.07894736842105263),
                             'ю': (6, 0.05263157894736842),
                             'я': (29, 0.18421052631578946)},
            'word_amount': 114,
            'paragraph_amount': 3,
            'bilingual_word_amount': 1
        }
        s = text_stat('info.txt')
        self.assertEqual(s, result)
