from setuptools import setup, find_packages

setup(
    name="Topsis-Ojasvi-102203960",  # Package name
    version="0.1",  # Version
    author="Ojasvi",  # Author name
    author_email="ojasvi@example.com",  # Your email
    description="A Python package for TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)",  # Short description
    long_description=open("README.md").read(),  # Long description (from README.md)
    long_description_content_type="text/markdown",  # Content type
    packages=find_packages(),  # Automatically find package directories
    install_requires=[  # Dependencies
        "numpy",
        "pandas",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
