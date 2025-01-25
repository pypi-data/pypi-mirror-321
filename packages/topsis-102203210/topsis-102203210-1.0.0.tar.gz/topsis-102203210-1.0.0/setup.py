#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from setuptools import setup, find_packages

setup(
    name='topsis-102203210',  # Replace with your unique package name
    version='1.0.0',
    author='Anureet Kaur',
    author_email='cheemaanureet2811@gmail.com',
    description='A Python package for TOPSIS multi-criteria decision-making.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/reet1104/Topsis',  # Update with your GitHub repo URL
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'scipy',
    ],
    
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        "console_scripts": [
            "topsis=Topsis.topsis:main",  # Link 'topsis' command to the 'main' function in topsis.py
        ],
    },
)



