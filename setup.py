from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in juzapp/__init__.py
from juzapp import __version__ as version

setup(
	name="juzapp",
	version=version,
	description="Dokumentation und Verwaltung in Jugendzentren",
	author="Moritz Kaimann",
	author_email="moritz@kaimann.net",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
