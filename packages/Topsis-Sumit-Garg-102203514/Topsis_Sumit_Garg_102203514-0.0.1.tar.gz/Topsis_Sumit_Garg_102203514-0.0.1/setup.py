from setuptools import setup, find_packages

setup(
    name="Topsis_Sumit_Garg_102203514",
    version="0.0.1",
    author="Sumit Garg",
    author_email="sumit0000garg@gmail.com",
    description="A Python package for the TOPSIS algorithm",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/topsis",  # Update with your repo URL
    packages=find_packages(),
    install_requires=["numpy"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    
    entry_points={
        "console_scripts": [
            "topsis=topsis.cli:main"
        ]
    },
)
