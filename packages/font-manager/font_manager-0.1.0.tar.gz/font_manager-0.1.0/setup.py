from setuptools import setup, find_packages

setup(
    name="font_manager",
    version="0.1.0",
    description="Library for managing fonts in PyQt5 applications",
    author="Андрей",
    author_email="andrey960123@gmail.com",
    packages=find_packages(),
    include_package_data=True,  # Включение дополнительных данных
    install_requires=[
        "PyQt5>=5.15.0"
    ],
    package_data={
        "font_manager": ["TT Interphases Pro Trial Condensed DemiBold.ttf"]  # Указываем файл шрифта
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
