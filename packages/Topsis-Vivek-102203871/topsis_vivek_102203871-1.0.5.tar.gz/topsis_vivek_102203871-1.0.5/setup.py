from setuptools import setup, find_packages

setup(
    name="Topsis-Vivek-102203871",
    version="1.0.5",
    author="Vivek",
    author_email="atrivivek001@gmail.com",
    description="A Python package for implementing the Topsis method",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/VivekAttri01/Topsis-Vivek-102203871",
    packages=find_packages(),  # Automatically finds the package directory
    include_package_data=True,
    install_requires=[
        "numpy",
        "pandas",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
