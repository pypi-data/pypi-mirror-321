import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text(encoding="utf-8")

setup(
    name="Topsis-Guramrit-102203234",
    version="1.0.2",
    description="Topsis Package",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Beast-Hunter/TopsisPackage",
    author="Guramrit Singh",
    author_email="guramrit.singh8@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    packages=["topsis"],
    include_package_data=True,
    install_requires=['numpy', 'pandas'],
    entry_points={
        'console_scripts': [
            'topsis = topsis.__main__:main',
        ],
    },
    python_requires=">=3.6",
)