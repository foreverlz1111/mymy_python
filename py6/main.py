# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import platform

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi()
    print("platform.system(): "+platform.system())
    print("platform.machine(): "+platform.machine())
    print("platform.version(): "+platform.version())
    print("platform.release(): "+platform.release())
    print(platform.uname())
    print("platform.python_version()"+platform.python_version())
    print("platform.python_build()"+platform.python_build())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
