from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name="Topsis_vaibhav_tandon_102203877",
    version="1.0.1",
    author="VAIBHAV_TANDON",
    author_email="vtandon_be22@thapar.edu",
    description="A Python package for implementing the TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) method in Multi-Criteria Decision Making (MCDM)",
    long_description=readme(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas'
    ],
    entry_points={
        'console_scripts': [
            'topsis=topsis_jatin.topsis:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)