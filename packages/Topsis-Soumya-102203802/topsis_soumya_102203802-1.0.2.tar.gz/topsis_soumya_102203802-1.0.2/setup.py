from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='Topsis-Soumya-102203802',  # Replace with your package name
    version='1.0.2',                 # Version number
    author='Soumya',                 # Your name
    author_email='soumyajindal2004@gmail.com',  # Replace with your email
    description='A Python package for implementing the TOPSIS algorithm.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/soumya-1313/Topsis-Soumya-102203802',  # Replace with your GitHub URL (optional)
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'openpyxl'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
