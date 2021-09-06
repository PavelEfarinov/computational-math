class EquationSolver:
    def __init__(self):
        self.__result = 0
        self.__result_iterations = 0
        self.__result_error = 0

    def get_result_string(self):
        return "X of the root: " + str(self.__result) + "\n Error: " + str(
            self.__result_error) + "\n In " + str(self.__result_iterations) + " iterations"

    def calculate_result(self, lower, upper, epsilon, solving_method, target_function):
        self.__result, self.__result_error, self.__result_iterations = solving_method(lower, upper, target_function,
                                                                                      epsilon)

    def get_result(self):
        return self.__result

    def get_result_error(self):
        return self.__result_error