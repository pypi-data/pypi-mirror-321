from setuptools import setup, find_packages

setup(
    name="convertomp",  
    version="1.0.0",  
    packages=find_packages(),  
    install_requires=["mediafire_dl","requests","beautifulsoup4"],  
    py_modules=["convertomp"],
    entry_points={
        'console_scripts': [
            'convertomp=convertomp:main', 
        ],
    },
    author="brabos",
    author_email="",
    description="Um conversor samp para open.mp",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Brabosxtz/Conversor-samp-para-open.mp",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6', 
)
