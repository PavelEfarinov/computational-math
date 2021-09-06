from tkinter import *

from Lab3 import lab_functions
from Lab3.EquationSolver import EquationSolver
from Lab3.GuiHolder import GuiHolder
from Lab3.GuiMessages import GuiMessages
from Lab3.SystemSolver import SystemSolver
from Lab3.UserExceptions import SameFunctionException, NoRootsException, LimitSignException


def validate_inputs():
    is_valid = True
    try:
        g.display_lower_limit_error()
        if abs(float(g.get_lower_bound())) >= 1e-9 and abs(float(g.get_lower_bound())) != float("inf") or float(
                g.get_lower_bound()) == 0:
            g.hide_lower_limit_error()
        else:
            raise ValueError
    except ValueError:
        g.display_lower_limit_error()
        is_valid = False
    try:
        g.display_upper_limit_error()
        if abs(float(g.get_upper_bound())) >= 1e-9 and abs(float(g.get_upper_bound())) != float("inf") or float(
                g.get_upper_bound()) == 0:
            g.hide_upper_limit_error()
        else:
            raise ValueError
    except ValueError:
        g.display_upper_limit_error()
        is_valid = False
    try:
        g.display_epsilon_error()
        if float(g.get_epsilon()) >= 1e-18 and abs(float(g.get_epsilon())) != float("inf"):
            g.hide_epsilon_error()
        else:
            raise ValueError
    except ValueError:
        g.display_epsilon_error()
        is_valid = False
    return is_valid


def get_function_by_name(function_name):
    if function_name == GuiMessages['system_functions_list'][0]:
        return lab_functions.get_function_circle()
    elif function_name == GuiMessages['system_functions_list'][1]:
        return lab_functions.get_function_parabolic()
    elif function_name == GuiMessages['system_functions_list'][2]:
        return lab_functions.get_function_sinusoid()
    elif function_name == GuiMessages['system_functions_list'][3]:
        return lab_functions.get_function_polynomial()


def display_functions(*args):
    g.clear_canvas()
    g.display_plot(get_function_by_name(g.get_function_names()[0]).get_y_from_x, 'green')
    g.display_plot(get_function_by_name(g.get_function_names()[1]).get_y_from_x, 'blue')


def get_functions():
    if g.get_function_names()[0] == g.get_function_names()[1]:
        raise SameFunctionException
    functions_list = []
    for i in range(2):
        if g.get_function_names()[i] == GuiMessages['system_functions_list'][0]:
            functions_list.append(lab_functions.get_function_circle())
        elif g.get_function_names()[i] == GuiMessages['system_functions_list'][1]:
            functions_list.append(lab_functions.get_function_parabolic())
        elif g.get_function_names()[i] == GuiMessages['system_functions_list'][2]:
            functions_list.append(lab_functions.get_function_sinusoid())
        elif g.get_function_names()[i] == GuiMessages['system_functions_list'][3]:
            functions_list.append(lab_functions.get_function_polynomial())
    return functions_list


def btn_pressed():
    if validate_inputs():
        g.clear_canvas()
        if g.is_solving_system():
            try:
                g.display_plot(get_functions()[0].get_y_from_x)
                g.display_plot(get_functions()[1].get_y_from_x, 'blue')
                system_solver = SystemSolver()
                system_solver.solveSystem(float(g.get_lower_bound()), float(g.get_upper_bound()), get_functions(),
                                          float(g.get_epsilon()))
                g.set_result_text(system_solver.get_result_string())
                g.display_root(system_solver.get_result()[0], system_solver.get_result()[1])
            except SameFunctionException as message:
                g.set_result_text(message)
            except NoRootsException as message:
                g.set_result_text(message)
            except LimitSignException as message:
                g.set_result_text(message)

        else:
            try:
                equation_solver = EquationSolver()
                g.display_plot(target_function.get_y_from_x)
                equation_solver.calculate_result(float(g.get_lower_bound()), float(g.get_upper_bound()),
                                                 float(g.get_epsilon()),
                                                 solving_method, target_function)
                g.set_result_text(equation_solver.get_result_string())
                g.display_root(equation_solver.get_result(), equation_solver.get_result_error())
            except NoRootsException as message:
                g.set_result_text(message)
            except LimitSignException as message:
                g.set_result_text(message)


def change_integrated_function():
    var = g.get_function_index()
    global target_function
    if var == 0:
        target_function = lab_functions.get_function_e()
    elif var == 1:
        target_function = lab_functions.get_function_parabolic()
    elif var == 2:
        target_function = lab_functions.get_function_sinusoid()
    else:
        target_function = lab_functions.get_function_polynomial()
    g.clear_canvas()
    g.display_plot(target_function.get_y_from_x)
    print("Function", g.get_function_index())


def change_integration_method():
    var = g.get_method_index()
    global solving_method
    if var == 0:
        solving_method = lab_functions.bisection_method
    elif var == 1:
        solving_method = lab_functions.secant_method
    print("Method", g.get_method_index())


main_window = Tk(className="Computational math")
main_window.geometry("1300x700")
target_function = lab_functions.get_function_e()
solving_method = lab_functions.bisection_method
g = GuiHolder(main_window, btn_pressed, change_integrated_function, change_integration_method, display_functions)
g.build_gui()
main_window.mainloop()

