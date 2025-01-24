from setuptools import setup, find_packages

setup(
    name="bdforuniversity",  # Название пакета
    version="0.1",  # Версия пакета
    author="Liliya_Severin",  # Ваше имя
    description="A library for managing building construction data in PostgreSQL",  # Краткое описание
    long_description=open("README.md").read(),  # Длинное описание (из README.md)
    long_description_content_type="text/markdown",  # Тип описания
    url="https://github.com/yourusername/building_management",  # Ссылка на репозиторий
    packages=find_packages(),  # Автоматически находит все пакеты
    install_requires=[
        "psycopg2>=2.9.0",  # Зависимости
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Лицензия
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Минимальная версия Python
)