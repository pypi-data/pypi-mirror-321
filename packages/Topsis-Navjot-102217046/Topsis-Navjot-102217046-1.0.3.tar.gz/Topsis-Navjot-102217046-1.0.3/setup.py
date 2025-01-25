from setuptools import setup, find_packages

DESCRIPTION = 'Implementation of Topsis'

try:
    with open('README.md', 'r', encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

VERSION = '1.0.3'

setup(
    name="Topsis-Navjot-102217046",
    version=VERSION,
    author="Navjot",
    author_email="nsingh5_be22@thapar.edu",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['pandas', 'numpy'],
    project_urls={
        'Project Link': 'https://github.com/NavjotSingh2003/Topsis_Navjot'
    },
    keywords=['Topsis', 'Topsis-Navjot-102217046', 'Navjot', 'Topsis-Navjot', '102217046'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    ]
)
