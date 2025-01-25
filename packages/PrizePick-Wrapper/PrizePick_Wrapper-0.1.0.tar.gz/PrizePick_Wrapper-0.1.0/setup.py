from setuptools import setup, find_packages

setup(
    name='PrizePick_Wrapper',
    version='0.1.0',
    packages=find_packages(),
    description='PrizePick Wrapper to easily access the PrizePick API',
    install_requires=[
        "certifi==2024.12.14",
        "charset-normalizer==2.0.10",
        "idna==3.3",
        "requests==2.26.0",
        "urllib3==1.26.7"
    ]
)