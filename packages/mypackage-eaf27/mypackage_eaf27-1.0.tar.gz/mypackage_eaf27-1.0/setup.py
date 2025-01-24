from setuptools import setup, find_packages

setup(
    name="mypackage-eaf27",  # Уникальное имя пакета
    version="1.0",  # Версия пакета
    author="qwertyqwerty",  # Автор пакета
    author_email="eaf27@tpu.ru",  # Email автора
    description="text",
    long_description=open("README.md").read(),  # Описание пакета из README.md
    long_description_content_type="text/markdown",  # Формат описания
    packages=find_packages(),  # Поиск всех пакетов внутри проекта
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Требуемая версия Python
    entry_points={
        "console_scripts": [
            "mypackage=mypackage.__main__:main",  # Подключение главного модуля
        ],
    },
)
