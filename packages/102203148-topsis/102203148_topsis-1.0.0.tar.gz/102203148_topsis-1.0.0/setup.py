from setuptools import setup, find_packages

setup(
    name="102203148_topsis",
    version="1.0.0",
    author="Aryan Kakkar",
    author_email="aryan10767@gmail.com",
    description="A Python package for multi-criteria decision-making using the TOPSIS method.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    py_modules=["topsis"],
    install_requires=[
        "pandas",
        "numpy",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'topsis=topsis:main',
        ],
    },
)
