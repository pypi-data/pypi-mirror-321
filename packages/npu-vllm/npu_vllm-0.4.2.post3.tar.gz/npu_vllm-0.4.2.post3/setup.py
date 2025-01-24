import io
import os
import re
from typing import List
import setuptools
ROOT_DIR = os.path.dirname(__file__)

def get_path(*filepath) -> str:
    return os.path.join(ROOT_DIR, *filepath)

def find_version(filepath: str):
    """Extract version information from the given filepath.
    """
    with open(filepath) as fp:
        version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", fp.read(), re.M)
        print(version_match)
        if version_match:
            return version_match.group(1)
        raise RuntimeError("Unable to find version string.")
        
def read_readme() -> str:
    """Read the README file."""
    return io.open(get_path("README.md"), "r", encoding="utf-8").read()

def get_requirements() -> List[str]:
    """Get Python package dependencies from requirements.txt."""
    with open(get_path("requirements.txt")) as f:
        requirements = f.read().strip().split("\n")
    return requirements

setuptools.setup(
    name="npu-vllm",
    version=find_version(get_path("vllm_npu", "__init__.py")) + ".post3",
    author="Huawei",
    license="Apache 2.0",
    description=("A high-throughput and memory-efficient inference and "
                 "serving engine for LLMs"),
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my_package",
    project_urls={
        "Homepage": "https://github.com/yourusername/my_package",
        "Documentation": "https://github.com/yourusername/my_package",
    },
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    packages=setuptools.find_packages(exclude=("benchmarks", "examples", "tests")),
    python_requires=">=3.8",
    install_requires=get_requirements(),
)
