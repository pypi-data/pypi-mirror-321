from setuptools import setup, find_packages

setup(
    name='ariwebscraper',
    version='1.0.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'beautifulsoup4==4.9.3',
        'requests==2.25.1',
    ],
    url='https://github.com/ilkeryolundagerek/ariwebscraper',
    description='A simple web scraper',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    author='John/Jane Doe',
    author_email='j.doe@example.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
