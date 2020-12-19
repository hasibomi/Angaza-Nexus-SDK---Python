import setuptools

with open('README.md', 'r') as file:
    long_description = file.read()

setuptools.setup(
    name='Angaza Nexus SDK - Python',
    version='0.0.2',
    author='Hasibur Rahman Omi',
    author_email='hrahmanomi@gmail.com',
    description='SDK for Angaza Nexus API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com:hasibomi/Angaza-Nexus-SDK---Python',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.6',
)
