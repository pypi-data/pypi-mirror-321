from setuptools import setup, find_packages

setup(
    name="Topsis-Nikhil_Garg-102203275",  # Replace with your package name
    version="1.0.1",  # Increment the version
    author="Nikhil_Garg",
    author_email="nikhilgarg288@gmail.com",
    description="A Python package for performing TOPSIS analysis.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Bluebird5757/Topsis_Nikhil_Garg_102203275",  # Replace with your GitHub URL
    packages=find_packages(),
    install_requires=["pandas", "numpy", "openpyxl"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)