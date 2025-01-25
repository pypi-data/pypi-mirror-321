from setuptools import setup, find_packages

DESCRIPTION = 'Implementation of Topsis'

try:
    with open('README.md', 'r', encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

VERSION = '1.0.3'

setup(
    name="Topsis-Dhruv-102217050",
    version=VERSION,
    author="Dhruv",
    author_email="drajoria_be22@thapar.edu",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['pandas', 'numpy'],
    project_urls={
        'Project Link': 'https://github.com/dhruvRajoria/Topsis_Dhruv'
    },
    keywords=['Topsis', 'Topsis-Dhruv-102217050', 'Dhruv', 'Topsis-Dhruv', '102217050'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    ]
)
