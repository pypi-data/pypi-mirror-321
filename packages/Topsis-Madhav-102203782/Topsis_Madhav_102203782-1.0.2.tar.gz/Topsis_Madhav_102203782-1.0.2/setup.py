from setuptools import setup, find_packages

setup(
    name='Topsis_Madhav_102203782',
    version='1.0.2',
    author='Madhav Garg',
    author_email='gargmadhav90@gmail.com',
    description='A Python package to perform TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
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
