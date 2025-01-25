# from setuptools import setup, find_packages

# setup(
#     name='xander-ai',
#     version='0.2.4',
#     packages=find_packages(),
#     install_requires=[
#         'pandas', 
#         'numpy', 
#         'chardet', 
#         'tensorflow', 
#         'scikit-learn', 
#         'openpyxl', 
#         'channels', 
#         'asgiref', 
#         'keras', 
#         'keras-tuner', 
#         'joblib', 
#         'requests', 
#         'nltk',
#         'matplotlib',
#         'xgboost'
#     ],
#     author='Atulit gaur',
#     author_email='atulit23@gmail.com',
#     description='Xander - A package to train Classification, Regression, and Image Classification models.',
#     long_description=open('README.md').read(),
#     long_description_content_type='text/markdown',
#     classifiers=[
#         'Programming Language :: Python :: 3',
#         'License :: OSI Approved :: MIT License',
#         'Operating System :: OS Independent',
#     ],
#     include_package_data=True,
# )
from setuptools import setup, find_packages

setup(
    name='xander-ai',
    version='0.2.6',
    packages=find_packages(include=["xander_ai", "xander_ai.*"]),
    install_requires=[
        'pandas',
        'numpy',
        'chardet',
        'tensorflow',
        'scikit-learn',
        'openpyxl',
        'channels',
        'asgiref',
        'keras',
        'keras-tuner',
        'joblib',
        'requests',
        'nltk',
        'matplotlib',
        'xgboost'
    ],
    author='Atulit Gaur',
    author_email='atulit23@gmail.com',
    description='Xander - A package to train Classification, Regression, and Image Classification models.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    include_package_data=True,  # Ensures files listed in MANIFEST.in are included
    # package_data is optional if you have MANIFEST.in handling it
    # package_data={
    #     'xander_ai': ['**/*.pyc'],
    # }
)
