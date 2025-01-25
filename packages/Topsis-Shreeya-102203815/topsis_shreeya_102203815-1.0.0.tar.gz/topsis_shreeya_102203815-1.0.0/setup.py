from setuptools import setup, find_packages

def read_readme():
    with open('README.md', 'r', encoding='utf-8') as f:
        return f.read()

setup(
    name="Topsis-Shreeya-102203815",
    version="1.0.0",
    author="Shreeya",
    author_email="shreeya.kesarwani65@gmail.com",
    description="A Python package implementing TOPSIS method for MCDM problems",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/shreeya65/topsis_Shreeya_102203815",
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'openpyxl'
    ],
    entry_points={
        'console_scripts': [
            'topsis=topsis_Shreeya_102203815.topsis:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)