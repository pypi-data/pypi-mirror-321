from setuptools import setup, find_packages

setup(
    name="Topsis-ShrihanTayal-102203460",  # Replace with your package name
    version="1.0.1",  # Increment the version
    author="Shrihan Tayal",
    author_email="shrihantayal@gmail.com",
    description="A Python package for performing TOPSIS analysis.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ShrihanTayal/topsis-package",  # Replace with your GitHub URL
    packages=find_packages(),
    install_requires=["pandas", "numpy", "openpyxl"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
