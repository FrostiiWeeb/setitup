# setitup

setitup is a tool for making it easier to build python projects.

This library aims to make it simple for you to build your python project.
all the utilities and functions you need to help make this job easier.

## Features

- [x] Modernic Python syntax.
- [x] Optimised in both speed and memory.
- [x] Wraps setuptools around an easier stntax.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install setitup.

```bash
pip install setitup
```

## Usage

setup.py

```python
# Import the setitup module
import setitup

# Instantiate a setitup setup object.
setup = setitup.Setup()

# Add a package name attribute to the setup instance.
@setup.attribute('name')
def name():
	return 'EXAMPLE_PROJECT'

# setitup also allows to add multiple attributes at once.
@setup.attributes('version', 'author', 'author_email')
def version_author_email():
	# you can return a tuple of values.
	return ('0.0.1', 'John Doe', 'johndoe@example.com')

# setitup makes it easier to add project urls and classifiers.
@parser.attributes('project_urls', 'classifiers')
def urls_classifiers():
	return (setitup.PROJECT_URLS([setitup.PROJECT_URL("Bug Tracker", 'https://github.com/pypa/sampleproject')]), setitup.CLASSIFIERS([setitup.CLASSIFIER('Development Status :: 3 - Alpha'), setitup.CLASSIFIER('Intended Audience :: Developers')]))

# we also make it easier to add files to long descriptions.
@setup.attributes('long_description', 'long_description_content_type')
def long_description_and_content_type():
	return (setitup.LONG_DESCRIPTION(setitup.FILE('README.md')), setitup.LONG_DESCRIPTION_CONTENT_TYPE('text/markdown'))

# Run the setup script
setup.run()
```

## Issues

If you find any bugs, issues, or unexpected behaviour while using the library,
you should open an issue with details of the problem and how to reproduce if possible.
Please also open an issue for any new features you would like to see added.

## Contributing

Pull requests are appreciated, but not required.
If it is a breaking change, please open an issue discussing the change.

## Links

- **License:** [MPL2.0](https://choosealicense.com/licenses/mpl-2.0/)
- **Repository:** [GitHub](https://github.com/FrostiiWeeb/setitup)
- **Documentation:** [ReadTheDocs](https://setitup.readthedocs.io/en/latest/) NOT WORKING AT THE MOMENT

**NOTE**: Please note that this project is released with a [Contributor Code of Conduct](CODE-OF-CONDUCT.md). By participating in this project you agree to abide by its terms.
