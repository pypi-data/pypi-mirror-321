from setuptools import setup, find_packages

setup(
    name='topsis_navneet_102203715',
    version='1.0.3',
    author='Navneet Sagar',
    author_email='sagar.26navneet@gmail.com',
    description='A Python package to perform TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/sagar09navneet/topsis_navneet_10203715',
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
