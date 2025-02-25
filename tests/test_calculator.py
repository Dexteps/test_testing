import unittest

# Импортируем класс MadCalculator.
from calc_code.calculator import MadCalculator


class TestCalc(unittest.TestCase):
    """Тестируем MadCalculator."""
    @classmethod
    def setUpClass(cls):
        cls.calc = MadCalculator()
        print(cls.calc)

    def test_sum_string(self):
        """Тестирование функции sum_string с конкатенацией строк."""
        # Создаём экземпляр класса MadCalculator.
        # calc = MadCalculator()
        # Вызываем метод.
        # act = self.calc.sum_string(1, 100500)
        # Сравниваем фактический результат с ожидаемым.
        self.assertEqual(self.calc.sum_string(1, 100500), 1100500, 'Метод sum_string работает неправильно.')

    def test_sum_string_negative_value(self):
        """Тестирование исключения с отрицательным числом."""
        # Создаём другой экземпляр класса MadCalculator.
        # calc = MadCalculator()
        # Проверяем, что тест выдаст ошибку ValueError.
        with self.assertRaises(ValueError):
            # Вызываем метод.
            self.calc.sum_string(1, -100500)

    def test_sum_args(self):
        """Тестирование функции суммирования аргументов."""
        # Создаём ещё один экземпляр класса MadCalculator.
        # calc = MadCalculator()
        # Вызываем метод.
        # act = self.calc.sum_args(3, -3, 5)
        self.assertEqual(self.calc.sum_args(3, -3, 5), 5, 'Метод sum_args работает неправильно.')