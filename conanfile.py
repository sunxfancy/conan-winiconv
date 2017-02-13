from conans import ConanFile
import os
from conans.tools import download
from conans.tools import unzip
from conans import CMake


class GTestConan(ConanFile):
    name = "winiconv"
    version = "1.14.0"
    ZIP_FOLDER_NAME = "win-iconv-master"
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    exports = "CMakeLists.txt"
    url="http://github.com/sunxfancy/conan-winiconv"
    license="https://github.com/win-iconv/win-iconv"

    def config(self):
        try: # Try catch can be removed when conan 0.8 is released
            del self.settings.compiler.libcxx
        except:
            pass

    def conan_info(self):
        self.info.settings.compiler.runtime = "MDd" if self.settings.build_type == "Debug" else "MD"

    def source(self):
        zip_name = "master.zip"
        url = "https://github.com/win-iconv/win-iconv/archive/master.zip"
        download(url, zip_name)
        unzip(zip_name)
        os.unlink(zip_name)

    def build(self):
        cmake = CMake(self.settings)
        self.output.warn(cmake.command_line)
        self.run("cd %s && mkdir _build" % self.ZIP_FOLDER_NAME)
        cd_build = "cd %s/_build" % self.ZIP_FOLDER_NAME
        self.run('%s && cmake .. %s -DBUILD_SHARED_LIBS=ON' % (cd_build, cmake.command_line))
        self.run("%s && cmake --build . %s" % (cd_build, cmake.build_config))

    def package(self):
        # Copying headers
        self.copy(pattern="*.h", dst="include", src="%s/include" % self.ZIP_FOLDER_NAME, keep_path=True)

        # Copying dynamic libs
        self.copy(pattern="*.dll", dst="bin", src="%s/_build" % self.ZIP_FOLDER_NAME, keep_path=False)
        self.copy(pattern="*.lib", dst="lib", src="%s/_build" % self.ZIP_FOLDER_NAME, keep_path=False)


    def package_info(self):
        self.cpp_info.libs = ['iconv']
