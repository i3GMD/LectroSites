import os

# Получаем путь к папке sites (на 2 уровня выше текущего файла)
SITES_PATH = os.path.abspath(os.path.join(__file__, '..', '..'))

# Для диагностики (можно удалить после проверки)
print("Текущая директория:", os.getcwd())
print("Путь к sites:", SITES_PATH)

# Получаем ввод пользователя
search_text = input("Введите текст для поиска: ").strip().lower()

# Проверяем существование папки sites
if not os.path.exists(SITES_PATH):
    print(f"❌ Папка {SITES_PATH} не найдена")
else:
    # Получаем список всех элементов в папке sites
    for item in os.listdir(SITES_PATH):
        full_path = os.path.join(SITES_PATH, item)
        
        # Проверяем, что это папка И имя содержит искомый текст
        if os.path.isdir(full_path) and search_text in item.lower():
            # Исключаем саму папку searcher_site из результатов
            if item != "searcher_site":
                print(item)