from setuptools import setup

setup(
    name="UGit",
    version="0.1.0",
    packages=["ugit"],
    install_requires=[],
    entry_points={
        "console_scripts": [
            "ugit=ugit.cli:main",
        ],
    },
)
