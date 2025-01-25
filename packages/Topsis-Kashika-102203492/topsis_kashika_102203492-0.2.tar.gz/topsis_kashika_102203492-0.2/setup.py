from setuptools import setup, find_packages  # Ensure you have this import statement

setup(
    name="Topsis-Kashika-102203492",
    version="0.2",  # Make sure the version is updated
    description="A Python package that implements the TOPSIS method for multi-criteria decision-making (MCDM).",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',  # Ensure markdown is specified
    packages=find_packages(),
    install_requires=[
        'pandas',  # If your package uses pandas
        'numpy',   # If your package uses numpy
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
