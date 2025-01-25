from setuptools import setup, find_packages

setup(
    name='my_pac_module',  # Ensure this is the new name
    version='0.1.0',
    description='A simple pac module',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Vasanth Naik',
    author_email='ramavath.naik@itilite.com',
    url='https://github.com/yourusername/my_pac_module',  # Updated project URL
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
