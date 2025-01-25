from setuptools import setup, find_packages

setup(
    name='topsis-manya-102203284',  # Package name on PyPI
    version='1.0.0',
    author='Manya Verma',                
    author_email='manyaverma0154@gmail.com',  # Your email
    description='A Python package to implement TOPSIS for decision-making problems.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/manyaverma11/topsis-manya-102203284',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
