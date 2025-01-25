from setuptools import setup, find_packages
setup(
    name="102203092_topsis",
    version="1.1.1",
    description="MCDM solved using TOPSIS",
    author="Uday Sharma",
    author_email="udaysharma1501@gmail.com",
    packages=["102203092_topsis"],
    install_requires=[
        "numpy",
        "pandas"
    ],
    entry_points={
        "console_scripts": [
            "topsis=102203092_topsis.topsis:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)