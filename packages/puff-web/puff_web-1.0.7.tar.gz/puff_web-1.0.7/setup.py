from setuptools import setup, find_packages

# Чтение README.md для описания проекта
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="puff-web",  # Имя пакета
    version="1.0.7",  # Версия пакета
    author="Nemeeza",  # Ваше имя или имя команды
    author_email="demo@qnro.ru",  # Ваш email
    description="Инструмент для быстрого развёртывания веб-приложений на стеке PeeWee + MySQL + FastAPI + Jinja2 + JQuery",  # Краткое описание
    long_description=long_description,  # Длинное описание из README.md
    long_description_content_type="text/markdown",  # Тип описания
    url="https://github.com/Nemeeza/Puff",  # Ссылка на репозиторий
    include_package_data=True,  # Включает статические файлы (например, шаблоны и статику)
    package_data={
        '': ['jquery.js'],  # Указываем путь к файлам JS
    },
    install_requires=[  # Зависимости
        "fastapi>=0.68.0",
        "peewee>=3.14.0",
        "jinja2>=3.0.0",
        "mysql-connector-python>=8.0.0",
        "uvicorn>=0.15.0",
    ],
    classifiers=[  # Классификаторы для PyPI
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",  # Минимальная версия Python
    entry_points={  # Точки входа для CLI
        "console_scripts": [
            "puff=puff_web.cli:cli",
        ],
    },
)