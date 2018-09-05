from setuptools import setup
from setuptools import find_packages

setup(
    name='analytics',
    version='0.0.1',
    description='''Data Science and Machine Learning Modelings''',
    author='Kevin Liao',
    author_email='kevin.lwk.liao@gmail.com',
    license='MIT',
    install_requires=[
        'numpy>=1.9.1',
        'scipy>=0.14',
        'pandas>=0.20.1',
        'scikit-learn>=0.19.1',
        'nltk>=3.3'
    ],
    extras_require={
        'visualize': [
            'seaborn>=0.8.1',
            ],
    },
    dependency_links=[],
    platforms='any',
    packages=find_packages(),
)