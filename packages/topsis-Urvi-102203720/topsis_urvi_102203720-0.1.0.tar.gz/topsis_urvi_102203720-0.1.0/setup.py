from setuptools import setup, find_packages

setup(
    name="topsis-Urvi-102203720",
    version="0.1.0",
    author="Urvi Garg",
    author_email="urvigarg43@gmail.com",
    description="A Python package for TOPSIS implementation",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/UrviGarg/102203720_topsis",
    packages=find_packages(where='src'),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
    ],
    python_requires=">=3.7",
    install_requires=[
        "pandas",
        "numpy"
    ],
)
