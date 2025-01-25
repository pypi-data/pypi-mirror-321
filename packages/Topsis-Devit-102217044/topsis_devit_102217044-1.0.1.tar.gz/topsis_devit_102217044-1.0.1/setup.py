from setuptools import setup, find_packages

with open("README.md", "r") as f:
    description = f.read()

setup(
    name="Topsis-Devit-102217044",
    version="1.0.1",
    author="Devit Sah",
    author_email="dsah_be22@thapar.edu",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/devitsah/Topsis-Devit-102217044",
    packages=find_packages(),
    install_requires=["pandas", "numpy"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
