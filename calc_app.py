from tkinter import *
import ast

root = Tk()
root.title('Calculator')

# get the use input and place it in the text field
i = 0


def get_variables(num):
    global i
    display.insert(i, num)
    i += 1


def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length


def factorial():
    """Calculates the factorial of the number entered."""
    whole_string = display.get()
    number = int(whole_string)
    fact = 1
    counter = number
    try:
        while counter > 0:
            fact = fact * counter
            counter -= 1
        clear_all()
        display.insert(0, fact)
    except Exception:
        clear_all()
        display.insert(0, "Error")


def calculate():
    entire_string = display.get()
    try:
        expr = ast.parse(entire_string).body[0]
        result = eval(compile(ast.Expression(expr.value), '<string>', "eval"))

        clear_all()
        display.insert(0, result)

    except Exception:
        clear_all()
        display.insert(0,"Error")


# Clear All Function
def clear_all():
    display.delete(0,END)


# Undo Function
def undo():
    entire_string = display.get()
    if len(entire_string)>0:
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0,new_string)
    else:
        clear_all()
        display.insert(0, "Error")


# adding the input field
display = Entry(root)
display.grid(row = 1, columnspan = 6, sticky = W+E)

# adding buttons to the calculator

Button(root, text = '1', command = lambda :get_variables(1)).grid(row=2, column=0)
Button(root, text = '2', command = lambda :get_variables(2)).grid(row=2, column=1)
Button(root, text = '3', command = lambda :get_variables(3)).grid(row=2, column=2)

Button(root, text = '4', command = lambda :get_variables(4)).grid(row=3, column=0)
Button(root, text = '5', command = lambda :get_variables(5)).grid(row=3, column=1)
Button(root, text = '6', command = lambda :get_variables(6)).grid(row=3, column=2)

Button(root, text = '7', command = lambda :get_variables(7)).grid(row=4, column=0)
Button(root, text = '8', command = lambda :get_variables(8)).grid(row=4, column=1)
Button(root, text = '9', command = lambda :get_variables(9)).grid(row=4, column=2)

# adding the other buttons to the calculator
Button(root, text = "AC", command = lambda :clear_all()).grid(row=5,column=0)
Button(root, text = "0", command = lambda :get_variables(0)).grid(row=5,column=1)
Button(root, text = "=", command = lambda :calculate()).grid(row=5,column=2)

Button(root, text = "+", command = lambda :get_operation("+")).grid(row=2,column=3)
Button(root, text = "-", command = lambda :get_operation("-")).grid(row=3,column=3)
Button(root, text = "*", command = lambda :get_operation("*")).grid(row=4,column=3)
Button(root, text = "/", command = lambda :get_operation("/")).grid(row=5,column=3)

# adding operations
Button(root, text = "pi", command = lambda :get_operation("*3.14")).grid(row=2,column=4)
Button(root, text = "%", command = lambda :get_operation("%")).grid(row=3,column=4)
Button(root, text = "(", command = lambda :get_operation("(")).grid(row=4,column=4)
Button(root, text = "exp", command = lambda :get_operation("**")).grid(row=5,column=4)

Button(root, text = "DEL", command = lambda :undo()).grid(row=2,column=5)
Button(root, text = "x!", command = lambda :factorial()).grid(row=3,column=5)
Button(root, text = ")", command = lambda :get_operation(")")).grid(row=4,column=5)
Button(root, text = "x^2", command = lambda :get_operation("**2")).grid(row=5,column=5)

root.mainloop()
