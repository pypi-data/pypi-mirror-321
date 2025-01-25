from setuptools import setup, find_packages

setup(
    name='topsis_Bhavya_Jaiswal_102203087',
    version='1.0.3',
    author='Bhavya Jaiswal',
    author_email='bhavya.jaiswal27@gmail.com',
    description='A Python package to perform TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/bhavyajaiswal27/topsis_BhavyaJaiswal_102203087',
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
