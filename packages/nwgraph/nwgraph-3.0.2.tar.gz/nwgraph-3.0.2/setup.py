"""setup.py -- note use setuptools==73.0.1; older versions fuck up the data files, newer versions include resources."""
from pathlib import Path
from setuptools import setup

NAME = "nwgraph"
VERSION = "3.0.2"
DESCRIPTION = "Neural Wrappers Graph library"
URL = "https://gitlab.com/neuralwrappers/nwgraph"

CWD = Path(__file__).absolute().parent
with open(CWD/"README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

REQUIRED = [
    "torch>=2.5.1",
    "tqdm==4.67.1",
    "overrides==7.7.0",
    "graphviz==0.20.1",
    "colorama==0.4.6",
    "lovely_tensors==0.1.17",
    "numpy==1.26.4",
    "loggez==0.4.2",
]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=URL,
    install_requires=REQUIRED,
    dependency_links=[],
    license="WTFPL",
    python_requires=">=3.10",
)
