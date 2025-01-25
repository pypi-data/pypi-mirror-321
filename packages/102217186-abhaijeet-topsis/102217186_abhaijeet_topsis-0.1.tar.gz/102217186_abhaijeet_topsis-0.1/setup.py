from setuptools import setup, find_packages

setup(
    name="102217186_abhaijeet_topsis",  # Updated name
    version="0.1",  # Package version
    description="A Python implementation of the TOPSIS method for multi-criteria decision making.",
    long_description=open('README.md').read(),  # You can write a detailed description in README.md
    long_description_content_type="text/markdown",
    author="Abhaijeet Singh",
    author_email="asingh37_be22@thapar.edu",  # Replace with your email
    url="https://github.com/yourusername/102217186_abhaijeet_topsis",  # Replace with the URL of your repository
    packages=find_packages(),
    install_requires=[
        'pandas',  # List the dependencies your package needs
        'numpy'
    ],
    entry_points={
        'console_scripts': [
            '102217186_abhaijeet_topsis=102217186_abhaijeet_topsis.102217186_abhaijeet_topsis:main',  # Updated entry point
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Or another license you prefer
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Minimum Python version
)
