# coding: utf-8
r"""
高等数学:Advanced Mathematics
线性代数:Linear Algebra
概率论与数理统计:Probability and Statistics

数学相关:
gcd - 求最大公因数
hexCalculate - 16进制相关计算
cal_range - 范围计算
initialDeviator - 初始范围偏移器
complementDemonstrator - 补码演示器
complementCalculate - 补函数计算
binaryPow - 二进制幂计算,二进制位权
binaryPrefixRemoved - 去除前缀的二进制数
myrandom - 自定义随机数
PlaneCartesianCoordinateSystem - 平面直角坐标系

"""
__version__ = "0.1"
__author__ = "mingwe <shannonhacker@outlook.com>"
# __all__ = [
#     name
#     for name, obj in globals().items()
#     if all(
#         [
#             not name.startswith("_"),
#             not isinstance(obj, types.ModuleType),
#             name not in {"wantobjects"},
#         ]
#     )
# ]

import types
import time
import random


def gcd(a, b):
    """
    gcd - 求最大公因数
    """
    t = 0
    while b != 0:
        t = a % b
        a = b
        b = t
    return a


def hexCalculate(a, b):
    """
    十六进制计算器
    a,b is hex number.
    """
    return f"{a+b:#x}"


def cal_range(Bytes, var_type=None, unsigned=True):
    """
    计算数字类型范围
    cal_range(2,"短整型short int")

    """
    if var_type:
        print(f"{var_type}:{Bytes} Bytes")

    if unsigned:
        print(f"min,{0},Latex:-(2^{{{Bytes}*8}})")
        print(f"max,{2**(Bytes*8)-1=},Latex:(2^{{{Bytes}*8}})-1")
        print(f"{0}~{2**(Bytes*8)-1}")
        print(f"Latex:\\left [ 0,(2^{{{Bytes}*8}})-1 \\right ]")
        print()
    else:
        print(f"min,{-2**(Bytes*8-1)=},Latex:-(2^{{{Bytes}*8-1}})")
        print(f"max,{2**(Bytes*8-1)-1=},Latex:(2^{{{Bytes}*8-1}})-1")
        print(f"{-2**(Bytes*8-1)}~{2**(Bytes*8-1)-1}")
        print(f"Latex:\\left [ -(2^{{{Bytes}*8-1}}),(2^{{{Bytes}*8-1}})-1 \\right ]")
        print()


def initialDeviator():
    """
    初始范围偏移器
    """
    r = (-150, 150)
    r = list(map(lambda x: x + 150, r))
    print(r)
    r = list(map(lambda x: x / 6, r))
    print(r)
    r = list(map(lambda x: x + 2, r))
    print(r)


def complementDemonstrator(size):
    """
    补码演示器
    """

    def mybin(n, size):
        """
        parameter: n,size
        return: size string
        """
        if n < 0:
            s = bin(n)[3:]
        else:
            s = bin(n)[2:]
        return s.zfill(size)

    # unsigned int 无符号整数
    print("unsigned int 无符号整数")
    print(f"0~{(2**size)-1}")
    for i in range(0, ((2**size) - 1) + 1, 1):
        print(f"{i:<4}{mybin(i,size):10}")

    print()
    # signed int 有符号整数
    print("signed int 有符号整数")
    print(f"{-(2**(size-1))}~{(2**(size-1)-1)}")
    for i in range(-(2 ** (size - 1)), -1 + 1, 1):
        print(f"{i:<5}{mybin(i+(2**size),size):10}")

    for i in range(0, (2 ** (size - 1) - 1) + 1, 1):
        print(f"{i:<5}{mybin(i,size):10}")


def complementCalculate(n):

    # 补码，符号位不变，取反再加一
    text = ""
    text += "{},{}\n".format("原码", "1" + bin(n)[2:].zfill(7))
    text += "{},{}\n".format("反码", "1" + bin(n ^ 127)[2:].zfill(7))
    text += "{},{}\n".format("补码", "1" + bin((n ^ 127) + 1)[2:].zfill(7))

    return text


def binaryPow():
    """
    二进制位权
    """
    for i in range(-10, 10 + 1):
        print(i, 2 ** (i))


def binaryPrefixRemoved(n, size):
    """
    去除前缀的二进制数
    parameter: n,size
    return: size string
    """
    if n < 0:
        s = bin(n)[3:]
    else:
        s = bin(n)[2:]
    return s.zfill(size)


# import time,random
def myrandom(minimum, maximum):
    """
    自定义随机整数
    parameter: minimum,maximum
    return: a random integer number of range(minimum,maximum+1)
    """
    width = (maximum - minimum) + 1
    #     s = int(time.time()*(10**6))
    s = int(time.time_ns() / 1000)
    #     print(s,s%width,'inner')
    return (s % width) + minimum


