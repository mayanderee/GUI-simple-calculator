import tkinter as tk
from tkinter import *


class CalculatorApp:
    # constructor
    def __init__(self, root):
        """Initialize the main window and UI components."""
        self.root = root
        self.root.title("Calculator")
        self.create_widget()

    # create widgets function
    def create_widget(self):
        # Welcome banner
        banner = tk.Label(self.root, text="Welcome to the calculator", font=("Arial", 16))
        banner.grid(row=0, columnspan=3)

        # load image
        self.image = PhotoImage(file="image/canvas_img.png")

        # develop a canvas
        self.canvas = Canvas(self.root, width=300, height=250)
        self.canvas.create_image(150, 125, image=self.image, anchor="center")

        # Dropdown Menu
        self.operation_variable = tk.StringVar()
        self.operation_variable.set("Select Operations")
        operations = ["Addition", "Multiplication", "Division", "Subtraction"]
        self.operation_menu = tk.OptionMenu(self.root, self.operation_variable, *operations)
        self.canvas.create_window(130, 112, window=self.operation_menu)

        # input fields
        self.num1_entry = tk.Entry(self.root, width=5, font=("Arial", 14), bg="#34d9eb")
        self.canvas.create_window(194, 37, window=self.num1_entry)
        self.num2_entry = tk.Entry(self.root, width=5, font=("Arial", 14), bg="#34d9eb")
        self.canvas.create_window(194, 62, window=self.num2_entry)

        # Calculate button
        calc_button = tk.Button(self.root, text="Calculate", font=("Helvetica", 10, "bold"),
                                width=9, height=1, command=self.calculate_result, bg="#34c9eb")
        self.canvas.create_window(150,223, window=calc_button)

        # Exit button
        exit_button = tk.Button(self.root, text="Exit", font=("Helvetica", 10, "bold"),
                                width=3, height=1, command=self.root.quit)
        self.canvas.create_window(88,223, window=exit_button)

        # result display
        self.result_label = tk.Label(self.root, text="", font=("Arial", 14), bg="#34d9eb")
        self.canvas.create_window(100,70, window=self.result_label)
        self.canvas.grid(row=1, column=0, columnspan=3)

    def calculate_result(self):
        try:
            num1 = int(self.num1_entry.get())
            num2 = int(self.num2_entry.get())
            operation = self.operation_variable.get()

            if operation == "Addition":
                result = num1 + num2
            elif operation == "Multiplication":
                result = num1 * num2
            elif operation == "Division":
                result = num1 / num2 if num2 != 0 else "Error: Division by Zero"
            elif operation == "Subtraction":
                result = num1 - num2
            else:
                result = "Please select a valid operation"

            self.result_label.config(text=f"{result}")
        except ValueError:
            self.result_label.config(text="Error: Invalid input.")

        # Clear inputs for the next calculation
        self.num1_entry.delete(0, 'end')
        self.num2_entry.delete(0, 'end')
        self.operation_variable.set("Select Operation")





