import tkinter


height = 800
width = 800
road_width = width
road_height = 50
speed = 10


class Car:
    def __init__(self, canvas, width, height, x, y, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.canvas = canvas
        self.speed = speed
        self.car = canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill="salmon")

    def move_car(self):
        deltax = -self.speed
        self.canvas.move(self.car, deltax, 0)
        self.canvas.after(50, self.move_car)


root = tkinter.Tk()
root.title('Traffic Flow')
root.resizable(False, False)

canvas = tkinter.Canvas(root, bg="white", height=height, width=width)

canvas.create_rectangle(0,
                        (height-road_height)/2,
                        width,
                        (height-road_height)/2 + road_height,
                        fill='paleturquoise',
                        outline='paleturquoise')

car = Car(canvas, 70, 40, width, height/2-40/2, 20)
car.move_car()

canvas.pack()
root.mainloop()