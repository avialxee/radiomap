from setuptools import setup

with open("README.md", "r") as rdme:
    desc = rdme.read()

setup(
    name = 'radiomap',
    version = '0.0.1.2',
    url='https://github.com/avialxee/radiomap',
    author='Avinash Kumar',
    author_email='avialxee@gmail.com',
    description='A python package which has radio astronomy calculation tools including spectral index map calculation.',
    py_modules=["radiomap"],
    package_dir={'':'src'},
    classifiers=["Programming Language :: Python :: 3.6",
                 "Programming Language :: Python :: 3.7",
                 "Programming Language :: Python :: 3.8",
                 "Programming Language :: Python :: 3.9",
                 "License :: OSI Approved :: BSD License",
                 "Intended Audience :: Science/Research",
                 ],
    long_description=desc,
    long_description_content_type = "text/markdown",
    install_requires=["astropy>=4.2.1", "numpy>= 1.20.3", 
                        "astroquery",
                      ],
    extras_require = {
        "dev" : ["pytest>=3.7",
        ]
    }

)
