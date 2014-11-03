#!/usr/bin/env python
from setuptools import setup


setup(
    name="django-shortcodes",
    version="0.3.2",
    description="WordPress shortcode support for Django",
    author="Mark Steadman",
    author_email="marksteadman@me.com",
    url="https://github.com/writepython/django-shortcodes",
    license="MIT",
    packages=[
        "shortcodes",
        "shortcodes.parsers",
        "shortcodes.templatetags",
    ],
    long_description=open("README.rst").read(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
    ],
)
