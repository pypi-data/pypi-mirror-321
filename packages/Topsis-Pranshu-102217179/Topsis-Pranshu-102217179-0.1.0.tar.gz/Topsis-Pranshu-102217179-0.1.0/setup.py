from setuptools import setup, find_packages

setup(
    name='Topsis-Pranshu-102217179',  # This is the name of your package
    version='0.1.0',  # Version of your package
    description='TOPSIS method implementation by Pranshu',  # A short description of your package
    long_description=open('README.md').read(),  # Read the long description from README
    long_description_content_type='text/markdown',  # Specify that it's markdown format
    author='Pranshu',  # Your name
    author_email='pranshugargktl@gmail.com',  # Your email address
    url='https://github.com/pranshugarg123/Topsis-Pranshu-102217179',  # Link to your repository (or wherever your package is hosted)
    packages=find_packages(),  # This will find all packages in the directory
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[  # List any dependencies your package needs
        'pandas',  # pandas for data manipulation
        'numpy',  # numpy for numerical operations
    ],
    python_requires='>=3.6',  # Minimum required Python version
)
