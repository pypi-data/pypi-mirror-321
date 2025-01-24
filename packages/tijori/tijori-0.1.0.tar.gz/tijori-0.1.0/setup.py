from setuptools import setup, find_packages

setup(
    name='tijori',
    version='0.1.0',
    description='A Python library to scrape financial data from Tijori Finance for analysis with LLMs.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Phanindra Parashar',
    author_email='phanindraparashar@gmail.com',
    url='https://github.com/yourusername/phanindraparashar-tijori',  # Replace with your repo URL
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4==4.12.3',
        'pandas==1.5.3',
        'selenium==4.27.1',
    ],
    classifiers=[
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
    include_package_data=True,
)
