import os
import platform
import sys

if __name__ == "__main__":
    os.system('conan export lasote/stable')
   
    def test(settings):
        argv =  " ".join(sys.argv[1:])
        command = "conan test %s %s" % (settings, argv)
        retcode = os.system(command)
        if retcode != 0:
            exit("Error while executing:\n\t %s" % command)


    if platform.system() == "Windows":
        for visual_version in [10, 12, 14]:
            compiler = '-s compiler="Visual Studio" -s compiler.version=%d ' % visual_version
            # Shared x86
            test(compiler + '-s arch=x86 -s build_type=Debug -s compiler.runtime=MDd')
            test(compiler + '-s arch=x86 -s build_type=Release -s compiler.runtime=MD')
            if visual_version != 10:
                # Shared x86_64
                test(compiler + '-s arch=x86_64 -s build_type=Debug -s compiler.runtime=MDd')
                test(compiler + '-s arch=x86_64 -s build_type=Release -s compiler.runtime=MD')
