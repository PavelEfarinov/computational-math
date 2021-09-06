class GraphPlotter:
    def __init__(self, canvas):
        self.canvas = canvas
        self.min_x = -10
        self.max_x = 10
        self.min_y = -10
        self.max_y = 10
        self.window_height = self.canvas.winfo_height()
        self.window_width = self.canvas.winfo_width()
        
        
    def draw_root(self, x, y):
        realX = self.x_to_pixels(x)
        realY = self.y_to_pixels(y)
        radius = 3
        self.canvas.create_oval(realX - radius, realY - radius, realX + radius, realY + radius, fill="yellow",
                                outline="red")

    def draw_point(self, x, y):
        realX = self.x_to_pixels(x)
        realY = self.y_to_pixels(y)
        radius = 1
        self.canvas.create_oval(realX - radius, realY - radius, realX + radius, realY + radius, fill="green",
                                outline="green")

    def clear_canvas(self, x=None, y=None):
        if x is None or y is None:
            self.window_height = self.canvas.winfo_height()
            self.window_width = self.canvas.winfo_width()
        else:
            self.window_height = y
            self.window_width = x
        self.draw_web()

    def draw_web(self):
        self.canvas.delete("all")
        for i in range(self.min_x, self.max_x, 1):
            self.canvas.create_line(self.x_to_pixels(i), 0, self.x_to_pixels(i), self.window_height,
                                    fill='grey70',
                                    width=1)
            self.canvas.create_text(self.x_to_pixels(i + 0.1), self.window_height - 10, text=str(i),
                                    fill="grey10")
            self.canvas.create_text(self.x_to_pixels(i + 0.1), 10, text=str(i), fill="grey10")
        for i in range(self.min_y, self.max_y, 1):
            self.canvas.create_line(0, self.y_to_pixels(i), self.window_width, self.y_to_pixels(i),
                                    fill='grey70',
                                    width=1)
            self.canvas.create_text(self.window_width - 10, self.y_to_pixels(i), text=str(i),
                                    fill="grey10")
            self.canvas.create_text(10, self.y_to_pixels(i), text=str(i),
                                    fill="grey10")
        self.draw_axis()

    def draw_axis(self):
        self.canvas.create_line(self.x_to_pixels(0), 0, self.x_to_pixels(0), self.window_height, fill='black',
                                width=2, arrow="first")
        self.canvas.create_line(0, self.y_to_pixels(0), self.window_width,
                                self.y_to_pixels(0), fill='black', width=2, arrow="last")
        self.canvas.create_text(self.x_to_pixels(9.2), self.y_to_pixels(-0.5), text="X")
        self.canvas.create_text(self.x_to_pixels(-0.5), self.y_to_pixels(9.2), text="Y")

    def drawFunction(self, function, color="green"):
        x = self.min_x
        x_1 = x
        y_1 = function(x)
        # TODO draw function with a bunch of lines
        points_in_graph = 600
        while x < self.max_x:
            y = function(x)
            if y != None:
                try:
                    for i in range(len(y)):
                        if y_1 == None:
                            self.canvas.create_line(self.x_to_pixels(x), self.y_to_pixels(y[0]), self.x_to_pixels(x),
                                                    self.y_to_pixels(y[1]), fill=color, width=3)
                        else:
                            self.canvas.create_line(self.x_to_pixels(x), self.y_to_pixels(y[i]), self.x_to_pixels(x_1),
                                                    self.y_to_pixels(y_1[i]), fill=color, width=3)
                except TypeError:
                    self.canvas.create_line(self.x_to_pixels(x), self.y_to_pixels(y), self.x_to_pixels(x_1),
                                            self.y_to_pixels(y_1), fill=color, width=3)
            x_1 = x
            y_1 = y
            x += (self.max_x - self.min_x) / points_in_graph

    def x_to_pixels(self, x):
        return (x - self.min_x) / (abs(
            self.max_x - self.min_x)) * self.window_width

    def y_to_pixels(self, y):
        return self.window_height - ((y - self.min_y) / (abs(
            self.max_y - self.min_y)) * self.window_height)
