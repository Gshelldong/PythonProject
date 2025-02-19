import random
import tkinter


class RandomBall():
    """
    定义球的运动
    """

    def __init__(self, canvas, scrnwidth, scrnheight):
        """
        canvas:画布，所有的内容都应该在画布绗棉画出来，此处通过变量传入
        scrnwidth/scrnheigh:屏幕宽高
        """
        self.canvas = canvas

        # 球出现的位置要随机，此处位置表示球的圆
        # 心
        # xpos 代表x的坐标
        self.xpos = random.randint(10, int(scrnwidth) - 20)
        self.ypos = random.randint(10, int(scrnheight) - 20)

        # 定义球的运动速度
        # 模拟运动：不断的擦掉原来的，再重新绘制
        # 此处xvelocity模拟x轴方向运动
        self.xvelocity = random.randint(4, 20)
        self.yvelocity = random.randint(4, 20)

        # 定义屏幕的大小
        self.scrnwidth = scrnwidth
        self.scrnheight = scrnheight

        # 球的大小随机，使用半径表示
        self.radius = random.randint(4, 20)

        # 定义颜色 RGB：0-255  ；也可以使用单词来表示
        color = lambda: random.randint(0, 255)
        self.color = "#%02x%02x%02x" % (color(), color(), color())

    def create_ball(self):
        """
        用构造函数定义的变量值，在canvas上画一个球
        """
        # tkinter没有画圆形函数
        # 只有画椭圆的函数，画椭圆需要定义两个坐标，
        # 在一个长方形里面画一个椭圆只需要左上角和右下角的坐标就好
        x1 = self.xpos - self.radius
        y1 = self.ypos - self.radius

        x2 = self.xpos + self.radius
        y2 = self.ypos + self.radius
        self.item = self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)

    def move_ball(self):
        # 球移动的时候需要控制球的方向
        # 每次移动后，球都会有一个新坐标
        self.xpos += self.xvelocity
        self.ypos += self.yvelocity

        # 判断是否会撞墙
        if self.xpos + self.radius >= self.scrnwidth:
            # 撞到了右边墙
            self.xvelocity = -self.xvelocity

        if self.ypos + self.radius >= self.scrnheight:
            self.yvelocity = -self.yvelocity

        if self.ypos - self.radius <= 0:
            self.xvelocity = -self.xvelocity

        if self.ypos - self.radius <= 0:
            self.yvelocity = -self.yvelocity

        self.canvas.move(self.item, self.xvelocity, self.yvelocity)


class ScreenSaver():
    """
    定义屏保的类,可以被启动
    """
    # 如何装随机产生的球？
    balls = list()

    def __init__(self):
        # 每次启动球的数量随机
        self.num_balls = random.randint(6, 20)
        self.root = tkinter.Tk()
        # 取消边框
        self.root.overrideredirect(1)

        self.root.bind("<Motion>", self.but)
        self.root.bind("<Key>", self.myquit)

        # 得到屏幕大小规格
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()

        # 创建画布，包括画布的归属规格
        self.canvas = tkinter.Canvas(self.root, width=w, height=h)
        self.canvas.pack()

        # 在画布上面画球
        for i in range(self.num_balls):
            ball = RandomBall(self.canvas, scrnheight=h, scrnwidth=w)
            ball.create_ball()
            self.balls.append(ball)

        self.run_screen_saver()
        self.root.mainloop()

    def run_screen_saver(self):

        for ball in self.balls:
            ball.move_ball()

        # after是200毫秒后启动一个函数，需要启动的函数是第二个参数
        self.canvas.after(200, self.run_screen_saver)

    def myquit(self, e):
        # 此处只是利用了事件处理机制
        # 实际上并不关心事件的类型
        # 作业：
        # 此屏保程序扩展成，一旦捕获事件，则判断屏保不退出
        # 显示一个Button，Ｂｕｔｔｏｎ上显示事件类型，点击Ｂｕｔｔｏｎ后屏保
        # 才退出
        self.root.destroy()

    def but(self):
        self.balls.clear()
        self.but = tkinter.Button(self.canvas, text="点击退出", commamd =self.myquit)
        self.pack()


if __name__ == "__main__":
    ScreenSaver()
    

