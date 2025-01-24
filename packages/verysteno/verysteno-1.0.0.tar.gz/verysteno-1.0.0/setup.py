from setuptools import setup, find_packages

setup(
    name="verysteno",
    version="1.0.0",
    description="A library for encoding and decoding messages in sound and images using steganography.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="XenonPy",
    author_email="xenonpy@wearehackerone.com",
    url="https://github.com/XenonPy/steno",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pillow"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
