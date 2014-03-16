from setuptools import setup, find_packages

setup(
    name="selenate",
    version="0.1.1",
    author="William Mak",
    packages=find_packages(exclude=['*.tests']),
    test_suite="selenate.tests",
    description="Web Automation made easy",
    install_requires=[
        "selenium >= 2.40.0",
    ],
)
