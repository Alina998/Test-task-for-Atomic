# Тестовое задание *АО "АтомикСофт"*
## Описание задачи
На вход дан неупорядоченный набор объектов, каждый из которых помечен одним из трёх
цветов: <span style="color:red">красный</span>, <span style="color:green">зелёный</span> и <span style="color:blue">синий</span>. Также на вход даётся правило, устанавливающее отношение
порядка между цветами. Требуется упорядочить объекты в соответствии с указанным отношением порядка цветов.
Пример:
(Обозначения: <span style="color:red">К</span>, <span style="color:green">З</span>, <span style="color:blue">С</span> – объекты, помеченные красным, зелёным и синим цветами,
соответственно.)
1. Входной набор объектов:
С С З С К З З З К К С З С С К З
2. Задано следующее отношение порядка цветов:
З < С < К
3. На выходе должен быть следующий набор объектов:
З З З З З З С С С С С С К К К К
### Необходимо реализовать описанный алгоритм в виде функции (или метода класса) и написать код, тестирующий его.