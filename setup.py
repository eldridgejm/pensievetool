from setuptools import setup, find_packages

setup(
    name="pensievetool",
    version="0.0.0",
    packages=["pensievetool"],
    entry_points={
        "console_scripts": [
            "pensievetool = pensievetool.cli:main",
        ]
    },
    install_requires=[ "markdown" ],
)
