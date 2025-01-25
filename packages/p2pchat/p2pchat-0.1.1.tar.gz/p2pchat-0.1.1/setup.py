from setuptools import setup, find_packages

setup(
    name="p2pchat",
    version="0.1.1",  # Incremented version number
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'p2pchat': ['api/*.py', 'utils/*.py'],
    },
    install_requires=[
        'aiohttp',
        'asyncio'
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python package for P2P chat bot development",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/p2pchat",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
