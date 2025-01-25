from setuptools import setup, find_packages

setup(
    name="Topsis-YatinJindal-102203418",
    version="0.1.0",
    url='https://github.com/yatinjindal21/topsis_YatinJindal_102203418',
    author="Yatin Jindal",
    author_email="jindalyatin2109@gmail.com",
    description="A Python package for TOPSIS decision-making method",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["pandas", "numpy"],
    entry_points={
        "console_scripts": [
            "topsis=topsis_package.topsis:main",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
