# docutils-extensions's setup.py
from distutils.core import setup
setup(
    name = "docutils-extensions",
    version = "0.1.0",
    license = "MIT",
    requires = ["docutils (>=0.7)"],

    description = "A docutils extension for allowing easy directive contribution.",
    long_description = open('README.txt').read(),
    author = "Robin Jarry",
    author_email = "robin.jarry@gmail.com",
    url = "https://github.com/diabeteman/rst_extensions",
    download_url = "https://github.com/diabeteman/rst_extensions",
    keywords = ["docutils", "rst", "reStructuredText"],
    classifiers = [
        "Programming Language :: Python",
        "Development Status :: Beta",
        "Environment :: Windows",
        'Intended Audience :: End Users/Desktop',
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Document Generation",
    ],
    packages = ["docutilsextensions"],
    package_dir = {'': 'src'},
    package_data = {'docutilsextensions' : ["src/docutilsextensions/*.txt"] },
    scripts = ['src/scripts/rst', 'src/scripts/rst.cmd', 'src/scripts/rst.py']
)

