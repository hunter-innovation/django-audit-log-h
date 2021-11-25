import os
from setuptools import setup, find_packages


def get_readme():
    try:
        return open(
            os.path.join(os.path.dirname(__file__), "README.md")
        ).read()
    except IOError:
        return ""


setup(
    name="django-audit-log",
    version="0.7.0",
    packages=find_packages(exclude=["testproject"]),
    author="Vasil Vangelovski",
    author_email="vvangelovski@gmail.com",
    license="New BSD License (http://www.opensource.org/licenses/bsd-license.php)",
    description="Audit trail for django models",
    long_description=get_readme(),
    url="https://github.com/Atomidata/django-audit-log",
    download_url="https://github.com/Atomidata/django-audit-log/downloads",
    include_package_data=True,
    zip_safe=False,
    classifiers="Django 3.2"
    + [
        "Environment :: Plugins",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ],
)
