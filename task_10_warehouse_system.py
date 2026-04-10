"""Задача 10. Система учёта склада."""

# Создаём словарь склада с вложенными словарями (ввод с консоли)
warehouse = {}
materials_count = int(input("Введите количество материалов на складе: "))

for i in range(1, materials_count + 1):
    name = input(f"Материал #{i} (название): ").strip()
    quantity = int(input(f"Количество '{name}': "))
    price = float(input(f"Цена '{name}' (руб): "))
    min_quantity = int(input(f"Минимальный остаток '{name}': "))

    warehouse[name] = {
        "quantity": quantity,
        "price": price,
        "min_quantity": min_quantity,
    }

print("=" * 78)
print("СИСТЕМА УЧЁТА СКЛАДА")
print("=" * 78)
print("Материал | Кол-во | Цена | Мин. | Стоимость")
print("-" * 78)

total_cost = 0
most_expensive_name = ""
most_expensive_cost = 0
critical_items = []

for material, data in warehouse.items():
    quantity = data["quantity"]
    price = data["price"]
    minimum = data["min_quantity"]
    cost = quantity * price

    total_cost += cost

    if cost > most_expensive_cost:
        most_expensive_cost = cost
        most_expensive_name = material

    if quantity < minimum:
        critical_items.append((material, quantity, minimum))

    mark = " ⚠ КРИТИЧНО" if quantity < minimum else ""
    print(f"{material} | {quantity} | {price:.2f} | {minimum} | {cost:.2f}{mark}")

print("=" * 78)
print(f"ОБЩАЯ СТОИМОСТЬ: {total_cost:.2f} руб")
print(f"Самый дорогой: {most_expensive_name} ({most_expensive_cost:.2f} руб)")

print(f"⚠ КРИТИЧЕСКИЕ ОСТАТКИ ({len(critical_items)}):")
for material, quantity, minimum in critical_items:
    print(f"- {material}: {quantity} < {minimum}")

# Моделируем выдачу со склада
issue_material = input("Введите материал для выдачи: ").strip()
issue_amount = int(input("Введите количество для выдачи: "))

print("\n=== ВЫДАЧА МАТЕРИАЛА ===")
if issue_material in warehouse and warehouse[issue_material]["quantity"] >= issue_amount:
    before = warehouse[issue_material]["quantity"]
    warehouse[issue_material]["quantity"] -= issue_amount
    after = warehouse[issue_material]["quantity"]

    print(f"✓ Выдано {issue_amount} единиц '{issue_material}'")
    print(f"Остаток: {before} -> {after}")
else:
    print("✗ Невозможно выполнить выдачу: недостаточно запаса или материал не найден.")
