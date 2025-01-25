from setuptools import setup, find_packages

setup(
    name="Topsis-Devit-102217044",
    version="1.0.0",
    author="Devit Sah",
    author_email="dsah_be22@thapar.edu",
    description="A Python package for implementing the Topsis method",
    long_description=open("README.md").read(),
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
