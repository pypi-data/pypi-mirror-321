from setuptools import setup, find_packages

setup(
    name="Topsis-Vedant_Saha-102203494",  # Replace with your name and roll number
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            'topsis=topsis.topsis:main',
        ],
    },
    author="Vedant_Saha",  # Replace with your name
    author_email="vedantsaha04@gmail.com",  # Replace with your email
    description="A Python package for TOPSIS implementation",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    python_requires='>=3.6',
)

