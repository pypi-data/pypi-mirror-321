from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="Topsis-SaiVarsha-102217040",
    version="1.0.1",
    author="Varsha",
    author_email="sgummadapu_be22@thapar.edu",
    description="A Python package to implement TOPSIS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["pandas", "numpy"],
    entry_points={
        "console_scripts": [
            "topsis=Topsis.topsis:main",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
