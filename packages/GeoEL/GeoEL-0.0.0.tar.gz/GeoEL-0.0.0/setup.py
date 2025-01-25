import setuptools
import os

FILE_PATH = os.path.dirname(os.path.abspath(__file__))
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# 读取requirements.txt文件
requirements_path = os.path.join(FILE_PATH, 'requirement.txt')
with open(requirements_path, 'r') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="GeoEL",
    version="0.0.0",
    author="ChiBeiSheng",
    url='https://github.com/cbsux/GeoEL',
    author_email="cbs3307821258@qq.com",
    description="Geographically Weighted EnsembleLearning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    package_data={'': ['*.txt', '*.md']},
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)