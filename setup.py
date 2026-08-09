from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mx-snek-purge",
    version="1.0.0",
    author="Tu Nombre",
    author_email="tu@email.com",
    description="Multi-platform system cleaner and optimizer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tu-usuario/MX-Snek-Purge",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: System :: Systems Administration",
    ],
    python_requires=">=3.8",
    install_requires=[
        "colorama>=0.4.6",
        "psutil>=5.9.0",
        "tqdm>=4.64.0",
    ],
    entry_points={
        "console_scripts": [
            "snekpurge=snekpurge.main:main",
        ],
    },
)
