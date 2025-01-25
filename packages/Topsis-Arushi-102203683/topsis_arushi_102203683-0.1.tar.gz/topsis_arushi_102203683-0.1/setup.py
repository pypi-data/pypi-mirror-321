from setuptools import setup, find_packages

setup(
    name="Topsis-Arushi-102203683",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy'
    ],
    author="Arushi",
    author_email="Arushigadodia14@gmail.com",  # Replace with your actual email
    description="A Python package implementing TOPSIS method for MCDM",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ArushiGadodia/Topsis",  # Replace with your GitHub repo
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'topsis=topsis.topsis:main',
        ],
    },
    python_requires='>=3.6',
)