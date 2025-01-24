from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="batch-log-manager",
    version="0.1.0",
    packages=find_packages(),
    install_requires=requirements,
    author="Jacob Vartuli-Schonberg",
    author_email="jacob.vartuli.92@gmail.com",
    description="A Python package for managing logs.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/OpenJ92/log-manager",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)

