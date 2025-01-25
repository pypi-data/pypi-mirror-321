from setuptools import setup, find_packages

with open("README.md", "r") as file:
    description = file.read()


setup(
    name='PrizePick_Wrapper',
    version='0.2.0',
    packages=find_packages(),
    description='PrizePick Wrapper to easily access the PrizePick API',
    install_requires=[
        "certifi==2024.12.14",
        "charset-normalizer==2.0.10",
        "idna==3.3",
        "requests==2.26.0",
        "urllib3==1.26.7"
    ],
    long_description=description,
    long_description_content_type="text/markdown",
)