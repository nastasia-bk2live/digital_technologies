"""Задача 7. Прайс-лист материалов (словарь)."""

# Создаём словарь из 5 материалов и цен, введённых с консоли
price_list = {}
for i in range(1, 6):
    material = input(f"Введите название материала #{i}: ").strip()
    price = float(input(f"Введите цену для '{material}' (руб): "))
    price_list[material] = price

print("=== ПРАЙС-ЛИСТ МАТЕРИАЛОВ ===")
print(f"Исходный словарь: {price_list}")

# Добавляем 2 новых материала
for i in range(1, 3):
    material = input(f"Введите новый материал #{i}: ").strip()
    price = float(input(f"Введите цену для '{material}' (руб): "))
    price_list[material] = price
print(f"После добавления: {price_list}")

# Изменяем цену одного материала (+10%)
item_to_increase = input("Введите материал для увеличения цены на 10%: ").strip()
if item_to_increase in price_list:
    old_price = price_list[item_to_increase]
    price_list[item_to_increase] = old_price * 1.10
    print(
        f"Цена '{item_to_increase}' изменена: "
        f"{old_price:.2f} -> {price_list[item_to_increase]:.2f}"
    )
else:
    print(f"Материал '{item_to_increase}' не найден, цена не изменена.")

# Удаляем один материал
removed_item = input("Введите материал для удаления: ").strip()
if removed_item in price_list:
    del price_list[removed_item]
    print(f"Удалён материал: {removed_item}")
else:
    print(f"Материал '{removed_item}' не найден, удаление пропущено.")

# Средняя цена
average_price = sum(price_list.values()) / len(price_list)
print(f"Средняя цена: {average_price:.2f} руб")
print(f"Итоговый словарь: {price_list}")
