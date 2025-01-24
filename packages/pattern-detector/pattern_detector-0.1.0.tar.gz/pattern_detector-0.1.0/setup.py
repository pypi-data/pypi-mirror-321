from setuptools import setup, find_packages

setup(
    name='pattern_detector',
    version='0.1.0',
    description='A library for detecting patterns in time-series data.',
    author='Yigit Utku Bulut and Ahmet Faruk Minareci',
    author_email='yigit.utku.bulut@gmail.com, ahmetfaruk.minareci@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'joblib',
        'scipy'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
