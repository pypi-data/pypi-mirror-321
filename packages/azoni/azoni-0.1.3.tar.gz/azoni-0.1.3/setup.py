from setuptools import setup, find_packages

setup(
    name='azoni',                  # Name of the package
    version='0.1.3',                    # Version
    description='azoni test agent',  # Short description
    #long_description=open('README.md').read(),  # Detailed description
    long_description_content_type='text/markdown',
    author='Azoni',
    author_email='azoninft@gmail.com',
    url='https://github.com/azoni/azoni-package',
    license='MIT',
    packages=find_packages(),          # Automatically find all packages
    install_requires=[                 # Dependencies
    ],
    classifiers=[                      # Metadata
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
