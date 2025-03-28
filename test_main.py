from main import sort_by_color


def test_sort_by_color():
    """Функция, которая запускает тесты для функции sort_by_color"""

    def assert_equal(actual, expected, test_name):
        if actual == expected:
            print(f"{test_name}: Passed")
        else:
            print(f"{test_name}: Failed (Expected {expected}, got {actual})")

    # Тесты
    try:
        # Проверка на корректность сортировки
        assert_equal(
            sort_by_color("ССЗСКЗЗЗККСЗССКЗ", "ЗСК"),
            "ЗЗЗЗЗЗССССССКККК",
            "Test Basic Case",
        )

        # Проверка на корректность сортировки
        assert_equal(
            sort_by_color("КЗСЗКЗСЗКККЗ", "СКЗ"),
            "ССКККККЗЗЗЗЗ",
            "Test Alternate Colors",
        )

        # Проверка на корректность сортировки
        assert_equal(
            sort_by_color("КЗСЗКЗСЗКККЗ", "СК"),
            "ССКККККЗЗЗЗЗ",
            "Test Alternate Colors 1",
        )

        # Проверка на корректность сортировки
        assert_equal(
            sort_by_color("КЗСЗКЗСЗКККЗ", "С"),
            "ССКЗЗКЗЗКККЗ",
            "Test Alternate Colors 2",
        )

        # Проверка на корректность сортировки
        assert_equal(
            sort_by_color("КЗКЗЗЗК", "СКЗ"), "КККЗЗЗЗ", "Test Alternate Colors 3"
        )

        # Проверка на корректность сортировки при 1 используемом цвете
        assert_equal(sort_by_color("СССС", "С"), "СССС", "Test Single Color")

        # Проверка на корректность сортировки при пустом правиле
        assert_equal(
            sort_by_color("КЗСЗКЗСЗКККЗ", ""), "КЗСЗКЗСЗКККЗ", "Test Empty Rule"
        )

        # Проверка на корректность сортировки при пустом наборе объектов
        assert_equal(sort_by_color("", "ЗСК"), "", "Test Empty String")

        # Проверка на корректность сортировки при отсутствии подходящих цветов в наборе
        assert_equal(sort_by_color("КККК", "ЗС"), "КККК", "Test No Matching Colors")

        # Проверка на корректность сортировки в случае если в наборе больше цветов, чем указано в правиле
        assert_equal(sort_by_color("ККЗС", "ЗС"), "ЗСКК", "Test Rule With Extra Colors")

        # Проверка на корректность сортировки, когда правило включает дубликаты
        assert_equal(sort_by_color("КЗС", "ККЗС"), "КЗС", "Test Rule With Duplicates")

        # Проверка на корректность сортировки, когда правило включает дубликаты
        assert_equal(sort_by_color("КЗС", "КЗКС"), "КЗС", "Test Rule With Duplicates 1")

        # Проверка на недопустимые цвета
        try:
            sort_by_color("ССЗКХ", "ЗСК")
            print("Test Invalid Color In Objects: Failed (Expected ValueError)")
        except ValueError as e:
            assert_equal(
                str(e),
                "Входные данные содержат недопустимые цвета. Допустимые цвета: К, З, С.",
                "Test Invalid Color In Objects",
            )

        # Проверка на недопустимые символы, пробелы
        try:
            sort_by_color("КЗ С", "ЗСК")
            print("Test Spaces In Objects: Failed (Expected ValueError)")
        except ValueError as e:
            assert_equal(
                str(e),
                "Входные данные содержат недопустимые символы. Допустимы только буквы.",
                "Test Spaces In Objects",
            )

        try:
            sort_by_color("КЗС!", "ЗСК")
            print("Test Punctuation In Objects: Failed (Expected ValueError)")
        except ValueError as e:
            assert_equal(
                str(e),
                "Входные данные содержат недопустимые символы. Допустимы только буквы.",
                "Test Punctuation In Objects",
            )

    except Exception as e:
        print(f"An error occurred during testing: {e}")


# Запускаем тесты
if __name__ == "__main__":
    test_sort_by_color()


