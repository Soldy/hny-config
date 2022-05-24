from setuptools import setup

with open("README.md", "r") as readme:
     long_description = readme.read()

setup(
    name='hny-config',
    version='0.1.0',
    description='',
    py_modules=['hnyconfig'],
    package_dir={'hnyconfig':'src'},
    packages=['hnyconfig'],
    install_requires=[],
    extras_require={
        "dev":[
            "pytest>=6.2"
        ]
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Topic :: Utilities'
    ],
    url='https://github.com/Soldy/hny-config',
    author='Soldy',
    long_description=long_description,
    long_description_content_type="text/markdown"
)
