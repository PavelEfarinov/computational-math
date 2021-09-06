from tkinter import *

from Lab3.graphPlotter import GraphPlotter


class GuiHolder:
    def __init__(self, window, method, change_integrated_func, change_integration_meth):
        self.__define_messages()
        self.__define_results_frame(window)
        self.__define_radio_frame(window, change_integrated_func, change_integration_meth)
        self.__define_inputs_frame(window, method)
        self.graph_plotter = GraphPlotter(self.__canvas)

    def __define_messages(self):
        self.__from_text = StringVar()
        self.__from_text.set("From:")
        self.__to_text = StringVar()
        self.__to_text.set("To:")
        self.__epsilon_text = StringVar()
        self.__epsilon_text.set("epsilon:")
        self.__limit_error_text = " it should be a number"
        self.__epsilon_error_text = " it should be a positive real number"
        self.__result_text = StringVar()
        self.__result_text.set("")
        self.__lower_limit = StringVar()
        self.__upper_limit = StringVar()
        self.__epsilon = StringVar()
        self.__function_index = IntVar()
        self.__method_index = IntVar()

    def __define_inputs_frame(self, window, method):
        self.__frm_text_inputs = Frame(master=window, width=70, borderwidth=5, pady=5)
        self.__lbl_epsilon = Label(master=self.__frm_text_inputs, textvariable=self.__epsilon_text, anchor=W, pady=5)
        self.__ent_upper_limit = Entry(master=self.__frm_text_inputs, width=10, textvariable=self.__upper_limit)
        self.__lbl_upper_limit = Label(master=self.__frm_text_inputs, textvariable=self.__to_text, anchor=W, pady=5)
        self.__ent_lower_limit = Entry(master=self.__frm_text_inputs, width=10, textvariable=self.__lower_limit)
        self.__lbl_lower_limit = Label(master=self.__frm_text_inputs, textvariable=self.__from_text, anchor=W, pady=5)
        self.__ent_epsilon = Entry(master=self.__frm_text_inputs, width=10, textvariable=self.__epsilon)
        self.__btn_calculate = Button(master=self.__frm_text_inputs, text='Calculate and graph', width=17, height=3,
                                      borderwidth=3, command=method)

    def __define_radio_frame(self, window, change_integrated_func, change_integration_meth):
        self.__frm_radio = Frame(master=window, width=70, bg="yellow")
        self.__frm_function_radio = Frame(master=self.__frm_radio, width=70, bg="red")
        self.__lbl_functions = Label(master=self.__frm_function_radio, text="Choose your function:")
        self.__rbtn_function_1 = Radiobutton(master=self.__frm_function_radio, text="y = x * x - |x + 1| / (x + 1) - 1",
                                             variable=self.__function_index,
                                             value=0, command=change_integrated_func)
        self.__rbtn_function_2 = Radiobutton(master=self.__frm_function_radio, text="y = 1 / x",
                                             variable=self.__function_index,
                                             value=1, command=change_integrated_func)
        self.__rbtn_function_3 = Radiobutton(master=self.__frm_function_radio, text="y = ln(x)",
                                             variable=self.__function_index,
                                             value=2, command=change_integrated_func)
        self.__rbtn_function_4 = Radiobutton(master=self.__frm_function_radio, text="y = sin(x) / x",
                                             variable=self.__function_index,
                                             value=3, command=change_integrated_func)

        self.__frm_type_label = Frame(master=self.__frm_radio, width=70)
        self.__lbl_type = Label(master=self.__frm_type_label, text="Choose your integration method:", height=3,
                                anchor=S,
                                borderwidth=17)
        self.__frm_type_radio = Frame(master=self.__frm_radio, width=70, bg="grey50")
        self.__rbtn_type_1 = Radiobutton(master=self.__frm_type_radio, text="Left", variable=self.__method_index,
                                         value=0, anchor=N,
                                         command=change_integration_meth)
        self.__rbtn_type_2 = Radiobutton(master=self.__frm_type_radio, text="Middle", variable=self.__method_index,
                                         value=1,
                                         anchor=N,
                                         command=change_integration_meth)
        self.__rbtn_type_3 = Radiobutton(master=self.__frm_type_radio, text="Right", variable=self.__method_index,
                                         value=2, anchor=N,
                                         command=change_integration_meth)

    def __define_results_frame(self, window):
        self.__frm_results = Frame(master=window, width=250, bg="cyan")
        self.__canvas = Canvas(self.__frm_results, width=250, height=250, bg='white', highlightbackground="black",
                               highlightthickness=1)
        self.__lbl_result = Label(master=self.__frm_results, textvariable=self.__result_text)

    def build_result_frame(self):
        self.__frm_results.pack(fill=BOTH, side=LEFT, expand=True)

        self.__canvas.pack(fill=BOTH, side=TOP, expand=True)
        self.__lbl_result.pack(fill=BOTH, side=TOP, expand=True)

    def build_radio_frame(self):
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
        self.__rbtn_type_3.pack(fill=BOTH, side=LEFT, expand=True)

    def build_inputs_frame(self):
        self.__frm_text_inputs.pack(fill=BOTH, side=LEFT, expand=True)

        self.__lbl_lower_limit.pack(fill=BOTH, side=TOP)
        self.__ent_lower_limit.pack(fill=BOTH, side=TOP)

        self.__lbl_upper_limit.pack(fill=BOTH, side=TOP)
        self.__ent_upper_limit.pack(fill=BOTH, side=TOP)

        self.__lbl_epsilon.pack(fill=BOTH, side=TOP)
        self.__ent_epsilon.pack(fill=BOTH, side=TOP)

        self.__btn_calculate.pack(fill=BOTH, side=TOP, pady=35)

    def build_gui(self):
        self.build_result_frame()
        self.build_radio_frame()
        self.build_inputs_frame()

    def clear_canvas(self):
        self.graph_plotter.draw_web()

    def display_plot(self, lower, upper, min_y, max_y, parts_number, integrated_function, integration_method):
        self.graph_plotter.set_reference_points(lower, upper, min_y, max_y)
        self.graph_plotter.draw_web()
        self.graph_plotter.drawRectangles(parts_number, integrated_function, integration_method)
        self.graph_plotter.drawFunction(integrated_function)

    def display_lower_limit_error(self):
        self.__from_text.set("From: " + self.__limit_error_text)

    def display_upper_limit_error(self):
        self.__to_text.set("To: " + self.__limit_error_text)

    def display_epsilon_error(self):
        self.__epsilon_text.set("epsilon: " + self.__epsilon_error_text)

    def hide_epsilon_error(self):
        self.__epsilon_text.set("epsilon: ")

    def hide_lower_limit_error(self):
        self.__from_text.set("From: ")

    def hide_upper_limit_error(self):
        self.__to_text.set("To: ")

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

    def set_result_text(self, text):
        self.__result_text.set(text)
