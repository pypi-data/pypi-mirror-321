from setuptools import setup, find_packages

setup(
    name="linearoptimize",
    version="0.0.2",
    author="avadra mahougnon martial hilarion",
    author_email="martialhilarionavadra@gmail.com",
    url="https://github.com/Martial2023/Simplex",
    description="Un package pour résoudre les problèmes de programmations linéaires (maximisation, minimisation en utilisant la  méthode de Simplexe)",
    packages=find_packages(),
    readme="README.md",
    install_requires= ["numpy >= 1.26.4"],
    python_requires=">=3.12",
    classifiers=[
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)