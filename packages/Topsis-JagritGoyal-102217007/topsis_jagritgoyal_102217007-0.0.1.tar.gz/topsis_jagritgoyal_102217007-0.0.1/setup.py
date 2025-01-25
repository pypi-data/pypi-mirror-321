from setuptools import setup, find_packages

setup(
    name='Topsis_JagritGoyal_102217007',
    version='0.0.1',
    author='Jagrit Goyal',
    author_email='jagritgoyal31@gmail.com',
    description='A Python package to perform TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/jagrit-goyal/Topsis',
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
            'topsis=topsis.topsis:run',
        ],
    },
)
