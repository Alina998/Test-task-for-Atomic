def sort_by_color(objects: str, rule: str):
    """Функция, которая упорядочивает набор объектов в соответствии с заданным правилом"""

    # Проверка на наличие недопустимых символов во входном наборе объектов (цифры, пробелы, знаки препинания)
    if any(not color.isalpha() for color in objects):
        raise ValueError(
            "Входные данные содержат недопустимые символы. Допустимы только буквы."
        )

    # Проверка на наличие недопустимых символов в правиле (цифры, пробелы, знаки препинания)
    if any(not color.isalpha() for color in rule):
        raise ValueError(
            "Входные данные содержат недопустимые символы. Допустимы только буквы."
        )

    # Проверка входного набора объектов на допустимые цвета
    valid_colors = "КЗС"
    if not all(color in valid_colors for color in objects):
        raise ValueError(
            "Входные данные содержат недопустимые цвета. Допустимые цвета: К, З, С."
        )

    # Проверка правила на допустимые цвета
    if not all(color in valid_colors for color in rule):
        raise ValueError(
            "Правило содержит недопустимые цвета. Допустимые цвета: К, З, С."
        )

    # Проверка правила на наличие дублирующихся цветов
    if len(set(rule)) < len(rule):
        raise ValueError("Цвета в правиле не должны дублироваться.")

    # Сортируем полученный список согласно правилу
    sorted_objects = []

    # Проходим по каждому цвету в списке правил
    for color in rule:
        # Считаем количество объектов каждого цвета из правила
        colored_objects = objects.count(color)
        # Добавляем все объекты данного цвета в sorted_objects
        for i in range(colored_objects):
            sorted_objects.append(color)

    # Возвращаем результат сортировки объектов
    return "".join(sorted_objects)


# Пример вызова функции
# try:
#     objects = input("Введите набор объектов: ")
#     rule = input("Введите правило сортировки: ")
#     print(sort_by_color(objects, rule))
# except ValueError as e:
#     print(e)
