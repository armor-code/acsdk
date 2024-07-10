from setuptools import setup, find_packages

setup(
    name="acsdk",
    version="0.1",
    description="A minimal SDK for interfacing with ArmorCode's API.",
    url="https://github.com/armor-code/customer-success/tree/main/python/acsdk",
    author="Brian Jenkins",
    author_email="bjenkins@armorcode.io",
    license="UNLICENSED",
    packages=find_packages(),
    install_requires=[
        "aiohttp",
        "asyncstdlib",
        "throttler",
        "tqdm"
    ]
)
