from setuptools import setup, find_packages

setup(
    name="TopsisDanish102203633",  # Package Name
    version="0.1",  # Package Version
    packages=find_packages(),  # Automatically find all packages in the directory
    install_requires=[  # External dependencies (none for now)
        "pandas", 
        "numpy",
        "streamlit",
        "SpeechRecognition",
    ],
    description="A simple implementation of the TOPSIS decision-making method with additional features.",
    author="Danish",  # Your name
    author_email="dsharma.workmain@gmail.com",  # Your email address
    long_description="This package allows easy decision-making using the TOPSIS method. It includes features like file upload and voice control.",
    long_description_content_type='text/markdown',
    url="https://github.com/Danish2op/voice-controlled-topsis-package.git",  # Your GitHub link (if any)
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
