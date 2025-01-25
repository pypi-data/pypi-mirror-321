from setuptools import setup, find_packages

# Read the README file with UTF-8 encoding
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='topsis102203633Danishsharma',
    version='1.0.1',  
    description='A Python package for TOPSIS implementation',
    author='Danish Sharma',
    author_email='dsharma.workmain@gmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown',  # Ensure correct markdown format
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scipy',
        'matplotlib',
        'SpeechRecognition',
    ],
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],

    python_requires='>=3.6',
)
