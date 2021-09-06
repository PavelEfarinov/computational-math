from typing import List

from Lab3.FunctionWrapper import FunctionWrapper
from Lab3.UserExceptions import NoRootsException


class SystemSolver:
    def __init__(self):
        self.__result = None
        self.__result_iterations = None
        self.__result_error = None

    def get_determinant(self, a: List):
        return a[0][0] * a[1][1] - a[1][0] * a[0][1]

    def __solve_linear_iteration(self, a_matrix: List, b_matrix: List) -> List[float]:
        if self.get_determinant(a_matrix) == 0:
            raise NoRootsException("Bad approximation, this would not converge!")# + str(a_matrix) +str(b_matrix))
        x = a_matrix[1][1] * b_matrix[0] - a_matrix[0][1] * b_matrix[1]
        y = a_matrix[0][0] * b_matrix[1] - a_matrix[1][0] * b_matrix[0]
        x /= self.get_determinant(a_matrix)
        y /= self.get_determinant(a_matrix)
        return [x, y]

    def __calculate_jacobian(self, functions: List[FunctionWrapper], x: List[float]):
        return [[functions[0].df_dx(x[0]), functions[0].df_dy(x[1])],
                [functions[1].df_dx(x[0]), functions[1].df_dy(x[1])]]

    def __evaluate_functions(self, functions: List[FunctionWrapper], x: List[float]) -> List[float]:
        return [-functions[0].get_value(x[0], x[1]), -functions[1].get_value(x[0], x[1])]

    def solveSystem(self, x: float, y: float, functions: List, epsilon: float,
                    iteration_limit=1e6):
        i = 0
        delta_x = [1e6, 1e6]
        x_k = [x, y]
        while abs(max(abs(delta_x[0]), abs(delta_x[1]))) >= epsilon and i < iteration_limit:
            delta_x = self.__solve_linear_iteration(self.__calculate_jacobian(functions, x_k),
                                                    self.__evaluate_functions(functions, x_k))
            x_k[0] = x_k[0] + delta_x[0]
            x_k[1] = x_k[1] + delta_x[1]
            i += 1
        self.__result, self.__result_error, self.__result_iterations = x_k, delta_x, i

    def get_result_string(self):
        return "X of the root: " + str(self.__result[0]) + "\nY of the root: " + str(
            self.__result[1]) + "\n Error: " + str(
            self.__result_error[1] - self.__result_error[0]) + "\n In " + str(self.__result_iterations) + " iterations"

    def get_result(self):
        return self.__result

    def get_result_error(self):
        return self.__result_error
# print(solveSystem(-0.1, 0, [get_function_1(), get_function_2()], 0.000001))
