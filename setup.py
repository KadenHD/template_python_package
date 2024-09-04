from setuptools import setup, find_packages
import os
import io

# Package meta-data.
NAME = ""
VERSION = ""
DESCRIPTION = ""
AUTHOR = ""
AUTHOR_EMAIL = ""
PYTHON_REQUIRES = ""
INSTALL_REQUIRES = []
EXTRAS_REQUIRE = {
    "dev": [
        "flake8",
        "mypy",
        "pytest",
        "build",
        "twine",
        "sphinx"
    ]
}

# Import and use README (which must be inside MANIFEST.in) as long-description.
try:
    here: str = os.path.abspath(os.path.dirname(__file__))
    with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        LONG_DESCRIPTION = "\n" + f.read()
except FileNotFoundError:
    LONG_DESCRIPTION = DESCRIPTION

# Launch now the setup
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    python_requires=PYTHON_REQUIRES,
    extras_require=EXTRAS_REQUIRE
)
