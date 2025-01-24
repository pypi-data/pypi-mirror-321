from setuptools import setup, find_packages

setup(
    name='szyfrowanie_json',
    version='0.1.0',
    author='Mateusz Zaręba',
    author_email='zarebamateusz12@gmail.com',
    description='Biblioteka do szyfrowania i odszyfrowywania plików JSON.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Mateusz-Zareba/Szyforwanie_json',
    packages=find_packages(),
    install_requires=[
        'cryptography',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
