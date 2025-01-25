from setuptools import setup, find_packages

setup(
    name='topsis_vardhan_102203268',
    version='1.0.3',
    author='Vardhan Singh Rawat',
    author_email='vardhanrawat1@gmail.com',
    description='A Python package to perform TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/vardhan-rawat/topsis_vardhan_102203268',
    packages=find_packages(),
    py_modules=['topsis'],
    install_requires=[
        'numpy',
        'pandas'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'topsis=topsis:run',
        ],
    },
)
