from setuptools import setup
# Read the content of the README.md file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(name="topsis_102217115",
      version="1.1",
      description="This is a package for TOPSIS score calculation",
      long_description=long_description,
      long_description_content_type="text/markdown",
      author="Gurleen",
      packages=['topsis_102217115'],
      install_requires=[
        "pandas>=1.0.0",  
        "numpy>=1.18.0"]
      )