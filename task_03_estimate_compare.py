"""Задача 3. Конвертер температур."""

# Исходная температура в °C
celsius = 23

# Перевод в °F
fahrenheit = celsius * 9 / 5 + 32

# Определение состояния воды
if celsius <= 0:
    water_state = "Лёд"
elif celsius < 100:
    water_state = "Жидкость"
else:
    water_state = "Пар"

# Вывод
print("=== КОНВЕРТЕР ТЕМПЕРАТУР ===")
print(f"Температура: {celsius}°C")
print(f"В Фаренгейтах: {fahrenheit:.2f}°F")
print(f"Состояние воды: {water_state}")
