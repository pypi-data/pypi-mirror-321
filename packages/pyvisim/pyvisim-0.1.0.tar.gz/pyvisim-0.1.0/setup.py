from setuptools import setup, find_packages

setup(
    name="pyvisim",
    version="0.1.0",
    author="Nhat Huy Vu",
    author_email="vunhathuy234@gmail.com",
    description="A Python library for image similarity analysis using Image Encoders and Neural Networks",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/MechaCritter/Python-Visual-Similarity",
    license="MIT",
    packages=find_packages(include=["pyvisim", "pyvisim.*"]),
    python_requires=">=3.10",
    install_requires=[
        "opencv-python>=4.5.3",
        # Add other dependencies here
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
