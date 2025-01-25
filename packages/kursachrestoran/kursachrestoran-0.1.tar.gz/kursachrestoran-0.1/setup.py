from setuptools import setup, find_packages

setup(
    name='kursachrestoran',          # Название библиотеки
    version='0.1',                   # Версия
    packages=find_packages(),        # Автоматически находит пакеты
    install_requires=['psycopg2'],   # Зависимости
    author='Your Name',              # Ваше имя
    author_email='your.email@example.com',  # Ваш email
    description='A library for interacting with a PostgreSQL database for restaurant management',
    long_description_content_type='text/markdown',  # Тип описания
    url='https://github.com/yourusername/kursachrestoran',  # Ссылка на репозиторий
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Минимальная версия Python
)