# Реализация решения при помощи unittest:
# import unittest
#
#
# class TestSortByColor(unittest.TestCase):
#
#     # Проверка на корректность сортировки
#     def test_basic_case(self):
#         result = sort_by_color("ССЗСКЗЗЗККСЗССКЗ", "ЗСК")
#         self.assertEqual(result, "ЗЗЗЗЗЗССССССКККК")
#
#     # Проверка на корректность сортировки
#     def test_alternate_colors(self):
#         result = sort_by_color("КЗСЗКЗСЗКККЗ", "СКЗ")
#         self.assertEqual(result, "ССКККККЗЗЗЗЗ")
#
#     # Проверка на корректность сортировки
#     def test_alternate_colors_1(self):
#         result = sort_by_color("КЗСЗКЗСЗКККЗ", "СК")
#         self.assertEqual(result, "ССКККККЗЗЗЗЗ")
#
#     # Проверка на корректность сортировки
#     def test_alternate_colors_2(self):
#         result = sort_by_color("КЗСЗКЗСЗКККЗ", "С")
#         self.assertEqual(result, "ССКЗЗКЗЗКККЗ")
#
#     # Проверка на корректность сортировки
#     def test_alternate_colors_3(self):
#         result = sort_by_color("КЗКЗЗЗК", "СКЗ")
#         self.assertEqual(result, "КККЗЗЗЗ")
#
#     # Проверка на корректность сортировки при 1 используемом цвете
#     def test_single_color(self):
#         result = sort_by_color("СССС", "С")
#         self.assertEqual(result, "СССС")
#
#     # Проверка на корректность сортировки при пустом наборе объектов для сортировки
#     def test_empty_string(self):
#         result = sort_by_color("КЗСЗКЗСЗКККЗ", "")
#         self.assertEqual(result, "КЗСЗКЗСЗКККЗ")
#
#     # Проверка на корректность сортировки при пустом правиле
#     def test_empty_rule(self):
#         result = sort_by_color("", "ЗСК")
#         self.assertEqual(result, "")
#
#     # Проверка на корректность сортировки при отсутствии подходящих цветов в наборе
#     def test_no_matching_colors(self):
#         result = sort_by_color("КККК", "ЗС")
#         self.assertEqual(result, "КККК")
#
#     # Проверка на корректность сортировки в случае если в наборе больше цветов, чем указано в правиле
#     def test_rule_with_extra_colors(self):
#         result = sort_by_color("ККЗС", "ЗС")
#         self.assertEqual(result, "ЗСКК")
#
#     # Проверка на корректность сортировки, когда правило включает дубликаты
#     def test_rule_with_duplicates(self):
#         result = sort_by_color("КЗС", "ККЗС")
#         self.assertEqual(result, "КЗС")
#
#     # Проверка на корректность сортировки, когда правило включает дубликаты
#     def test_rule_with_duplicates_1(self):
#         result = sort_by_color("КЗС", "КЗКС")
#         self.assertEqual(result, "КЗС")
#
#     # Проверка на корректность сортировки при наличии во входном наборе объектов недопустимых цветов
#     def test_invalid_color_in_objects(self):
#         with self.assertRaises(ValueError) as context:
#             sort_by_color("ССЗКХ", "ЗСК")
#         self.assertEqual(
#             str(context.exception),
#             "Входные данные содержат недопустимые цвета. Допустимые цвета: К, З, С.",
#         )
#
#     # Проверка на корректность сортировки при наличии в правиле недопустимых цветов
#     def test_invalid_color_in_rule(self):
#         with self.assertRaises(ValueError) as context:
#             sort_by_color("ССЗК", "ЗСКХ")
#         self.assertEqual(
#             str(context.exception),
#             "Правило содержит недопустимые цвета. Допустимые цвета: К, З, С.",
#         )
#
#     # Проверка на корректность сортировки при наличии во входном наборе объектов недопустимых символов
#     def test_invalid_data_in_objects(self):
#         with self.assertRaises(ValueError) as context:
#             sort_by_color("ССЗК1", "ЗСК")
#         self.assertEqual(
#             str(context.exception),
#             "Входные данные содержат недопустимые символы. Допустимы только буквы.",
#         )
#
#     # Проверка на корректность сортировки при наличии в правиле недопустимых символов
#     def test_invalid_data_in_rule(self):
#         with self.assertRaises(ValueError) as context:
#             sort_by_color("ССЗК", "ЗСК1")
#         self.assertEqual(
#             str(context.exception),
#             "Входные данные содержат недопустимые символы. Допустимы только буквы.",
#         )
#
#
# if __name__ == "__main__":
#     unittest.main()
