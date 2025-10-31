from setuptools import setup, find_packages

setup(
    name="py-cashify",
    version="0.1.0",
    description="Python library for Cashify QRIS API integration.",
    author="iamnolimit",
    packages=find_packages(),
    install_requires=[
        "requests",
        "croniter"
    ],
    python_requires='>=3.7',
    url="https://github.com/iamnolimit/py-cashify",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
