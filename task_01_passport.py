"""Задача 1. Цифровой паспорт строительного объекта."""

# Данные студента
student_name = "Бычкова Анастасия Вячеславовна"
group_number = "3150801/10102"

# Данные объекта
project_name = "ЖК 'Невский Берег'"
floors = 16
height = 54.5
is_residential = True
construction_year = 2022


# Человекочитаемый вывод
print("=== ПАСПОРТ СТРОИТЕЛЬНОГО ОБЪЕКТА ===")
print(f"Составитель: {student_name}")
print(f"Группа: {group_number}")
print()
print(f"Объект: {project_name}")
print(f"Этажность: {floors} этажей")
print(f"Высота: {height:.1f} м")
print(f"Тип: {'Жилой' if is_residential else 'Нежилой'}")
print(f"Год постройки: {construction_year}")
print()
print("Где находится объект:")
print(project_location)
print("Почему выбран именно он:")
print(project_reason)

# Дополнительный комментарий по заданию
project_location = "г. Санкт-Петербург, Невский район, Октябрьская набережная"
project_reason = "Выбран современный жилой объект в крупном городе с активной застройкой."
