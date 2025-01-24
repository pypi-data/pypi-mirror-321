from io import open
from setuptools import setup
#from xml.sax.expatreader import version

from setuptools import setup

version = '0.9.9'

setup(
    name='lib_for_querry_table_name',  # Название вашей библиотеки
    version=version,  # Версия
    author='Daniil_Viktorovich',  # Ваше имя
    author_email='daniil789p@gmail.com',  # Ваш email
    packages=['lib_for_querry_table_name'],  # Найти все пакеты
    install_requires=['psycopg2', 'tkinter'],  # Список зависимостей
    description='A simple example library',  # Краткое описание
    long_description='lib_for_querry_table_name',  # Длинное описание
    #long_description_content_type='text/markdown',  # Формат длинного описания
    url='https://github.com/DanikPryanik71/asfasfsaf',  # URL на ваш репозиторий
    download_url= 'https://github.com/DanikPryanik71/asfasfsaf/archive/v{}.zip'.format(version),

    license='MIT',  # Лицензия
    classifiers=[  # Классификаторы для вашей библиотеки
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Совместимые версии Python
)