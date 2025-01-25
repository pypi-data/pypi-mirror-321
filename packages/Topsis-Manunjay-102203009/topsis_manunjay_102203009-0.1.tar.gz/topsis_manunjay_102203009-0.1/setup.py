# setup.py

from setuptools import setup, find_packages

setup(
    name='Topsis-Manunjay-102203009',  # Replace with your actual name and roll number
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
    ],
    entry_points={
        'console_scripts': [
            'topsis = topsis.topsis:topsis',  # This tells Python to map 'topsis' to topsis.py
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
