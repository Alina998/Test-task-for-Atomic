# Реализация решения при помощи unittest:
from main import sort_by_color
import unittest


class TestSortByColor(unittest.TestCase):
    """Тестирование функции, сортирующей набор объектов в соответствии с заданным правилом"""

    # Проверка на корректность сортировки
    def test_basic_case(self):
        result = sort_by_color("ССЗСКЗЗЗККСЗССКЗ", "ЗСК")
        self.assertEqual(result, "ЗЗЗЗЗЗССССССКККК")

    # Проверка на корректность сортировки
    def test_alternate_colors(self):
        result = sort_by_color("КЗСЗКЗСЗКККЗ", "СКЗ")
        self.assertEqual(result, "ССКККККЗЗЗЗЗ")

    # Проверка на корректность сортировки
    def test_alternate_colors_1(self):
        result = sort_by_color("КЗСЗКЗСЗКККЗ", "СК")
        self.assertEqual(result, "ССККККК")

    # Проверка на корректность сортировки
    def test_alternate_colors_2(self):
        result = sort_by_color("КЗСЗКЗСЗКККЗ", "С")
        self.assertEqual(result, "СС")

    # Проверка на корректность сортировки
    def test_alternate_colors_3(self):
        result = sort_by_color("КЗКЗЗЗК", "СКЗ")
        self.assertEqual(result, "КККЗЗЗЗ")

    # Проверка на корректность сортировки при 1 используемом цвете
    def test_single_color(self):
        result = sort_by_color("СССС", "С")
        self.assertEqual(result, "СССС")

    # Проверка на корректность сортировки при пустом наборе объектов для сортировки
    def test_empty_string(self):
        result = sort_by_color("КЗСЗКЗСЗКККЗ", "")
        self.assertEqual(result, "")

    # Проверка на корректность сортировки при пустом правиле
    def test_empty_rule(self):
        result = sort_by_color("", "ЗСК")
        self.assertEqual(result, "")

    # Проверка на корректность сортировки при отсутствии подходящих цветов в наборе
    def test_no_matching_colors(self):
        result = sort_by_color("КККК", "ЗС")
        self.assertEqual(result, "")

    # Проверка на корректность сортировки в случае если в наборе больше цветов, чем указано в правиле
    def test_rule_with_extra_colors(self):
        result = sort_by_color("ККЗС", "ЗС")
        self.assertEqual(result, "ЗС")

    # Проверка на корректность сортировки, когда правило включает дубликаты
    def test_rule_with_duplicates(self):
        with self.assertRaises(ValueError) as context:
            sort_by_color("КЗСЗКЗСЗКККЗ", "ЗСКК")
        self.assertEqual(
            str(context.exception),
            "Цвета в правиле не должны дублироваться.",
        )

    # Проверка на корректность сортировки при наличии во входном наборе объектов недопустимых цветов
    def test_invalid_color_in_objects(self):
        with self.assertRaises(ValueError) as context:
            sort_by_color("ССЗКХ", "ЗСК")
        self.assertEqual(
            str(context.exception),
            "Входные данные содержат недопустимые цвета. Допустимые цвета: К, З, С.",
        )

    # Проверка на корректность сортировки при наличии в правиле недопустимых цветов
    def test_invalid_color_in_rule(self):
        with self.assertRaises(ValueError) as context:
            sort_by_color("ССЗК", "ЗСКХ")
        self.assertEqual(
            str(context.exception),
            "Правило содержит недопустимые цвета. Допустимые цвета: К, З, С.",
        )

    # Проверка на корректность сортировки при наличии во входном наборе объектов недопустимых символов
    def test_invalid_data_in_objects(self):
        with self.assertRaises(ValueError) as context:
            sort_by_color("ССЗК1", "ЗСК")
        self.assertEqual(
            str(context.exception),
            "Входные данные содержат недопустимые символы. Допустимы только буквы.",
        )

    # Проверка на корректность сортировки при наличии в правиле недопустимых символов
    def test_invalid_data_in_rule(self):
        with self.assertRaises(ValueError) as context:
            sort_by_color("ССЗК", "ЗСК1")
        self.assertEqual(
            str(context.exception),
            "Входные данные содержат недопустимые символы. Допустимы только буквы.",
        )


if __name__ == "__main__":
    unittest.main()
