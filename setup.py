from setuptools import setup
import sys

sys.stderr.write(
    """
===============================
Unsupported installation method
===============================
django-openstax-accounts does not install with `python setup.py install`.
Please use `python -m pip install` instead.
"""
)
sys.exit(1)


# The below code will never execute, however GitHub is particularly
# picky about where it finds Python packaging metadata.
# See: https://github.com/github/feedback/discussions/6456
#
# To be removed once GitHub catches up.

setup(
    name="django-openstax-accounts",
    install_requires=[
        "Django>=3",
        "PyJWE>=1.0.0",
        "PyJWT>=1.7.1",
    ],
)