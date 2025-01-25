import os

# Получаем абсолютный путь к текущему файлу
current_file_path = os.path.abspath(__file__)

# Формируем полный путь к jquery.js
jquery_path = os.path.join(os.path.dirname(current_file_path), 'jquery.js')

def make_structure(name = 'Puff', DB_DATABASE='db',  DB_USER = 'root', DB_PASSWORD = 'secret', DB_HOST = 'localhost', DB_PORT=3306):
# Основная структура проекта
    return {
    f"{name}": {
        "app": {
            "__init__.py": "",
            "main.py": 
"""
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from peewee import Model, MySQLDatabase
import os
from config.settings import DATABASE


# Создаём экземпляр FastAPI
app = FastAPI()

# Монтируем статические файлы
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Инициализируем Jinja2 для работы с шаблонами
templates = Jinja2Templates(directory="app/templates")

# Настройка подключения к БД
db = MySQLDatabase(database=DATABASE['name'], user=DATABASE['user'], password=DATABASE['password'], host=DATABASE['host'],port=DATABASE['port'])
db.connect()

# Роут для главной страницы
@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
""",
            "models": {
                "__init__.py": '# Модели PeeWee',
            },
            "routes": {
                "__init__.py": "# Роутеры FastAPI",
            },
            "templates": {
                "index.html": f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name}</title>
    <!-- Подключение jQuery из папки static/js/ -->
    <script src="{{{{ url_for('static', path='js/jquery.js') }}}}"></script>
    
    
</head>
<body>
    <h1>Welcome to Puff!</h1>
    <script>
        // Пример использования jQuery
        $(document).ready(function() {{
            console.log("jQuery подключен и работает!");
        }});
    </script>
</body>
</html>""",
            },
            "static": {
                "css": {},
                "js": {'jquery.js': open(jquery_path).read()},
                "images": {},
            },
            "utils": {
                "__init__.py": "# Вспомогательные утилиты",
            },
        },
        "migrations": {
            "__init__.py": "# Миграции базы данных",
        },
        "config": {
            "__init__.py": "",
            "settings.py": f"# Настройки проекта\nDATABASE = {{\n    'name': '{DB_DATABASE}',\n    'user': '{DB_USER}',\n    'password': '{DB_PASSWORD}',\n    'host': '{DB_HOST}',\n    'port': {DB_PORT},\n}}",
        },
        "requirements.txt": "fastapi\npeewee\njinja2\nuvicorn\nmysql-connector-python",
        "manage.py": 
"""if __name__ == '__main__':
    from puff_web import pcli
    pcli.cli()
""",
    }
}

# Функция для создания структуры
def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            with open(path, "w", encoding="utf-8") as file:
                file.write(content)

