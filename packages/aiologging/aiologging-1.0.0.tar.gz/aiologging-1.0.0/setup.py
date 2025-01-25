from setuptools import setup, find_packages


def readme():
    with open("README.md", "r") as file:
        return file.read()


setup(
    name="aiologging",
    version="1.0.0",
    author="zvenios",
    author_email="kont.vladdd@gmail.com",
    description="Asynchronous module for logging in python.\n\'import aiologging\' and you can use it, it's simple",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/users/zvenios/projects/2",
    packages=find_packages(),
    install_requires=[],
    classifiers=[

    ],
    keywords="aio log logger logging aiolog aiologger aiologging",
    project_urls={
        "GitGub": "https://github.com/zvenios"
    },
    python_requires=">=3.11"
)