import setuptools

with open('README.md','r') as fh:
	long_description=fh.read()

setuptools.setup(
	name="ApiTestGenerics",
	version="1.0.0",
	author=" ",
	author_email="",
	description="Generic tool for api testing",
	long_description="generic tool verious api testing",
	packages=setuptools.find_packages(),
	install_requires=["testcase","requests"],
	classifiers=["Programming Language::Python::2.7",
				"License:: :: ",
				"Operationg Syster ::OS Independent",



	],
	python_requires='>=2.7',
	)