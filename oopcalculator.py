# Name: Benedict Waweru Mwangi
# Registration number: SCT211-0032/2022
# Welcome to my Github Repository!!!

import tkinter as tk

# This is a class named Calculator with an __init__ method that takes self and root as parameters
class Calculator:
    def __init__(self, root):
        self.equation = ""
        self.root = root
        self.equation_var = tk.StringVar()

        self.equation_label = tk.Label(root, textvariable = self.equation_var, font = ('consolas', 20), bg = "white", width = 24, height = 2)
        self.equation_label.pack()

        self.button_frame = tk.Frame(root)
        self.button_frame.pack()

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C' # Clear button
        ]

        row, col = 1, 0
        for button_text in buttons:
            command = lambda x = button_text: self.button_press(x)
            tk.Button(self.button_frame, text = button_text, height = 4, width = 9, font = 35, command = command).grid(row = row, column = col)
            col += 1
            if col > 3:
                col = 0
                row += 1
    
    # This method handles button presses
    def button_press(self, button):
        if button == '=':
            try:
                result = str(eval(self.equation))
                self.equation_var.set(result)
                self.equation = result
            except SyntaxError:
                self.equation_var.set("Syntax Error")
                self.equation = ''
            except ZeroDivisionError:
                self.equation_var.set("Math Error")
                self.equation = ''
        elif button == 'C':
            self.equation = ''
            self.equation_var.set('')
        else:
            self.equation += str(button)
            self.equation_var.set(self.equation)

    # This method clears the display and updates it
    def clear(self):
          self.equation = ""
          self.equation_var.set("")

# This block of code checks if the script is being run as the main program. If it is, it creates a Tk instance, sets the title and window properties and creates an instance of the Calculator class
if __name__ == '__main__':
    root = tk.Tk()
    root.title("Calculator Program")
    root.resizable(False, False)
    calc = Calculator(root)
    # This starts the Tkinter event loop and displays the Calculator GUI
    root.mainloop()