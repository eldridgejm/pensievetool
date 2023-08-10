from setuptools import setup, find_packages

setup(
    name="pensievetool",
    version="0.0.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "pensievetool = pensievetool.cli:main",
        ]
    },
    install_requires=[ 'markdown>=3.4' ],
)
