from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'  
]

setup(
    name='wikipediasearcher',
    version='0.0.1',
    description='a library that scrapes wikipedia',
    long_description = open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Ziegfred Zorrilla',
    author_email='ziegfredzorrilla23@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='wikipediasearcher',
    packages=find_packages(),
    install_requires=['BeautifulSoup4', 'lxml', 'requests', 'more-itertools', 'pytest']
)