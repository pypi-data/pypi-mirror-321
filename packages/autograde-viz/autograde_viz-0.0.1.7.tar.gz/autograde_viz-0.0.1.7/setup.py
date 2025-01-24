import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="autograde-viz",
    version="0.0.1.7",
    author="Matthew Hull",
    author_email="matthewdhull@gmail.com.com",
    description="D3 Autograding Utility",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/matthewdhull/autograde-viz',
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.11",
)

