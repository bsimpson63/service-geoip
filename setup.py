from setuptools import setup, find_packages

from baseplate.integration.thrift.command import ThriftBuildPyCommand


setup(
    name="reddit_service_geoip",
    packages=find_packages(),
    install_requires=[
        "baseplate",
        "geoip2", # maxmind's geoip library
        # also want geoipupdate--how can a service make a config file e.g. /usr/local/etc/GeoIP.conf
        # also need a cron to run the update http://dev.maxmind.com/geoip/geoipupdate/
        # also need to create the directory that updates go in!
    ],
    cmdclass={
        "build_py": ThriftBuildPyCommand,
    },
)
