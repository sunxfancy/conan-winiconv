[![Build status](https://ci.appveyor.com/api/projects/status/bowhv868xqi033wh?svg=true)](https://ci.appveyor.com/project/sunxfancy/conan-winiconv)

# conan-winiconv

winiconv forked from lasote/conan-libiconv, and changed to <https://github.com/win-iconv/win-iconv> implements.


[Conan.io](https://conan.io) package for Win-iconv library

The packages generated with this **conanfile** can be found in [conan.io](https://conan.io/source/winiconv/1.14.0/sunxfancy/stable).

## Build packages

Download conan client from [Conan.io](https://conan.io) and run:

    $ python build.py

## Upload packages to server

    $ conan upload winiconv/1.14.0@sunxfancy/stable --all

## Reuse the packages

### Basic setup

    $ conan install winiconv/1.14.0@sunxfancy/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    winiconv/1.14.0@sunxfancy/stable

    [options]
    winiconv:shared=true # false

    [generators]
    txt
    cmake

Complete the installation of requirements for your project running:</small></span>

    conan install .

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.txt* and *conanbuildinfo.cmake* with all the paths and variables that you need to link with your dependencies.
