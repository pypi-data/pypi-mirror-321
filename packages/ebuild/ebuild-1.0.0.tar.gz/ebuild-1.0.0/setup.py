from setuptools import setup, find_packages, Distribution


# Read long description from README.md
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Get version info from maix/version.py file
with open("ebuild/version.py", "r", encoding="utf-8") as f:
    vars = {}
    exec(f.read(), vars)
    __version__ = vars["__version__"]

# Read long requirements from requirements.txt
requirements = []
with open("requirements.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if line:
            requirements.append(line)

pkgs = find_packages()
print("-- found packages: {}".format(pkgs))

setup(
    # all keywords see https://setuptools.pypa.io/en/latest/references/keywords.html

    # Package name
    name='ebuild',

    # Versions should comply with PEP440: https://peps.python.org/pep-0440/
    version=__version__,

    author='Neutree',
    author_email='CZD666666@gmail.com',

    description='Easily cross compile your C/C++ projects or create your SDK',
    long_description=long_description,
    long_description_content_type="text/markdown",

    # The project's main homepage.
    url='https://github.com/neutree/ebuild',

    # All License should comply with https://spdx.org/licenses/
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Embedded Systems',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3'
    ],

    # What does your project relate to?
    keywords='embeded, cross compile, build system',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=pkgs,

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=requirements,

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        # 'dev': ['check-manifest'],
        # 'test': ['coverage'],
    },

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={
        # 'ebuild': ['*.so', "dl_lib/*.so*", "*.pyi", "**/*.pyi", "**/**/*.pyi"]
    },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    data_files=[
	        # ("",["LICENSE","README.md"])
        ],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'ebuild=ebuild.main_cli:main',
        ],
        # 'gui_scripts': [
        # ],
    },

)

