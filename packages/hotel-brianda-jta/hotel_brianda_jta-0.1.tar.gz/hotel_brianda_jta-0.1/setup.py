from setuptools import setup, find_packages

setup(
    name="hotel_brianda_jta",
    version="0.1",
    description="Aplicación para la gestión hotelera del hotel Brianda.",
    author="Jasmine Trillo Álvarez",
    author_email="jasslevelup@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "mysql-connector-python",
        "PySide6",
    ],
    scripts=[]
)