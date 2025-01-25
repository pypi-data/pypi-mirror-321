from setuptools import setup, find_packages

# Чтение README.md для long_description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    # Название вашей библиотеки (должно быть уникальным на PyPI)
    name='library_gpt4all',

    # Версия библиотеки (следуйте семантическому версионированию: MAJOR.MINOR.PATCH)
    version='0.1.0',

    # Автор библиотеки
    author='maga22maga44',

    # Email автора (должен быть корректным, с символом @)
    author_email='maga22maga44@gmail.com',

    # Краткое описание библиотеки
    description='Библиотека для запуска графического интерфейса с нейросетью GPT4All',

    # Длинное описание (обычно это содержимое README.md)
    long_description=long_description,

    # Тип длинного описания (Markdown)
    long_description_content_type="text/markdown",

    # Ссылка на репозиторий или домашнюю страницу проекта
    url='https://github.com/ваш_username/ваш_репозиторий',

    # Пакеты, которые нужно включить в дистрибутив
    packages=find_packages(),

    # Зависимости, которые будут установлены автоматически
    install_requires=[
        'customtkinter',
        'gpt4all',
    ],

    # Классификаторы для PyPI (указывают версию Python, лицензию, ОС и т.д.)
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",  # Статус разработки (Alpha, Beta, Stable)
        "Intended Audience :: Developers",  # Целевая аудитория
        "Topic :: Software Development :: Libraries :: Python Modules",  # Тематика
    ],

    # Минимальная версия Python, необходимая для работы библиотеки
    python_requires='>=3.6',

    # Точки входа (если хотите сделать консольную команду)
    entry_points={
        'console_scripts': [
            'run_my_library=my_library:run',  # Команда для запуска из терминала
        ],
    },

    # Дополнительные данные (например, файлы README, LICENSE и т.д.)
    include_package_data=True,

    # Ключевые слова для поиска на PyPI
    keywords='gpt4all customtkinter gui neural-network',

    # Лицензия (если не указана в classifiers)
    license='MIT',  # Укажите вашу лицензию
)