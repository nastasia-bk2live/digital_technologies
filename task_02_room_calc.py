"""Задача 2. Параметры помещения."""

# Ввод размеров помещения (метры)
length = float(input("Введите длину помещения (м): "))
width = float(input("Введите ширину помещения (м): "))
height = float(input("Введите высоту помещения (м): "))

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
