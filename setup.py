from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

setup(
    name="selenate",
    version="0.3.0",
    author="William Mak",
    author_email="WilliamSYMak@gmail.com",
    url="https://github.com/wmak/selenate",
    packages=find_packages(exclude=['*.tests']),
    test_suite="selenate.tests",
    description="Web Automation made easy",
    install_requires=[
        "selenium >= 2.40.0",
    ],
    long_description=readme,
    license='Apache 2.0',
)
