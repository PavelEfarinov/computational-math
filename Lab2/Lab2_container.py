from tkinter import *

from Lab2 import lab_functions
from Lab2.GuiHolder import GuiHolder
from Lab2.IntegralCalculator import IntegralCalculator


def btn_pressed():
    is_valid = True
    try:
        float(g.get_lower_bound())
        g.hide_lower_limit_error()
    except ValueError:
        g.display_lower_limit_error()
        is_valid = False
    try:
        float(g.get_upper_bound())
        g.hide_upper_limit_error()
    except ValueError:
        g.display_upper_limit_error()
        is_valid = False
    try:
        g.display_epsilon_error()
        if float(g.get_epsilon()) >= 1e-6 and abs(float(g.get_epsilon())) != float("inf"):
            g.hide_epsilon_error()
        else:
            raise ValueError
    except ValueError:
        g.display_epsilon_error()
        is_valid = False
    if is_valid:
        try:
            ic = IntegralCalculator()
            ic.calculate_result(float(g.get_lower_bound()), float(g.get_upper_bound()), float(g.get_epsilon()),
                                solving_method, target_function, k_runge)
            g.set_result_text(ic.get_result_string())
            g.display_plot(float(g.get_lower_bound()), float(g.get_upper_bound()), ic.get_min_y(), ic.get_max_y(),
                           int(ic.get_result_perts_number()),
                           target_function, solving_method)
        except ValueError:
            g.set_result_text("Integration limits should be in D(f)\n and function should be continuous from a to b")
            g.clear_canvas()
        except ZeroDivisionError:
            g.set_result_text("There was division by zero in one of the points")
            g.clear_canvas()


def change_integrated_function():
    var = g.get_function_index()
    global target_function
    if var == 0:
        integrated_function = lab_functions.function_1
    elif var == 1:
        integrated_function = lab_functions.function_2
    elif var == 2:
        integrated_function = lab_functions.function_3
    else:
        integrated_function = lab_functions.function_4
    print("Function", g.get_function_index())


def change_integration_method():
    var = g.get_method_index()
    global solving_method
    if var == 0:
        integration_method = lab_functions.calcLeft
        k_runge = 1
    elif var == 1:
        integration_method = lab_functions.calcMiddle
        k_runge = 2
    else:
        integration_method = lab_functions.calcRight
        k_runge = 1
    print("Method", g.get_method_index())


main_window = Tk(className="Computational math")
main_window.geometry("730x300")
g = GuiHolder(main_window, btn_pressed, change_integrated_function, change_integration_method)
g.build_gui()
k_runge = 1
target_function = lab_functions.function_1
solving_method = lab_functions.calcLeft
main_window.mainloop()
