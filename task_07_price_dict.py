"""Задача 7. Прайс-лист материалов (словарь)."""

# Исходный словарь из 5 материалов
price_list = {
    "Кирпич": 12.50,
    "Цемент": 450.00,
    "Песок": 800.00,
    "Арматура": 48000.00,
    "Бетон": 4200.00,
}

print("=== ПРАЙС-ЛИСТ МАТЕРИАЛОВ ===")
print(f"Исходный словарь: {price_list}")

# Добавляем 2 новых материала
price_list["Щебень"] = 1350.00
price_list["Гипс"] = 320.00
print(f"После добавления: {price_list}")

# Изменяем цену одного материала (+10%)
item_to_increase = "Цемент"
old_price = price_list[item_to_increase]
price_list[item_to_increase] = old_price * 1.10
print(
    f"Цена '{item_to_increase}' изменена: "
    f"{old_price:.2f} -> {price_list[item_to_increase]:.2f}"
)

# Удаляем один материал
removed_item = "Гипс"
del price_list[removed_item]
print(f"Удалён материал: {removed_item}")

# Средняя цена
average_price = sum(price_list.values()) / len(price_list)
print(f"Средняя цена: {average_price:.2f} руб")
print(f"Итоговый словарь: {price_list}")
