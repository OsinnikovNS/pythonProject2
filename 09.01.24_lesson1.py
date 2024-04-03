# todo собрать информацию об ОС и версии Python
import platform
import sys

info = 'OS info is: \n{}\nPython version is: \n{} {}'.format(platform.uname(), sys.version, platform.architecture())
print(info)
with open('os_info.txt', 'w') as file:
    file.write(info)
