from setuptools import find_packages, setup

setup(
    name="marcdiff",
    version="1.0.0",
    author="Geoffrey Spear",
    author_email="speargh@pitt.edu",
    description="diff MARC21 files",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "click",
        "pymarc",
    ],
    entry_points={
        "console_scripts": [
            'marcdiff = marcdiff.cli:run'
        ]
    },
)
