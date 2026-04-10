"""Задача 10. Система учёта склада."""

warehouse = {
    "Кирпич": {"quantity": 5000, "price": 12.50, "min_quantity": 1000},
    "Цемент": {"quantity": 120, "price": 450.00, "min_quantity": 50},
    "Песок": {"quantity": 8, "price": 800.00, "min_quantity": 10},
    "Арматура": {"quantity": 30, "price": 48000.00, "min_quantity": 20},
    "Бетон": {"quantity": 45, "price": 4200.00, "min_quantity": 15},
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
issue_material = "Цемент"
issue_amount = 25

print("\n=== ВЫДАЧА МАТЕРИАЛА ===")
if issue_material in warehouse and warehouse[issue_material]["quantity"] >= issue_amount:
    before = warehouse[issue_material]["quantity"]
    warehouse[issue_material]["quantity"] -= issue_amount
    after = warehouse[issue_material]["quantity"]

    print(f"✓ Выдано {issue_amount} единиц '{issue_material}'")
    print(f"Остаток: {before} -> {after}")
else:
    print("✗ Невозможно выполнить выдачу: недостаточно запаса или материал не найден.")
