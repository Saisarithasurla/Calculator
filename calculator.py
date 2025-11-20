import tkinter as tk
from PIL import Image, ImageTk
import math
window=tk.Tk()
window.title("Calculator")
window.geometry("300x500")
window.configure(bg="black")
expression = ""
sqrt_mode=False
input_text = tk.StringVar()
window.rowconfigure(0, weight=1)
entry_box = tk.Entry(window, textvariable=input_text,
                     font=("Arial", 20, "bold"),
                     bg="black", fg="white",
                     justify="right",highlightthickness=2, highlightbackground="white",  highlightcolor="white",bd=0)
entry_box.pack(fill="both", padx=10, pady=10)
scientific_frame = tk.Frame(window, bg="black")
entry_box.grid(row=0, column=0, columnspan=4)
image=Image.open("calculator.png")
photo=ImageTk.PhotoImage(image)
window.iconphoto(False,photo)
percent_mode = False
percent_value = 0.0
pending_fun=None
angle_mode="deg"
trig_mode = None

def press(num):
    global expression, sqrt_mode, percent_mode, percent_value, trig_mode, angle_mode
    if num == "clear":
        expression = ""
        sqrt_mode = False
        percent_mode = False
        trig_mode = None
        input_text.set("")
        return
    if num == "backspace":
        if expression:
            expression = expression[:-1]
            if trig_mode:
                input_text.set(f"{trig_mode}({expression})")
            else:
                input_text.set(expression)
        return
    if num == "+/-":
        if expression:
            if expression.startswith("-"):
                expression = expression[1:]
            else:
                expression = "-" + expression
            input_text.set(expression)
        return
    if num == "x²":
        try:
            result = float(expression) ** 2
            expression = str(result)
            input_text.set(expression)
        except:
            input_text.set("Error")
            expression = ""
        return
    if num == "√":
        sqrt_mode = True
        expression = ""
        input_text.set("√")
        return
    if num == "%":
        if expression:
            percent_mode = True
            expression += "%"
            input_text.set(expression)
        return
    if num in ("sin", "cos", "tan"):
        trig_mode = num
        expression = ""
        input_text.set(f"{num}(")  
        return
    if num == "=":
        if sqrt_mode:
            try:
                result = float(expression) ** 0.5
                expression = str(result)
                input_text.set(expression)
            except:
                input_text.set("Error")
            sqrt_mode = False
            return
        if percent_mode:
            try:
                p = expression.split("%")
                result = float(p[0]) * float(p[1]) / 100
                expression = str(result)
                input_text.set(expression)
            except:
                input_text.set("Error")
            percent_mode = False
            return
        if trig_mode:
            try:
                val = float(expression)
                if angle_mode == "deg":
                    val = math.radians(val)

                if trig_mode == "sin":
                    result = math.sin(val)
                elif trig_mode == "cos":
                    result = math.cos(val)
                elif trig_mode == "tan":
                    result = math.tan(val)
                result = round(result, 13)
                expression = str(result)
                input_text.set(expression)

            except:
                input_text.set("Error")

            trig_mode = None
            return
        try:
            safe_expr = expression.replace("x", "*")
            result = str(eval(safe_expr))
            expression = result
            input_text.set(result)
        except:
            input_text.set("Error")
            expression = ""

        return
    expression += str(num)

    if trig_mode:
        input_text.set(f"{trig_mode}({expression})")
    elif sqrt_mode:
        input_text.set("√" + expression)
    else:
        input_text.set(expression)
def toggle_angle():
    global angle_mode
    angle_mode = "rad" if angle_mode == "deg" else "deg"
    angle_btn.config(text=angle_mode.upper())
def toggle_scientific():
    if scientific_frame.winfo_ismapped():
        scientific_frame.grid_remove()
    else:
        scientific_frame.grid(row=1, column=0, columnspan=4, pady=5)
def press_sci(func):
    press(func)
