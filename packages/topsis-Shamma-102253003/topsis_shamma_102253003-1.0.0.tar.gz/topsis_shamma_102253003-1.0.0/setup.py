from setuptools import setup, find_packages

setup(
    name="topsis_Shamma_102253003",
    packages=find_packages(),
    version="1.0.0",
    author="Shamma",
    author_email="sshamma_be22@thapar.edu",
    description="A Python package to perform TOPSIS.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Shamma18/topsis",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "numpy",
        "pandas",
    ],
    entry_points={
        "console_scripts": [
            "topsis=topsis_Shamma_102253003.topsis:topsis",  # Replace `main` with your function handling CLI commands
        ],
    },
)
