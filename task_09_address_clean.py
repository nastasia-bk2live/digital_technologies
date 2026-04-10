"""Задача 9. Очистка адресов."""

# Исходные адреса
addresses = [
    "  г. Москва, ул. Ленина, д. 10  ",
    "г.Казань,ул.Баумана,д.15",
    "  г. Санкт-Петербург, ул. Невский, д. 100 ",
]


def normalize_address(address: str) -> str:
    """Приводит адрес к стандартному формату."""
    # Удаляем лишние пробелы по краям
    cleaned = address.strip()

    # Унифицируем запятые: после запятой один пробел
    parts = [part.strip() for part in cleaned.split(",")]
    cleaned = ", ".join(parts)

    # Добавляем пробелы после сокращений, если они слеплены
    cleaned = cleaned.replace("г.", "г. ")
    cleaned = cleaned.replace("ул.", "ул. ")
    cleaned = cleaned.replace("д.", "д. ")

    # Убираем возможные двойные пробелы
    cleaned = " ".join(cleaned.split())
    return cleaned


print("=== СРАВНЕНИЕ ===")
for i, old_address in enumerate(addresses, start=1):
    new_address = normalize_address(old_address)
    print(f"#{i}")
    print(f"ДО: '{old_address}'")
    print(f"ПОСЛЕ: '{new_address}'")
