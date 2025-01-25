from setuptools import setup, find_packages

VERSION = '0.0.3'
DESCRIPTION = 'Extension / Wrapper for structlog library.'
LONG_DESCRIPTION = 'Extension / Wrapper for structlog library.'

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="elastic_structlog",
    version=VERSION,
    author="Nuriel Gadilov",
    author_email="nurielprivet@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["elasticsearch", "structlog"],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'

    keywords=['python', 'structlog', 'es', "elastic"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
