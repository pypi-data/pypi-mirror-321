from setuptools import setup, find_packages

setup(
    name="Topsis_Krish_102203848",  # Name of your package
    version="1.0.2",  # Updated version number
    author="Krish",  # Replace with your name
    author_email="krishkumaar2703@gmail.com",  # Replace with your email
    description="A Python package to implement TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution)",
    long_description=open(r"C:\Users\krish\OneDrive\Desktop\New folder (3)\sem6\predictive\Topsis_Krish_102203848\README.md").read(),
    long_description_content_type="text/markdown",  # Readme is in markdown format
    url="https://github.com/Krish2728/Topsis_Krish_102203848",  # GitHub URL of the project
    packages=find_packages(),  # This will automatically find and include all your package directories
    install_requires=[  # Dependencies that your package requires
        "numpy",  # Numerical operations
        "pandas",  # Data manipulation
    ],
    classifiers=[  # Classifiers help users find your package
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={  # Allows you to run the package from the command line
        "console_scripts": [
            "topsis=topsis.topsis:main",  # Command `topsis` will run the main function in topsis.py
        ],
    },
    python_requires=">=3.6",  # Specify the minimum Python version required
)
