ebuild
====

## Intro

Easily cross compile your C/C++ projects or create your SDK with simple Python scripts, let forget Makefile or CMake.

## Features

* Easy to use, only a few fill-in-the-blanks based on simple template.
* Scalable and flexible, Use Python script, easy-to-use and powerfull, real program language, not string based language like CMake.
* Configurable, support menuconfig.

## Install

Ensure you have Python installed first, then:

```shell
pip install ebuild
```

Execute `ebuild -h` to start.

## First project

```shell
ebuild create hello_world
cd hello_world
ebuild  # or ebuild build
ebuild run
ebuild clean
ebuild distclean
```

In `hello_world` directory have an `ebuild_config.py` file like:
```python
from ebuild import find_src

class Project:
    build_type = "binary"  # binary, shared, static
    id = "hello"
    name = "Hello"
    desc = "Simple hello program"
    home = "https://github.com/neutree/ebuild"
    license = "MIT"
    version = "1.0.0"

    def on_add_src(self, dl_dir):
        srcs = find_src(".", [".c", ".cpp"], resursive = False)
        return srcs
```

* `class Project` means this is a project.
* `build_type = "binary"` means we need to generate a executable binary file.
* `id` is the unique name of this project, the final binary file name will be this.
* `name` is the name of this project.
* `desc` `home` `license` are description, home url, open source license.
* `version` is the version of project, format must be like `major.minor.patch`
* `on_add_src` function need we return the souce files list, so we invoke `find_src` to find all `c/cpp` file in current directory.

## Cross compile

When execute `ebuild`, will automatically build for host(your PC) with default toolchain(e.g. gcc on Linux).
If you want to cross compile, you need to assign your platform info, by default `ebuild` ingrated some platforms like `linux/windows/macos` and some special embeded platforms, you can find them by `ebuild platform list`, every platform has some toolchains, use `ebuild toolchain platform_name` to show.
Then use `ebuild config platform=linux toolchain=gcc`, this config will save to this project's `.config` file, remove `.config` file will change back to default platform.

If you want to customize a new special platform or toolchain, edit or create `.yaml` file in `~/.ebuild/platforms`, or commit code to `ebuild`.

## Menuconfig

Execute `ebuild menu`, then you can select options in GUI mode.
Press `Q` or `ESC` to exit, the config items will be saved to `build/config` directory, and you can use config item in source like
```c
#include "global_config.h"

#if CONFIG_LIBNAME_XXXX
#endif
```
Which `LIBNAME` is the uppercase of library name, `XXXX` is uppercase config item in the library.

## Add requirements

If your project want to use some library, return your requires in `on_requires` function like:
```python
class Project:
    def on_requires(self):
        '''
            Returns:
                requires I need, list type.
        '''
        requires = [
            # "inifile2"
            # "inifile2 >= 1.0.0"
            # "inifile2 == 1.0.0"
            # "inifile2 <= 1.0.0"
            # "inifile2 > 1.0.0"
        ]
        return requires
```

Where to find libraries:
* [Official libraries repository](): use int `add_requires` will automatically download.
* Third party libraries contains `ebuild_config.py`:
  * Download manually and put in `~/.ebuild/libraries`.
  * Or just return github address like ["git+https://github.com/xxx/xxx.git"], ebuild will automatically download it, ensure you have `git` installed and good network can connecte to `github.com`.

## Customize a library

Write a `Lib` class in `ebuild_config.py` file, implement callbacks

```python
class Lib:
    def on_add_include(self, dl_dir):
        return ["inc"]

    def on_add_src(self, dl_dir):
        srcs = find_src("src", [".c", ".cpp"], resursive = False)
        return srcs
```


## Change data store path

All downloaded data will be downloaded to `~/.ebuild`, you can customize this path by `ebuild config data_path=/xxx/xxx/xxx`



