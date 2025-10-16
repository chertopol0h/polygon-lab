from setuptools import setup, find_packages

setup(
    name="polygon-editor",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
    ],
    author="Your Name",
    description="Программа для редактирования полигонов с аффинными преобразованиями",
    python_requires=">=3.6",
)