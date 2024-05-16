from setuptools import setup

setup(
    name="version_sync",
    version="0.1.0",
    py_modules=["version_sync"],
    entry_points={
        "console_scripts": [
            "version_sync = version_sync:main",
        ],
    },
)
