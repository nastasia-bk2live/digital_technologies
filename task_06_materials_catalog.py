"""Задача 6. Каталог материалов (списки)."""

# Создаём список из 5 материалов, введённых с консоли
materials = []
for i in range(1, 6):
    material = input(f"Введите материал #{i}: ").strip()
    materials.append(material)

print("=== КАТАЛОГ МАТЕРИАЛОВ ===")
print(f"Исходный список: {materials}")
print(f"Первый элемент: {materials[0]}")
print(f"Последний элемент: {materials[-1]}")
print(f"Средние элементы: {materials[1:-1]}")

# Добавляем 2 новых материала
new_material_1 = input("Введите новый материал #1: ").strip()
new_material_2 = input("Введите новый материал #2: ").strip()
materials.append(new_material_1)
materials.append(new_material_2)
print(f"После добавления: {materials}")

# Удаляем второй элемент (индекс 1)
removed_item = materials.pop(1)
print(f"Удалён второй элемент: {removed_item}")

# Итог
print(f"Итоговый список: {materials}")
print(f"Длина списка: {len(materials)}")
