from setuptools import setup, find_packages
import os

setup(
    name="ldset_env",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "ldset_env=launch_darkly_set_env:launch_darkly_set_env",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A tool to set Launch Darkly environment variables",
    long_description=open("README.md").read() if os.path.exists("README.md") else "",
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/ldset_env",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
) 
