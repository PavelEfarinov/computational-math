from tkinter import *

from Lab3.GuiMessages import GuiMessages
from Lab3.graphPlotter import GraphPlotter


class GuiHolder:
    def __init__(self, window, method, change_integrated_func, change_integration_method, menu_clicked):
        self.__window = window
        self.__on_function_change = change_integrated_func
        self.__on_method_change = change_integration_method
        self.__calculation_method = method
        self.__menu_clicked = menu_clicked
        self.__solving_system = StringVar()
        self.__define_messages()
        self.__define_results_frame(window)
        self.__define_optional_frame(window)
        self.__solving_system.set("False")
        self.__define_radio_frame(self.__optional_frame)
        self.__define_inputs_frame(self.__optional_frame)
        self.graph_plotter = GraphPlotter(self.__canvas)
        self.__canvas.bind("<Configure>", self.clear_canvas)

    def __define_messages(self):
        self.__from_text = StringVar()
        self.__to_text = StringVar()
        self.__epsilon_text = StringVar()
        self.__define_labels()
        self.__result_text = StringVar()
        self.__lower_limit = StringVar()
        self.__upper_limit = StringVar()
        self.__epsilon = StringVar()
        self.__function_index = IntVar()
        self.__method_index = IntVar()
        self.__first_function_name = StringVar()
        self.__second_function_name = StringVar()
        self.__first_function_name.set(GuiMessages['system_functions_list'][0])
        self.__second_function_name.set(GuiMessages['system_functions_list'][1])
        self.__first_function_name.trace("w", self.__menu_clicked)
        self.__second_function_name.trace("w", self.__menu_clicked)

    def __define_labels(self):
        if self.__solving_system.get() == 'False':
            self.__from_text.set(GuiMessages['Equation']['limits_from'])
            self.__to_text.set(GuiMessages['Equation']['limits_to'])
            self.__epsilon_text.set(GuiMessages['Equation']['epsilon'])
        else:
            self.__from_text.set(GuiMessages['System']['limits_from'])
            self.__to_text.set(GuiMessages['System']['limits_to'])
            self.__epsilon_text.set(GuiMessages['System']['epsilon'])

    def __define_optional_frame(self, window):
        self.__optional_frame = Frame(master=window, width=10)
        self.__chbtn_solving_system = Checkbutton(master=self.__optional_frame, text="Solve system?",
                                                  command=self.build_gui,
                                                  variable=self.__solving_system,
                                                  onvalue="True", offvalue="False")

    def __define_inputs_frame(self, master_frame):
        self.__upper_limit.set("")
        self.__lower_limit.set("")
        self.__epsilon.set("")
        self.__frm_text_inputs = Frame(master=master_frame, width=70, borderwidth=5, pady=5)
        self.__lbl_epsilon = Label(master=self.__frm_text_inputs, textvariable=self.__epsilon_text, anchor=W, pady=5)
        self.__ent_upper_limit = Entry(master=self.__frm_text_inputs, width=10, textvariable=self.__upper_limit)
        self.__lbl_upper_limit = Label(master=self.__frm_text_inputs, textvariable=self.__to_text, anchor=W, pady=5)
        self.__ent_lower_limit = Entry(master=self.__frm_text_inputs, width=10, textvariable=self.__lower_limit)
        self.__lbl_lower_limit = Label(master=self.__frm_text_inputs, textvariable=self.__from_text, anchor=W, pady=5)
        self.__ent_epsilon = Entry(master=self.__frm_text_inputs, width=10, textvariable=self.__epsilon)
        self.__btn_calculate = Button(master=self.__frm_text_inputs, text='Calculate and graph', width=17, height=3,
                                      borderwidth=3, command=self.__calculation_method)

    def __define_radio_frame(self, master_frame):
        self.__frm_radio = Frame(master=master_frame, width=70)
        self.__frm_function_radio = Frame(master=self.__frm_radio, width=70, bg="red")
        self.__lbl_functions = Label(master=self.__frm_function_radio, text="Choose your function:")
        self.__rbtn_function_1 = Radiobutton(master=self.__frm_function_radio, text=GuiMessages['functions_list'][0],
                                             variable=self.__function_index,
                                             value=0, command=self.__on_function_change)
        self.__rbtn_function_2 = Radiobutton(master=self.__frm_function_radio, text=GuiMessages['functions_list'][1],
                                             variable=self.__function_index,
                                             value=1, command=self.__on_function_change)
        self.__rbtn_function_3 = Radiobutton(master=self.__frm_function_radio, text=GuiMessages['functions_list'][2],
                                             variable=self.__function_index,
                                             value=2, command=self.__on_function_change)
        self.__rbtn_function_4 = Radiobutton(master=self.__frm_function_radio, text=GuiMessages['functions_list'][3],
                                             variable=self.__function_index,
                                             value=3, command=self.__on_function_change)

        self.__frm_type_label = Frame(master=self.__frm_radio, width=70)
        self.__lbl_type = Label(master=self.__frm_type_label, text="Choose your solving method:", height=3,
                                anchor=S,
                                borderwidth=17)
        self.__frm_type_radio = Frame(master=self.__frm_radio, width=70, bg="grey50")
        self.__rbtn_type_1 = Radiobutton(master=self.__frm_type_radio, text="Bisection",
                                         variable=self.__method_index,
                                         value=0, anchor=N,
                                         command=self.__on_method_change)
        self.__rbtn_type_2 = Radiobutton(master=self.__frm_type_radio, text="Secant", variable=self.__method_index,
                                         value=1,
                                         anchor=N,
                                         command=self.__on_method_change)

    def __define_lists_frame(self):
        self.__lbl_functions = Label(master=self.__frm_radio, text="Choose your function:")
        self.__opm_first_function = OptionMenu(self.__frm_radio, self.__first_function_name,
                                               *GuiMessages['system_functions_list'])
        self.__opm_first_function['width'] = 35
        self.__opm_second_function = OptionMenu(self.__frm_radio, self.__second_function_name,
                                                *GuiMessages['system_functions_list'])
        self.__opm_second_function['width'] = 35

    def __define_results_frame(self, window):
        self.__frm_results = Frame(master=window, width=250, bg="cyan")
        self.__canvas = Canvas(self.__frm_results, width=450, height=450, bg='white', highlightbackground="black",
                               highlightthickness=1)
        self.__lbl_result = Label(master=self.__frm_results, textvariable=self.__result_text, height=7)

    def build_result_frame(self):
        self.__frm_results.pack(fill=BOTH, side=LEFT, expand=True)

        self.__canvas.pack(fill=BOTH, side=TOP, expand=True)
        self.__lbl_result.pack(fill=BOTH, side=TOP, expand=False)

    def build_optional_frame(self):
        self.__optional_frame.pack(fill=BOTH, side=LEFT, expand=True)
        self.__chbtn_solving_system.pack(fill=BOTH, side=LEFT, expand=True)
        self.__frm_text_inputs.destroy()
        self.__define_inputs_frame(self.__optional_frame)
        self.__frm_radio.destroy()
        self.__define_radio_frame(self.__optional_frame)

        self.__frm_radio.pack_forget()
        self.__frm_type_radio.pack_forget()
        self.__frm_type_label.pack_forget()

        if self.__solving_system.get() == "False":
            self.build_eq_radio_frame()
        else:
            self.__define_lists_frame()
            self.build_system_lists_frame()
        self.build_inputs_frame()

    def build_eq_radio_frame(self):
        self.__frm_radio.pack(fill=BOTH, side=LEFT, expand=True)

        self.__frm_function_radio.pack(fill=BOTH, side=TOP, expand=True)

        self.__lbl_functions.pack(fill=BOTH, side=TOP, expand=True)

        self.__rbtn_function_1.pack(fill=BOTH, side=TOP, expand=True)
        self.__rbtn_function_2.pack(fill=BOTH, side=TOP, expand=True)
        self.__rbtn_function_3.pack(fill=BOTH, side=TOP, expand=True)
        self.__rbtn_function_4.pack(fill=BOTH, side=TOP, expand=True)

        self.__frm_type_label.pack(fill=X, side=TOP)
        self.__lbl_type.pack(fill=X, side=TOP, expand=True)

        self.__frm_type_radio.pack(fill=BOTH, side=TOP, expand=True)

        self.__rbtn_type_1.pack(fill=BOTH, side=LEFT, expand=True)
        self.__rbtn_type_2.pack(fill=BOTH, side=LEFT, expand=True)

    def build_inputs_frame(self):
        self.__frm_text_inputs.pack(fill=BOTH, side=LEFT, expand=True)

        self.__lbl_lower_limit.pack(fill=BOTH, side=TOP)
        self.__ent_lower_limit.pack(fill=BOTH, side=TOP)

        self.__lbl_upper_limit.pack(fill=BOTH, side=TOP)
        self.__ent_upper_limit.pack(fill=BOTH, side=TOP)

        self.__lbl_epsilon.pack(fill=BOTH, side=TOP)
        self.__ent_epsilon.pack(fill=BOTH, side=TOP)

        self.__btn_calculate.pack(fill=BOTH, side=TOP, pady=35)

    def build_system_lists_frame(self):
        self.__frm_radio.pack(fill=BOTH, side=LEFT)
        self.__lbl_functions.pack(fill=BOTH, side=TOP, pady=30, padx=20)
        self.__opm_first_function.pack(fill=BOTH, side=TOP, pady=25, padx=20)
        self.__opm_second_function.pack(fill=BOTH, side=TOP, pady=25, padx=20)

    def build_gui(self):
        self.__define_labels()
        self.build_result_frame()
        self.build_optional_frame()
        self.clear_canvas()

    def clear_canvas(self, event=None):
        if event is None:
            self.graph_plotter.clear_canvas()
        else:
            self.graph_plotter.clear_canvas(event.width, event.height)

    def display_plot(self, function, color='green'):
        self.graph_plotter.drawFunction(function, color)

    def display_root(self, x, y):
        self.graph_plotter.draw_root(x, y)

    def display_lower_limit_error(self):
        if self.__solving_system.get() == 'False':
            self.__from_text.set(GuiMessages['Equation']['limits_from'] + GuiMessages['Errors']['limit'])
        else:
            self.__from_text.set(GuiMessages['System']['limits_from'] + GuiMessages['Errors']['limit'])

    def display_upper_limit_error(self):
        if self.__solving_system.get() == 'False':
            self.__to_text.set(GuiMessages['Equation']['limits_to'] + GuiMessages['Errors']['limit'])
        else:
            self.__to_text.set(GuiMessages['System']['limits_to'] + GuiMessages['Errors']['limit'])

    def display_epsilon_error(self):
        if self.__solving_system.get() == 'False':
            self.__epsilon_text.set(GuiMessages['Equation']['epsilon'] + GuiMessages['Errors']['epsilon'])
        else:
            self.__epsilon_text.set(GuiMessages['System']['epsilon'] + GuiMessages['Errors']['epsilon'])

    def hide_epsilon_error(self):
        if self.__solving_system.get() == 'False':
            self.__epsilon_text.set(GuiMessages['Equation']['epsilon'])
        else:
            self.__epsilon_text.set(GuiMessages['System']['epsilon'])

    def hide_lower_limit_error(self):
        if self.__solving_system.get() == 'False':
            self.__from_text.set(GuiMessages['Equation']['limits_from'])
        else:
            self.__from_text.set(GuiMessages['System']['limits_from'])

    def hide_upper_limit_error(self):
        if self.__solving_system.get() == 'False':
            self.__to_text.set(GuiMessages['Equation']['limits_to'])
        else:
            self.__to_text.set(GuiMessages['System']['limits_to'])

    def get_lower_bound(self):
        return self.__lower_limit.get()

    def get_upper_bound(self):
        return self.__upper_limit.get()

    def get_epsilon(self):
        return self.__epsilon.get()

    def get_function_index(self):
        return self.__function_index.get()

    def get_method_index(self):
        return self.__method_index.get()

    def is_solving_system(self):
        return self.__solving_system.get() == "True"

    def set_result_text(self, text):
        self.__result_text.set(text)

    def get_function_names(self):
        return self.__first_function_name.get(), self.__second_function_name.get()
