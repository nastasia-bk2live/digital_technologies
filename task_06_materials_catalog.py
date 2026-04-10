"""Задача 6. Каталог материалов (списки)."""

# Исходный список из 5 материалов
materials = ["Кирпич", "Цемент", "Песок", "Арматура", "Бетон"]

print("=== КАТАЛОГ МАТЕРИАЛОВ ===")
print(f"Исходный список: {materials}")
print(f"Первый элемент: {materials[0]}")
print(f"Последний элемент: {materials[-1]}")
print(f"Средние элементы: {materials[1:-1]}")

# Добавляем 2 новых материала
materials.append("Щебень")
materials.append("Гипс")
print(f"После добавления: {materials}")

# Удаляем второй элемент (индекс 1)
removed_item = materials.pop(1)
print(f"Удалён второй элемент: {removed_item}")

# Итог
print(f"Итоговый список: {materials}")
print(f"Длина списка: {len(materials)}")
