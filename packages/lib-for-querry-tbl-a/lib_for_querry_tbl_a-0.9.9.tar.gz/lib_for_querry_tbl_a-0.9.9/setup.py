from io import open
from setuptools import setup
#from xml.sax.expatreader import version

from setuptools import setup

version = '0.9.9'

setup(
    name='lib_for_querry_tbl_a',  # Название вашей библиотеки
    version=version,  # Версия
    author='Daniil_Viktorovich',  # Ваше имя
    author_email='daniil789p@gmail.com',  # Ваш email
    packages=['lib_for_querry_tbl_a'],  # Найти все пакеты
    install_requires=[],  # Список зависимостей
    description='A simple example library',  # Краткое описание
    long_description='lib_for_querry_tbl_a',  # Длинное описание
    #long_description_content_type='text/markdown',  # Формат длинного описания
    # url='https://github.com/DanikPryanik71/lib_for_querry_tbl_name',  # URL на ваш репозиторий
    # download_url= 'https://github.com/DanikPryanik71/lib_for_querry_tbl_name/archive/v{}.zip'.format(version),

    license='MIT',  # Лицензия
    classifiers=[  # Классификаторы для вашей библиотеки
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Совместимые версии Python
)