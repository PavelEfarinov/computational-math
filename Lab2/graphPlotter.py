from Lab2.IntegralCalculator import get_left_good_point, get_right_good_point


class GraphPlotter:
    def __init__(self, canvas):
        self.canvas = canvas
        self.lower_limit = 0
        self.upper_limit = 0
        self.min_y = 0
        self.max_y = 0

    def set_reference_points(self, lower_limit, upper_limit, min_y, max_y):
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit

        if lower_limit > upper_limit:
            self.lower_limit = upper_limit
            self.upper_limit = lower_limit

        self.min_y = 0
        self.max_y = 0

        if min_y <= 0:
            self.min_y = min_y
        if max_y >= 0:
            self.max_y = max_y

    def draw_point(self, x, y):
        realX = self.x_to_pixels(x)
        realY = self.y_to_pixels(y)
        radius = 1
        self.canvas.create_oval(realX - radius, realY - radius, realX + radius, realY + radius, fill="green",
                                outline="green")

    def draw_web(self):
        self.canvas.delete("all")
        self.canvas.create_line(self.x_to_pixels(0), 0, self.x_to_pixels(0), self.canvas.winfo_height(), fill='black',
                                width=2)
        self.canvas.create_line(0, self.y_to_pixels(0), self.canvas.winfo_width(),
                                self.y_to_pixels(0), fill='black', width=2)

    def drawFunction(self, integrated_function):
        x = self.lower_limit
        points_in_line = 2000
        while x < self.upper_limit:
            try:
                self.draw_point(x, integrated_function(x))
            except:
                pass
            x += (self.upper_limit - self.lower_limit) / points_in_line
        try:
            self.canvas.create_line(self.x_to_pixels(self.lower_limit), self.y_to_pixels(0),
                                    self.x_to_pixels(self.lower_limit),
                                    self.y_to_pixels(integrated_function(self.lower_limit)), fill='red', width=3)
        except:
            pass
        try:
            self.canvas.create_line(self.x_to_pixels(self.upper_limit), self.y_to_pixels(0),
                                    self.x_to_pixels(self.upper_limit),
                                    self.y_to_pixels(integrated_function(self.upper_limit)), fill='red', width=3)
        except:
            pass

    def drawRectangles(self, parts_number, integrated_function, integration_method):
        current_x = self.lower_limit
        if parts_number > 10000:
            parts_number = 10000
        delta = (self.upper_limit - self.lower_limit) / parts_number
        for i in range(1, parts_number + 1):
            approximated_x = integration_method(current_x, current_x + delta)
            try:
                self.canvas.create_rectangle(self.x_to_pixels(current_x), self.y_to_pixels(0),
                                             self.x_to_pixels(current_x + delta),
                                             self.y_to_pixels(integrated_function(approximated_x)),
                                             fill='yellow', outline='blue', width=3, activedash=(5, 4))
            except:
                try:
                    self.canvas.create_rectangle(self.x_to_pixels(current_x), self.y_to_pixels(0),
                                                 self.x_to_pixels(current_x + delta),
                                                 self.y_to_pixels((integrated_function(
                                                     get_left_good_point(integrated_function, approximated_x,
                                                                         delta)) + integrated_function(
                                                     get_right_good_point(integrated_function, approximated_x,
                                                                          delta))) / 2),
                                                 fill='yellow', outline='blue', width=3, activedash=(5, 4))
                except:
                    pass
            current_x += delta

    def x_to_pixels(self, x):
        return (self.canvas.winfo_width() * 0.2) + (x - min(self.lower_limit, self.upper_limit)) / (abs(
            self.upper_limit - self.lower_limit) + 0.0000001) * self.canvas.winfo_width() * 0.65

    def y_to_pixels(self, y):
        return self.canvas.winfo_height() - (self.canvas.winfo_height() * 0.1 + (y - self.min_y) / (abs(
            self.max_y - self.min_y) + 0.0000001) * self.canvas.winfo_height() * 0.8)
