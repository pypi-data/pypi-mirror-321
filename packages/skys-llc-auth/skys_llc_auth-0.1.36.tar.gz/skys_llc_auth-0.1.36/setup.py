from setuptools import find_packages, setup

setup(
    name="skys_llc_auth",
    version="0.1.36",
    packages=find_packages(),
    install_requires=[
        "PyJWT",
        "cryptography",
        "fastapi",
        "alembic",
        "sqlalchemy",
        "asyncpg",
        "aiokafka",
    ],
    author="skys_llc",
    author_email="skys.llc@ya.ru",
    description="Библиотека для работы с Jwt_token",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
