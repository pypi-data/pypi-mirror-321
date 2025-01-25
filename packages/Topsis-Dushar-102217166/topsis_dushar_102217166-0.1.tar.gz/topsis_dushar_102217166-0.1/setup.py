from setuptools import setup, find_packages

setup(
    name="Topsis-Dushar-102217166",
    version="0.1",
    packages=find_packages(),
    install_requires=["pandas", "numpy"],
    entry_points={
        'console_scripts': [
            'topsis = topsis.topsis:run_topsis',
        ],
    },
    author="Dushar Khatri",
    author_email="dkhatri_be22@thapar.edu",
    description="A Python package to implement the Topsis method",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/dusharkhatri/Topsis-Dushar-102217166",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)

