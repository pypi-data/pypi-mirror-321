import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyadguard",
    version="0.0.1",
    author="Lars Jelschen",
    author_email="mail@lars-jelschen.de",
    description="Python API Wrapper for Adguard Home",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ljelschen/pyadguard",
    project_urls={
        "Bug Tracker": "https://github.com/ljelschen/pyadguard/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7"
)