close_p = tk.Button(window, text=')', fg='white', bg='grey', command=lambda: press(")"), height=2, width=6,font=("Arial", 12, "bold"))
close_p.grid(row=7, column=1)
open_p = tk.Button(window, text='(', fg='white', bg='grey', command=lambda: press("("), height=2, width=6,font=("Arial", 12, "bold"))
open_p.grid(row=7, column=0)
clear = tk.Button(window, text='C', fg='white', bg='red', command=lambda: press("clear"), height=2, width=6,font=("Arial", 12, "bold"))
clear.grid(row=2, column=1)
back = tk.Button(window, text='⌫', fg='white', bg='orange', command=lambda: press("backspace"), height=2, width=6,font=("Arial", 12, "bold"))
back.grid(row=2, column=2)
btn1 = tk.Button(window, text='9', fg='white', bg='grey', command=lambda: press(9), height=2, width=6,font=("Arial", 12, "bold"))
btn1.grid(row=3, column=0)
btn2 =tk.Button(window, text='8', fg='white', bg='grey', command=lambda: press(8), height=2, width=6,font=("Arial", 12, "bold"))
btn2.grid(row=3, column=1)
btn3 =tk.Button(window, text='7', fg='white', bg='grey', command=lambda: press(7), height=2, width=6,font=("Arial", 12, "bold"))
btn3.grid(row=3, column=2)
btn4 = tk.Button(window, text='6', fg='white', bg='grey', command=lambda: press(6), height=2, width=6,font=("Arial", 12, "bold"))
btn4.grid(row=4, column=0)
btn5 = tk.Button(window, text='5', fg='white', bg='grey', command=lambda: press(5), height=2, width=6,font=("Arial", 12, "bold"))
btn5.grid(row=4, column=1)
btn6 = tk.Button(window, text='4', fg='white', bg='grey', command=lambda: press(4), height=2, width=6,font=("Arial", 12, "bold"))
btn6.grid(row=4, column=2)
btn7 = tk.Button(window, text='3', fg='white', bg='grey', command=lambda: press(3), height=2, width=6,font=("Arial", 12, "bold"))
btn7.grid(row=5, column=0)
btn8 = tk.Button(window, text='2', fg='white', bg='grey', command=lambda: press(2), height=2, width=6,font=("Arial", 12, "bold"))
btn8.grid(row=5, column=1)
btn9 = tk.Button(window, text='1', fg='white', bg='grey', command=lambda: press(1), height=2, width=6,font=("Arial", 12, "bold"))
btn9.grid(row=5, column=2)
btn0 = tk.Button(window, text='0', fg='white', bg='grey', command=lambda: press(0), height=2, width=6,font=("Arial", 12, "bold"))
btn0.grid(row=6, column=1)
btn11 = tk.Button(window, text='.', fg='white', bg='grey', command=lambda: press("."), height=2, width=6,font=("Arial", 12, "bold"))
btn11.grid(row=6, column=2)
btn12 = tk.Button(window, text='=', fg='white', bg='green', command=lambda: press("="), height=2, width=8,font=("Arial", 12, "bold"))
btn12.grid(row=6, column=3)
plus = tk.Button(window, text='+', fg='white', bg='orange', command=lambda: press("+"), height=2, width=8,font=("Arial", 12, "bold"))
plus.grid(row=5, column=3)
minus= tk.Button(window, text='-', fg='white', bg='orange', command=lambda: press("-"), height=2, width=8,font=("Arial", 12, "bold"))
minus.grid(row=4, column=3)
mul = tk.Button(window, text='x', fg='white', bg='orange', command=lambda: press("x"), height=2, width=8,font=("Arial", 12, "bold"))
mul.grid(row=3, column=3)
divide = tk.Button(window, text='/', fg='white', bg='orange', command=lambda: press("/"), height=2, width=8,font=("Arial", 12, "bold"))
divide.grid(row=2, column=3)
mod = tk.Button(window, text='%', fg='white', bg='grey', command=lambda: press("%"), height=2, width=8,font=("Arial", 12, "bold"))
mod.grid(row=7, column=3)
sign = tk.Button(window, text='+/-', fg='white', bg='grey', command=lambda: press("+/-"), height=2, width=6,font=("Arial", 12, "bold"))
sign.grid(row=6, column=0)
sqrt = tk.Button(window, text='√', fg='white', bg='grey', command=lambda: press("√"), height=2, width=6,font=("Arial", 12, "bold"))
sqrt.grid(row=7, column=2)
square = tk.Button(scientific_frame, text='x²', fg='white', bg='grey', command=lambda: press_sci("x²"), height=2, width=4,font=("Arial", 12, "bold"))
square.grid(row=0, column=4)
sin_btn = tk.Button(scientific_frame, text="sin", fg="white", bg="grey",command=lambda: press_sci("sin"), height=2, width=4,font=("Arial", 12, "bold"))
sin_btn.grid(row=0, column=0)
cos_btn = tk.Button(scientific_frame, text="cos", fg="white", bg="grey",command=lambda: press_sci("cos"), height=2, width=4,font=("Arial", 12, "bold"))
cos_btn.grid(row=0, column=1)
tan_btn = tk.Button(scientific_frame, text="tan", fg="white", bg="grey",command=lambda: press_sci("tan"), height=2, width=4,font=("Arial", 12, "bold"))
tan_btn.grid(row=0, column=2)
angle_btn = tk.Button(scientific_frame, text="DEG", fg="white", bg="grey",command=toggle_angle, height=2, width=4,font=("Arial", 12, "bold"))
angle_btn.grid(row=0, column=3)
sci_btn = tk.Button(window, text="Sci", fg="white", bg="orange",command=toggle_scientific, height=2, width=6,font=("Arial", 12, "bold"))
sci_btn.grid(row=2, column=0)
window.mainloop()
