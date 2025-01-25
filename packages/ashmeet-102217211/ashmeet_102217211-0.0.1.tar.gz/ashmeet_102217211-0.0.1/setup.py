from setuptools import setup, find_packages

setup(
    name="ashmeet_102217211",
    version="0.0.1",
    description="TOPSIS Python Package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Ashmeet Kaur",
    author_email="akaur9_be22@thapar.edu",
    url="https://github.com/ashmkaur/102217211_Ashmeet_topsis.git",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
    ],
    entry_points={
        "console_scripts": [
            "topsis=topsis.topsis:main",  # Ensure the `main()` function exists in topsis.py
        ],
    },
    python_requires=">=3.6",
)
