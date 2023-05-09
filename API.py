import requests

# Вітаємо користувача і виводимо список категорій
print("Вітаємо! Оберіть категорію зі списку:")
print("animal")
print("career")
print("celebrity")
print("dev")
print("eplicit")
print("fashion")
print("food")
print("history")
print("money")
print("movie")
print("music")
print("political")
print("religion")
print("sport")

# Отримуємо категорію від користувача
category = input()

# Формуємо URL для API з використанням введеної категорії
api_url = f"https://api.chucknorris.io/jokes/random?category={category}"

# Відправляємо запит до API
response = requests.get(api_url)

# Перевіряємо, чи є успішна відповідь
if response.status_code == 200:
    # Парсимо JSON-відповідь
    json_data = response.json()

    # Виводимо дані в консоль
    print("\nКатегорія:", json_data["categories"][0])
    print("Дата створення:", json_data["created_at"])
    print("Анекдот:", json_data["value"])
else:
    print("Сталася помилка при отриманні даних з API")
