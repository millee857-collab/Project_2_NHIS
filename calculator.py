from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import math

root = Tk()
root.title("Scientific Calculator")
root.geometry("400x500")

expression = ""

equation = StringVar()

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    global expression
    try:
        total = str(eval(expression))
        history.insert(END, expression + " = " + total + "\n")
        equation.set(total)
        expression = total
    except:
        equation.set("error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

# Scientific Functions
def sqrt():
    global expression
    result = str(math.sqrt(float(expression)))
    history.insert(END, "√" + expression + " = " + result + "\n")
    equation.set(result)
    expression = result

def square():
    global expression
    result = str(float(expression)**2)
    history.insert(END, expression + "² = " + result + "\n")
    equation.set(result)
    expression = result

def sine():
    global expression
    result = str(math.sin(math.radians(float(expression))))
    history.insert(END, "sin(" + expression + ") = " + result + "\n")
    equation.set(result)
    expression = result

def cosine():
    global expression
    result = str(math.cos(math.radians(float(expression))))
    history.insert(END, "cos(" + expression + ") = " + result + "\n")
    equation.set(result)
    expression = result

def tangent():
    global expression
    result = str(math.tan(math.radians(float(expression))))
    history.insert(END, "tan(" + expression + ") = " + result + "\n")
    equation.set(result)
    expression = result

def log():
    global expression
    result = str(math.log10(float(expression)))
    history.insert(END, "log(" + expression + ") = " + result + "\n")
    equation.set(result)
    expression = result

def ln():
    global expression
    result = str(math.log(float(expression)))
    history.insert(END, "ln(" + expression + ") = " + result + "\n")
    equation.set(result)
    expression = result

def factorial():
    global expression
    result = str(math.factorial(int(float(expression))))
    history.insert(END, expression + "! = " + result + "\n")
    equation.set(result)
    expression = result

# Modern Style
style = ttk.Style()
style.theme_use('clam')

entry = ttk.Entry(root, textvariable=equation, font=('Arial',18))
entry.grid(row=0, column=0, columnspan=5, ipadx=80, ipady=10)

# Buttons
ttk.Button(root,text='7',command=lambda: press(7)).grid(row=1,column=0)
ttk.Button(root,text='8',command=lambda: press(8)).grid(row=1,column=1)
ttk.Button(root,text='9',command=lambda: press(9)).grid(row=1,column=2)
ttk.Button(root,text='+',command=lambda: press("+")).grid(row=1,column=3)
ttk.Button(root,text='√',command=sqrt).grid(row=1,column=4)

ttk.Button(root,text='4',command=lambda: press(4)).grid(row=2,column=0)
ttk.Button(root,text='5',command=lambda: press(5)).grid(row=2,column=1)
ttk.Button(root,text='6',command=lambda: press(6)).grid(row=2,column=2)
ttk.Button(root,text='-',command=lambda: press("-")).grid(row=2,column=3)
ttk.Button(root,text='x²',command=square).grid(row=2,column=4)

ttk.Button(root,text='1',command=lambda: press(1)).grid(row=3,column=0)
ttk.Button(root,text='2',command=lambda: press(2)).grid(row=3,column=1)
ttk.Button(root,text='3',command=lambda: press(3)).grid(row=3,column=2)
ttk.Button(root,text='*',command=lambda: press("*")).grid(row=3,column=3)
ttk.Button(root,text='sin',command=sine).grid(row=3,column=4)

ttk.Button(root,text='0',command=lambda: press(0)).grid(row=4,column=0)
ttk.Button(root,text='C',command=clear).grid(row=4,column=1)
ttk.Button(root,text='=',command=equalpress).grid(row=4,column=2)
ttk.Button(root,text='/',command=lambda: press("/")).grid(row=4,column=3)
ttk.Button(root,text='cos',command=cosine).grid(row=4,column=4)

ttk.Button(root,text='tan',command=tangent).grid(row=5,column=0)
ttk.Button(root,text='log',command=log).grid(row=5,column=1)
ttk.Button(root,text='ln',command=ln).grid(row=5,column=2)
ttk.Button(root,text='x!',command=factorial).grid(row=5,column=3)

# History Box
history = ScrolledText(root, width=45, height=8)
history.grid(row=6,column=0,columnspan=5)

root.mainloop()