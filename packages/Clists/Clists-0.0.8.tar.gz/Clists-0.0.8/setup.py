from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    # 'Operating System :: Microsoft :: Windows :: Windows 11',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
]

setup(
    name='Clists',
    version='0.0.8',
    description='A simple package to hyper-optimise list operations by caching.',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    long_description_content_type='text/markdown',
    url='',
    author='Seth Brockman',
    author_email='brockman.seth@google.com',
    license='MIT',
    classifiers=classifiers,
    keywords=['list caching','caching','list','list optimisation', 'list operations'],
    packages=find_packages(),
    install_requires=[''],
)