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

    # Преобразовываем входную строку в список для сортировки
    objects_list = list(objects)

    # Упорядочиваем объекты согласно заданному правилу
    sorted_objects = sorted(
        objects_list, key=lambda x: rule.index(x) if x in rule else len(rule)
    )

    # Формируем итоговый результат для вывода
    return "".join(sorted_objects)
