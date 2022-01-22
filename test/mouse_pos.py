# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time

from pymouse import PyMouse

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


    m = PyMouse()
    a = m.position()    #获取当前坐标的位置
    print(a)

    m.move(850, 460)   #鼠标移动到(x,y)位置
    a = m.position()
    print(a)
    #
    # m.click(31, 100)  #移动并且在(x,y)位置左击
    # time.sleep(1)
    # m.click(31, 120)  # 移动并且在(x,y)位置左击
