from setuptools import setup, find_packages

from baseplate.integration.thrift.command import ThriftBuildPyCommand


setup(
    name="reddit_service_geoip",
    packages=find_packages(),
    install_requires=[
        "baseplate",
    ],
    cmdclass={
        "build_py": ThriftBuildPyCommand,
    },
)