def PlaneCartesianCoordinateSystem(coorLength=500):
    """
    这个程序使用turtle库绘制平面直角坐标系。
    """
    import turtle
    import tkinter

    # 获取屏幕宽度和高度
    root = tkinter.Tk()
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    root.destroy()
    # print(width, height)

    # 带平面直角坐标系的画布
    turtle.TurtleScreen._RUNNING = True
    coordinateTurtle = turtle.Turtle()
    screen = turtle.Screen()
    screen.tracer(0)  # 禁用动画
    screen.setup(screenWidth // 2, screenHeight, screenWidth // 2, 0)

    # coorLength 超出窗口范围
    if coorLength * 2 > screenWidth // 2:
        coorWidth_Half = int(screenWidth / 2 * (4 / 10))
    else:
        coorWidth_Half = coorLength

    if coorLength * 2 > screenHeight:
        coorHeight_Half = int(screenHeight * (4 / 10))
    else:
        coorHeight_Half = coorLength

    # 绘制x轴和y轴
    coordinateTurtle.color("red")
    coordinateTurtle.penup()
    coordinateTurtle.setheading(90)
    coordinateTurtle.goto(0, coorHeight_Half)
    coordinateTurtle.stamp()
    coordinateTurtle.pendown()
    coordinateTurtle.penup()
    coordinateTurtle.goto(-70, coorHeight_Half)
    coordinateTurtle.pendown()
    coordinateTurtle.write("y轴", font=("Arial", 16, "normal"))  # y轴标注
    coordinateTurtle.penup()
    coordinateTurtle.goto(0, coorHeight_Half)
    coordinateTurtle.pendown()
    coordinateTurtle.goto(0, -coorHeight_Half)

    coordinateTurtle.penup()
    coordinateTurtle.setheading(0)
    coordinateTurtle.goto(coorWidth_Half, 0)
    coordinateTurtle.stamp()
    coordinateTurtle.pendown()
    coordinateTurtle.penup()
    coordinateTurtle.goto(coorWidth_Half, -70)
    coordinateTurtle.pendown()
    coordinateTurtle.write("x轴", font=("Arial", 16, "normal"))  # x轴标注
    coordinateTurtle.penup()
    coordinateTurtle.goto(coorWidth_Half, 0)
    coordinateTurtle.pendown()
    coordinateTurtle.goto(-coorWidth_Half, 0)

    # 添加刻度点和标注

    x = range(-coorWidth_Half + (coorWidth_Half % 50), coorWidth_Half + 1, 50)
    for i in x:
        coordinateTurtle.penup()
        coordinateTurtle.goto(i, 10)  # 刻度线起点
        coordinateTurtle.pendown()
        coordinateTurtle.goto(i, 0)  # 刻度线终点

        coordinateTurtle.penup()
        coordinateTurtle.goto(i, -25)  # 向下偏移25单位
        coordinateTurtle.pendown()
        coordinateTurtle.write(i, font=("Arial", 12, "normal"))

    y = range(-coorHeight_Half + (coorHeight_Half % 50), coorHeight_Half + 1, 50)
    for j in y:
        coordinateTurtle.penup()
        coordinateTurtle.goto(10, j)  # 刻度线起点
        coordinateTurtle.pendown()
        coordinateTurtle.goto(0, j)  # 刻度线终点

        coordinateTurtle.penup()
        coordinateTurtle.goto(-35, j)  # 向左偏移30单位
        coordinateTurtle.setheading(270)
        coordinateTurtle.pendown()
        coordinateTurtle.write(j, font=("Arial", 12, "normal"))

    # 添加方向角度标注
    coordinateTurtle.penup()
    coordinateTurtle.goto(0, coorHeight_Half + 50)
    coordinateTurtle.setheading(0)
    coordinateTurtle.pendown()
    coordinateTurtle.write("北(90度)", font=("Arial", 12, "normal"))

    coordinateTurtle.penup()
    coordinateTurtle.goto(coorWidth_Half + 50, 0)
    coordinateTurtle.setheading(90)
    coordinateTurtle.pendown()
    coordinateTurtle.write("东(0度)", font=("Arial", 12, "normal"))

    coordinateTurtle.penup()
    coordinateTurtle.goto(0, -coorHeight_Half - 50)
    coordinateTurtle.setheading(180)
    coordinateTurtle.pendown()
    coordinateTurtle.write("南(270度)", font=("Arial", 12, "normal"))

    coordinateTurtle.penup()
    coordinateTurtle.goto(-coorWidth_Half - 50 - 20, 0)
    coordinateTurtle.setheading(270)
    coordinateTurtle.pendown()
    coordinateTurtle.write("西(180度)", font=("Arial", 12, "normal"))
    coordinateTurtle.hideturtle()
    coordinateTurtle.color("black")  # 画笔颜色和填充颜色
    coordinateTurtle.penup()
    coordinateTurtle.home()
    coordinateTurtle.pendown()
    del coordinateTurtle
    screen.update()  # 更新屏幕
    screen.tracer(1)  # 开启动画
    return screen, turtle


# 📜 定义模块的公开接口
__all__ = [
    # 🔍 遍历全局变量字典
    name
    for name, obj in globals().items()
    # ✅ 只选择不以下划线开头的变量
    if not name.startswith("_")
    # ✅ 排除类型为模块的对象
    and not isinstance(obj, types.ModuleType)
    # ✅ 排除在集合里的变量
    and name not in {"wantobjects", "types"}
]


if __name__ == "__main__":
    print(hexCalculate(0x1A1DF728, 0x950))

if __name__ == "__main__":
    cal_range(1, "字符型 char")
    cal_range(2, "短整型short int")
    cal_range(2, "整型 int")
    cal_range(4, "长整型long int")
    cal_range(8, "超长整型long long int")

if __name__ == "__main__":
    # 取反,1与255进行异或^操作，得到254，相异为真，相同为假，不进位的加法
    a = 0b00000001
    b = 0b11111111
    print(a ^ b)
if __name__ == "__main__":
    complementDemonstrator(4)

if __name__ == "__main__":
    for i in range(0, 255 + 1, 1):
        print(f"{i},{binaryPrefixRemoved(i,8)}")
        print(f"{~i},{binaryPrefixRemoved(~i,8)}")
        print(f"{i^255},{binaryPrefixRemoved(i^255,8)}")

if __name__ == "__main__":
    print(myrandom(1, 5))
    print(random.randint(1, 5))

if __name__ == "__main__":
    screen, turtle = PlaneCartesianCoordinateSystem(coorLength=500)
    turtle.TurtleScreen._RUNNING = True
    screen.mainloop()
