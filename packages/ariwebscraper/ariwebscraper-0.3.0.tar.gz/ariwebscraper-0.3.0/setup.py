from setuptools import setup, find_packages

setup(
    name='ariwebscraper',
    version='0.3.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'beautifulsoup4==4.9.3',
        'requests==2.25.1',
    ],
    description='A simple web scraper',
    author='John/Jane Doe',
    author_email='j.doe@example.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
