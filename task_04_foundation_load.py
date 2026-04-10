"""Задача 4. Рабочий график."""

# Номер дня недели (1-7)
day_number = 4

# Названия дней
week_days = {
    1: "Понедельник",
    2: "Вторник",
    3: "Среда",
    4: "Четверг",
    5: "Пятница",
    6: "Суббота",
    7: "Воскресенье",
}

# Проверка и формирование режима
if day_number in week_days:
    day_name = week_days[day_number]
    is_workday = day_number <= 5
    mode = "8:00 - начало смены" if is_workday else "Отдых"

    print("=== РАБОЧИЙ ГРАФИК ===")
    print(f"День #{day_number}: {day_name}")
    print(f"Тип дня: {'Рабочий' if is_workday else 'Выходной'}")
    print(f"Режим: {mode}")
else:
    print("Ошибка: номер дня должен быть в диапазоне 1-7.")
