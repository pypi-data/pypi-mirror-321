from setuptools import setup, find_packages

setup(
    name='lib_for_querrry',  # имя, под которым будет доступен ваш пакет на PyPI
    version='0.1.0',          # версия вашего пакета
    packages=find_packages(),  # найти все пакеты в директории
    description='Краткое описание вашей библиотеки',  # описание
    #long_description=open('README.md').read(),  # длинное описание, если у вас есть README.md
    long_description_content_type='text/markdown',  # тип контента для длинного описания
    #url='https://github.com/ваш_пользователь/ваш_репозиторий',  # URL до вашего репозитория (можно не указывать)
    author='Daniil_Viktorovich',  # ваше имя
    author_email='daniil789p@gmail.com',  # ваш email
    classifiers=[  # классификаторы, чтобы описать ваш пакет
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # минимальная версия Python
)
