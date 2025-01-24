from setuptools import setup, find_packages

setup(
    name="SAHANI_TTS",
    version="0.1.0",
    author="ARYAN SAHANI",
    author_email="sahaniaryan321@gmail.com",
    description="A package to convert text to speech with animated printing.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Aryan-crypt/J.A.R.V.I.S",  # Update with your GitHub repo URL
    packages=find_packages(),
    install_requires=[
        "requests",
        "playsound==1.2.2",
        "typing"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
