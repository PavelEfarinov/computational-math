def get_left_good_point(integrated_function, x, delta):
    try:
        integrated_function(x - delta)
        return x - delta
    except:
        return x + delta


def get_right_good_point(integrated_function, x, delta):
    try:
        integrated_function(x + delta)
        return x + delta
    except:
        return x - delta


class IntegralCalculator:
    def __init__(self):
        self.__result = 0
        self.__result_error = 0
        self.__result_part_number = 0
        self.__min_y = float("inf")
        self.__max_y = -float("inf")

    def get_result_string(self):
        return "Integral sum: " + str(self.__result) + "\n Error: " + str(
            self.__result_error) + "\n Total parts: " + str(self.__result_part_number)

    def runge_value(self, current, old, k_runge):
        return (old - current) / (2 ** k_runge - 1)

    def calculate_result(self, lower, upper, epsilon, integration_method, integrated_function, k_runge):
        current = 0
        old = 0
        parts = 1
        while (parts <= 2 or abs((current - old) / (old + 1e-10)) > epsilon) and parts <= 10e6:
            old = current
            current = 0
            delta = (upper - lower) / parts
            current_x = lower
            for i in range(0, parts):
                approximated_x = integration_method(current_x, current_x + delta)
                try:
                    f_x = integrated_function(approximated_x)
                    if abs(f_x) == float("inf"):
                        raise ValueError
                except:
                    f_x = (integrated_function((get_left_good_point(integrated_function, approximated_x, delta))) +
                           integrated_function(get_right_good_point(integrated_function, approximated_x, delta)) / 2)
                if self.__min_y > f_x:
                    self.__min_y = f_x
                if self.__max_y < f_x:
                    self.__max_y = f_x
                current += f_x * delta
                current_x += delta
            parts *= 2
        parts /= 2
        self.__result_part_number = parts
        self.__result = current
        self.__result_error = self.runge_value(current, old)

    def get_result(self):
        return self.__result

    def get_result_error(self):
        return self.__result_error

    def get_result_perts_number(self):
        return self.__result_part_number

    def get_min_y(self):
        return self.__min_y

    def get_max_y(self):
        return self.__max_y
