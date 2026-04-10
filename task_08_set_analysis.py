"""Задача 8. Анализ заказов (множества)."""


def read_materials_set(contractor_number: int) -> set[str]:
    """Считывает материалы подрядчика через запятую и возвращает множество."""
    raw = input(
        f"Введите материалы подрядчика #{contractor_number} через запятую: "
    ).strip()
    return {item.strip() for item in raw.split(",") if item.strip()}


# Материалы трёх подрядчиков (ввод с консоли)
contractor_1 = read_materials_set(1)
contractor_2 = read_materials_set(2)
contractor_3 = read_materials_set(3)

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
