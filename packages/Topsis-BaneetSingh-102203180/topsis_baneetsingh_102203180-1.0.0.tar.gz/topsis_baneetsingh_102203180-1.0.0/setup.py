from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="Topsis-BaneetSingh-102203180",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.6",
    install_requires=[
        'numpy',
        'pandas'
    ],
    author="Baneet Singh",
    author_email="2baneetsingh@gmail.com",
    description="A TOPSIS implementation for multiple-criteria decision analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Baneet2s/topsis",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'topsis-baneet-102203180=topsis_baneet_102203180.topsis:main',
        ],
    },
)
