from setuptools import setup, find_packages

setup(
    name="Topsis-Dishav-102217004",  # Package name for PyPI
    version="1.0.0",
    author="Dishav",
    author_email="dsingla2_be22@thapar.edu",
    description="A Python package to implement the TOPSIS method.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/<YourUsername>/Topsis-Dishav-102217004",
    packages=find_packages(include=["Topsis_Dishav_102217004", "Topsis_Dishav_102217004.*"]),
    install_requires=["numpy", "pandas"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
