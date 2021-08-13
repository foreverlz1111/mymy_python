# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')

    hour = float(input("hour : "))
    minute = float(input("minute : "))
    bitrate = float(input("bitrate per second / mbps : "))
    total_flow = (bitrate/8 * (3600*hour + 60*minute))
    if total_flow < 1024:
        print(str(float(bitrate) / 8 * float(3600 * hour + 60 * minute))+"MB")
    else:
        total_flow /= 1024
        print(str(total_flow)+"GB")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
