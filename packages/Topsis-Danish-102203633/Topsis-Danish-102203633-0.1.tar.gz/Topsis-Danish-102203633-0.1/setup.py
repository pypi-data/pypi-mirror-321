# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="Topsis-Danish-102203633",  # Package Name
    version="0.1",  # Package Version
    packages=find_packages(),  # Automatically find all packages in the directory
    install_requires=[  # External dependencies
        "pandas", 
        "numpy",
        "streamlit",
        "SpeechRecognition",
    ],
    description="A simple implementation of the TOPSIS decision-making method with additional features.",
    author="Danish",  # Your name
    author_email="dsharma.workmain@gmail.com",
    long_description=open('README.md', encoding='utf-8').read(),  # Correct file handling
    long_description_content_type='text/markdown',
    url="https://github.com/Danish2op/voice-controlled-topsis-package",  # Your GitHub link (if any)
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
