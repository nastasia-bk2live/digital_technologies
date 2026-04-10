"""Задача 2. Параметры помещения."""

# Размеры помещения (метры)
length = 6.8
width = 4.2
height = 2.9

# Константа стоимости покраски (руб/м²)
paint_price_per_m2 = 125

# Вычисления
floor_area = length * width
wall_area = 2 * (length + width) * height
volume = length * width * height
paint_cost = wall_area * paint_price_per_m2

# Лаконичный вывод
print("=== ПАРАМЕТРЫ ПОМЕЩЕНИЯ ===")
print(f"Размеры: {length} x {width} x {height} м")
print(f"Площадь пола: {floor_area:.2f} м²")
print(f"Площадь стен: {wall_area:.2f} м²")
print(f"Объём: {volume:.2f} м³")
print(f"Стоимость покраски стен: {paint_cost:.2f} руб")
