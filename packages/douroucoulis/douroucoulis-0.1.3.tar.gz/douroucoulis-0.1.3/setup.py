from setuptools import setup, find_packages

setup(
    name="douroucoulis",  # Replace with your package name
    version="0.1.3",  # Update with the new version
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "scikit-learn",
        "sweetviz",
        "douroucoulisay",
        "xgboost",
    ],
    author="Juan Pablo Perea-Rodriguez, Ph.D.",
    author_email="douroucoulis-fr@gmail.com",
    description="INformation-Theoretic model selection, multimodel inference, Machine Learning algorithms.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/douroucoulis-fr/douroucoulisdotpie",  # Replace with your GitHub URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
