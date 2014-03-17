from setuptools import setup, find_packages

setup(
    name="selenate",
    version="0.1.2",
    author="William Mak",
    url="https://github.com/wmak/selenate",
    packages=find_packages(exclude=['*.tests']),
    test_suite="selenate.tests",
    description="Web Automation made easy",
    install_requires=[
        "selenium >= 2.40.0",
    ],
)
