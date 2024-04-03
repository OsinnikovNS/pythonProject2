# todo собрать информацию об ОС и версии Python
import platform
import sys

info = f'OS info is: \n{platform.uname()}\nPython version is: \n{sys.version} {platform.architecture()}'
print(info)
with open('os_info.txt', 'w') as file:
    file.write(info)
