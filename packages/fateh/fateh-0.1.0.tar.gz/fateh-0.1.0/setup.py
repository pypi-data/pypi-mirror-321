from setuptools import setup, find_packages

setup(
    name="fateh",
    version="0.1.0",
    author="abhaijeet",
    author_email="your_email@example.com",
    description="A Python package for TOPSIS score calculation",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/fateh",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "fateh=fateh.fateh:main",  # CLI command
        ],
    },
)
