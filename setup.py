from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='apitaxcli',
    packages=find_packages(),  # this must be the same as the name above
    version='0.0.1',
    description='Apitax CLI provides a quick and easy interface into Apitax',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Shawn Clake',
    author_email='shawn.clake@gmail.com',
    url='https://github.com/ShawnClake/Apitax',  # use the URL to the github repo
    keywords=['restful', 'api', 'commandtax', 'scriptax'],  # arbitrary keywords
    include_package_data=True,
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=[
        'click',
        'requests',
        'certifi >= 14.05.14',
        'six >= 1.10',
        'python_dateutil >= 2.5.3',
        'urllib3 >= 1.15.1'
    ],
    entry_points={
        'console_scripts': [
            'apitax=cli.commands.Apitax:cli'
        ]
    },
    # entry_points='''
    #  [console_scripts]
    #  yourscript=yourpackage.scripts.yourscript:cli
    # ''',
)
