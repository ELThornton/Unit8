# elena thornton
# 1/8/18
# calculator.py
# this program is a calculator

import tkinter

root = tkinter.Tk()


def press_seven():
    """
    this sets 7 as the value for seven_button
    :return: nothing
    """
    a = answer.get()
    a = a + "7"
    answer.set(a)


def press_eight():
    """
    this sets 8 as the value for eight_button
    :return: nothing
    """
    a = answer.get()
    a = a + "8"
    answer.set(a)


def press_nine():
    """
    this sets 9 as the value for nine_button
    :return: nothing
    """
    a = answer.get()
    a = a + "9"
    answer.set(a)


def press_six():
    """
    this sets 6 as the value for six_button
    :return: nothing
    """
    a = answer.get()
    a = a + "6"
    answer.set(a)


def press_five():
    """
    this sets 5 as the value for five_button
    :return: nothing
    """
    a = answer.get()
    a = a + "5"
    answer.set(a)


def press_four():
    """
    this sets 4 as the value for four_button
    :return: nothing
    """
    a = answer.get()
    a = a + "4"
    answer.set(a)


def press_three():
    """
    this sets 3 as the value for three_button
    :return: nothing
    """
    a = answer.get()
    a = a + "3"
    answer.set(a)


def press_two():
    """
    this sets 2 as the value for two_button
    :return: nothing
    """
    a = answer.get()
    a = a + "2"
    answer.set(a)


def press_one():
    """
    this sets 1 as the value for one_button
    :return:
    """
    a = answer.get()
    a = a + "1"
    answer.set(a)


def press_zero():
    """
    this sets 1 as the value for one_button
    :return: nothing
    """
    a = answer.get()
    a = a + "0"
    answer.set(a)


def press_square():
    """
    this sets **2 as the value for squared_button
    :return: noting
    """
    a = answer.get()
    a = a + "**2"
    answer.set(a)


def press_square_root():
    """
    this sets **.5 as the value for squrt_button
    :return:
    """
    a = answer.get()
    a = a + "**.5"
    answer.set(a)


def press_clear():
    """
    this sets nothing as the value for clear_button
    :return: nothing
    """
    answer.set("")


def press_plus():
    """
    this sets + as the value for plus_button
    :return: nothing
    """
    a = answer.get()
    a = a + "+"
    answer.set(a)


def press_divide():
    """
    this sets / as the value for divide_button
    :return: nothing
    """
    a = answer.get()
    a = a + "/"
    answer.set(a)


def press_minus():
    """
    this sets - as the value for minus_button
    :return: nothing
    """
    a = answer.get()
    a = a + "-"
    answer.set(a)


def press_multiply():
    """
    this sets * as the value for multiply_button
    :return: nothing
    """
    a = answer.get()
    a = a + "*"
    answer.set(a)


def press_equals():
    """
    this sets = as the value for equals_button
    :return: nothing
    """
    a = answer.get()
    a = eval(a)
    answer.set(a)


def press_decimal():
    """
    this sets . as the value for decimal_button
    :return:nothing
    """
    a = answer.get()
    a = a + "."
    answer.set(a)


def press_negative():
    """
    this sets - as the value for negative_button
    :return: nothing
    """
    a = answer.get()
    a = a + "-"
    answer.set(a)


answer = tkinter.StringVar()
answer_enter = tkinter.Entry(root, textvariable=answer)
answer_enter.grid(row=1, column=1, columnspan=4)

clear_button = tkinter.Button(root, text="C", command=press_clear)
clear_button.grid(row=2, column=1)

sqrt_button = tkinter.Button(root, text=" √")
sqrt_button.grid(row=2, column=2)

seven_button = tkinter.Button(root, text="7", command=press_seven)
seven_button.grid(row=3, column=1)

eight_button = tkinter.Button(root, text="8", command=press_eight)
eight_button.grid(row=3, column=2)

nine_button = tkinter.Button(root, text="9", command=press_nine)
nine_button.grid(row=3, column=3)

four_button = tkinter.Button(root, text="4", command=press_four)
four_button.grid(row=4, column=1)

five_button = tkinter.Button(root, text="5", command=press_five)
five_button.grid(row=4, column=2)

six_button = tkinter.Button(root, text="6", command=press_six)
six_button.grid(row=4, column=3)

one_button = tkinter.Button(root, text="1", command=press_one)
one_button.grid(row=5, column=1)

two_button = tkinter.Button(root, text="2", command=press_two)
two_button.grid(row=5, column=2)

three_button = tkinter.Button(root, text="3", command=press_three)
three_button.grid(row=5, column=3)

zero_button = tkinter.Button(root, text="0", command=press_zero)
zero_button.grid(row=6, column=1)

squrt_button = tkinter.Button(root, text="√ ", command=press_square_root)
squrt_button.grid(row=2, column=2)

squared_button = tkinter.Button(root, text="^", command=press_square)
squared_button.grid(row=2, column=3)

plus_button = tkinter.Button(root, text="+", command=press_plus)
plus_button.grid(row=5, column=4)

multiply_button = tkinter.Button(root, text="x", command=press_multiply)
multiply_button.grid(row=3, column=4)

divide_button = tkinter.Button(root, text="÷", command=press_divide)
divide_button.grid(row=2, column=4)

minus_button = tkinter.Button(root, text="-", command=press_minus)
minus_button.grid(row=4, column=4)

equals_button = tkinter.Button(root, text="=", command=press_equals)
equals_button.grid(row=6, column=4)

decimal_button = tkinter.Button(root, text=".", command=press_decimal)
decimal_button.grid(row=6, column=2)

negative_button = tkinter.Button(root, text="-", command=press_negative)
negative_button.grid(row=6, column=3)

root.mainloop()
