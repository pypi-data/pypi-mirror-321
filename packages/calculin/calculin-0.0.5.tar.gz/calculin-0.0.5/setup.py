import setuptools
from pathlib import Path

long_desc = Path("description").read_text(encoding="utf-8")

setuptools.setup(
    name="calculin",
    version="0.0.5",
    long_description=long_desc,
    packages=setuptools.find_packages(
        exclude=["codes"]
    )
)
