from setuptools import setup, find_packages

setup(
    name="self_healing",
    version="0.1.0",
    description="helping to fix bugs and codes",
    author="Arsam",
    author_email="ashouriarsamold@gmail.com",
    url="https://github.com/pythonAndCplusplus/self_healing",
    packages=find_packages(),
    install_requires=[
        # Add your library's dependencies here
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)