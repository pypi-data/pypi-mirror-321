from setuptools import setup, find_packages

setup(
    name="Topsis-Kashika-102203492",  # Replace with your actual name and roll number
    version="0.1",  # Start with version 0.1
    packages=find_packages(),  # Automatically find all packages in the directory
    install_requires=[
        'pandas',  # Dependencies required by your package
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            'topsis = topsis.topsis:main',  # Define the command line script
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify the Python version you want to support
)

