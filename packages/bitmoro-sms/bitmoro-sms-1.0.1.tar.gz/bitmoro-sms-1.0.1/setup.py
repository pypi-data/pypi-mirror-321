from setuptools import setup, find_packages
import os

# Load the long description from the README file
long_description = ""
if os.path.exists("README.md"):
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()

setup(
    name="bitmoro-sms",
    version="1.0.1",  # Increment version for new release
    description="A Python interface for sending bulk messages, dynamic messages, and handling OTP operations via the Bitmoro API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Bitmoro Dev Team",
    packages=find_packages(),
    python_requires=">=3.6",  # Specify compatible Python versions if required
    install_requires=[
        "requests>=2.22.0",  # Automatically install requests if not already installed  
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
