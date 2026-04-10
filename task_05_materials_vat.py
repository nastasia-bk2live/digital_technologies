"""Задача 5. Калькулятор скидки."""

# Исходные данные
price = 780
quantity = 9

# Расчёт суммы до скидки
subtotal = price * quantity

# Определение скидки
if subtotal < 1000:
    discount_percent = 0
elif subtotal <= 5000:
    discount_percent = 5
else:
    discount_percent = 10

# Итоговые вычисления
discount_amount = subtotal * discount_percent / 100
total = subtotal - discount_amount

# Вывод
print("=== КАЛЬКУЛЯТОР СКИДКИ ===")
print(f"Цена за единицу: {price:.2f} руб")
print(f"Количество: {quantity}")
print(f"Сумма без скидки: {subtotal:.2f} руб")
print(f"Скидка: {discount_percent}% ({discount_amount:.2f} руб)")
print(f"Итого к оплате: {total:.2f} руб")
