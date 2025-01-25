from setuptools import setup, find_packages

setup(
    name="EmailUpdate",
    version="0.0.0",
    author="Denali Schlesinger",
    author_email="dsch28@bu.edu",
    description="Package to Add Email Updates to Code",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/dschlesinger/EmailMe",  # Repository URL
    packages=find_packages(),  # Automatically find sub-packages
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.5",  # Type annotations
    install_requires=[
    ],
)
