from setuptools import setup, find_packages

setup(
    name="homogeneous-transform",                     # Name of the library
    version="0.1.0",                       # Library version
    author="Gérémy Sauvageau",                    # Author's name
    author_email="geremysauvageau@gmail.com", # Author's email
    description="Homogeneous transformation toolbox",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/guimauve007/homogeneous-transform",  # URL of the project
    packages=find_packages(),             # Automatically find packages
    install_requires=[
        "numpy",
        "scipy",
    ],  # Dependencies
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
