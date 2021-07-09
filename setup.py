import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wikipedia-searcher",
    version="0.0.4",
    author="Ziegfred Zorrilla",
    author_email="ziegfredzorrilla23@gmail.com",
    description="A script that scrapes wikipedia",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires = [
        'beautifulsoup4==4.9.3',
        'certifi==2021.5.30',
        'chardet==4.0.0',
        'idna==2.10',
        'lxml==4.6.3',
        'more-itertools==8.8.0',
        'requests==2.25.1',
        'soupsieve==2.2.1',
        'urllib3==1.26.6'
    ],
    python_requires=">=3.9",
)