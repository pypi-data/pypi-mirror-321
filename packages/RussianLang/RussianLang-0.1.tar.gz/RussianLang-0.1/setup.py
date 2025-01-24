from setuptools import find_packages, setup

setup(
    name="RussianLang",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    test_suite="tests",
    author="Rodionov Andrew",
    author_email="dron3915work@gmail.com",
    description="Библиотека для программирования на python русским языком",
    long_description=open("README.md", encoding="utf-8").read(),  # Указываем кодировку
    long_description_content_type="text/markdown",
    url="https://github.com/Dron3916/RussianLanguage",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
