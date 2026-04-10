"""Задача 8. Анализ заказов (множества)."""

# Материалы трёх подрядчиков
contractor_1 = {"Кирпич", "Цемент", "Песок", "Арматура"}
contractor_2 = {"Цемент", "Песок", "Бетон", "Щебень"}
contractor_3 = {"Песок", "Цемент", "Гипс", "Кирпич"}

# Все уникальные
all_unique = contractor_1 | contractor_2 | contractor_3

# Общие для всех
common_all = contractor_1 & contractor_2 & contractor_3

# Только у первого
only_first = contractor_1 - contractor_2 - contractor_3

# Ровно у двух подрядчиков
exactly_two = (
    (contractor_1 & contractor_2)
    | (contractor_1 & contractor_3)
    | (contractor_2 & contractor_3)
) - common_all

# Вывод
print("=== АНАЛИЗ ЗАКАЗОВ ===")
print(f"Все уникальные материалы: {sorted(all_unique)}")
print(f"Общие для всех: {sorted(common_all)}")
print(f"Только у первого подрядчика: {sorted(only_first)}")
print(f"Есть ровно у двух подрядчиков: {sorted(exactly_two)}")
