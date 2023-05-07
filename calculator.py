from tkinter import *

num1 = 0
num2 = 0
sign = None


def clicked_button(num):
    display.insert(END, num)


def clear():
    display.delete(0, END)


def equal():
    global num1
    global num2
    num2 = display.get()
    display.delete(0, END)

    if sign == "+":
        total = float(num1) + float(num2)
    elif sign == "-":
        total = float(num1) - float(num2)
    elif sign == "*":
        total = float(num1) * float(num2)
    elif sign == "/":
        try:
            total = float(num1) / float(num2)
        except ZeroDivisionError:
            display.delete(0, END)
            display.insert(0, "Zero division error")

    if (total % 10) == 0:
        total = round(total, 0)
        display.insert(0, str(total))
        print(total)
    else:
        
        # print(total)
        display.insert(0, str(total))

    return


def add():
    global num1
    global sign
    sign = "+"
    num1 = display.get()
    display.delete(0, END)
    return num1


def minus():
    global num1
    global sign
    sign = "-"
    num1 = display.get()
    display.delete(0, END)
    return num1


def multi():
    global num1
    global sign
    sign = "*"
    num1 = display.get()
    display.delete(0, END)
    return num1


def divide():
    global num1
    global sign
    sign = "/"
    num1 = display.get()
    display.delete(0, END)
    return num1


window = Tk()
x = 6
y = 3
window.title('Calculator')


display = Entry(window, width=35, relief=SUNKEN)
display.grid(row=0, column=0, columnspan=5)

buttton1 = Button(
    window, text="1", width=x, height=y, command=lambda: clicked_button(1)
).grid(row=3, column=0)
buttton2 = Button(
    window, text="2", width=x, height=y, command=lambda: clicked_button(2)
).grid(row=3, column=1)
buttton3 = Button(
    window, text="3", width=x, height=y, command=lambda: clicked_button(3)
).grid(row=3, column=2)

buttton4 = Button(
    window, text="4", width=x, height=y, command=lambda: clicked_button(4)
).grid(row=2, column=0)
buttton5 = Button(
    window, text="5", width=x, height=y, command=lambda: clicked_button(5)
).grid(row=2, column=1)
buttton6 = Button(
    window, text="6", width=x, height=y, command=lambda: clicked_button(6)
).grid(row=2, column=2)

buttton7 = Button(
    window, text="7", width=x, height=y, command=lambda: clicked_button(7)
).grid(row=1, column=0)
buttton8 = Button(
    window, text="8", width=x, height=y, command=lambda: clicked_button(8)
).grid(row=1, column=1)
buttton9 = Button(
    window, text="9", width=x, height=y, command=lambda: clicked_button(9)
).grid(row=1, column=2)

buttton0 = Button(
    window, text="0", width=x, height=y, command=lambda: clicked_button(0)
).grid(row=4, column=0)
buttton_add = Button(window, text="+", width=x, height=y, command=add).grid(
    row=1, column=4
)
buttton_minus = Button(window, text="-", width=x, height=y, command=minus).grid(
    row=2, column=4
)
buttton_multi = Button(window, text="*", width=x, height=y, command=multi).grid(
    row=3, column=4
)
buttton_divide = Button(window, text="/", width=x, height=y, command=divide).grid(
    row=4, column=4
)
buttton_equal = Button(window, text="=", width=x, height=y, command=equal).grid(
    row=4, column=1
)
buttton_clear = Button(window, text="CE", width=x, height=y, command=clear).grid(
    row=4, column=2
)


window.mainloop()
