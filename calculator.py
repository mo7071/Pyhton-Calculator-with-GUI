from tkinter import *


#----------------------
#main window
#----------------------

root = Tk()

root.title("Calculator")

root.geometry("400x400")

root.configure(bg="#202334")

root.resizable(False, False)


#--------------------------------
# Display Screen
#--------------------------------


Display = Entry(root,font=("Arial", 22, "bold"),
                bg="black",fg="white",bd=4,width=24,justify="right")

Display.pack(pady=5,padx=15,ipadx=5,ipady=8,fill="x")

#-------------------------
# Buttons Function  
#--------------------------

def show7():
    Display.insert(END, "7")


def show8():
    Display.insert(END, "8")


def show9():
    Display.insert(END, "9")  


def show_backspace():

    current = Display.get()

    Display.delete(0 , END)

    Display.insert(0 , current[:-1])  


#-------------------------------------------------------
# Buttons Function 
#------------------------------------------------------  

def show4():
    Display.insert(END, "4")   


def show5():
    Display.insert(END, "5") 


def show6():
    Display.insert(END, "6") 


def show1():
    Display.insert(END, "1")  


def show2():
    Display.insert(END, "2")


def show3():
    Display.insert(END, "3")         


def show0():
    Display.insert(END, "0")   


def show_double_zero():
    Display.insert(END, "00")        


#----------------------------------------------------------------
# Dot function 
#----------------------------------------------------------------
def show_dot():

    expression = Display.get()

    current_number = expression

    for op in ["+", "-","*","/"]:

        if op in expression:

            current_number = expression.split(op)[-1]


    if "." not in current_number:

        Display.insert(END , ".")        

#------------------------
# Clear 
#------------------------

def show_clear():
    Display.delete(0 , END)


#------------------------
# ALl Operators
#------------------------  

def insert_operator(op):
    expression = Display.get()

  
    if not expression:
        if op == "-":
            Display.insert(END, op)
        return

  
    if expression[-1] in ["+", "-", "*", "/"]:
        Display.delete(len(expression) - 1, END)

    Display.insert(END, op)


def show_add():
    insert_operator("+")


def show_sub():
    insert_operator("-")


def show_multi():
    insert_operator("*")


def show_division():
    insert_operator("/")


#----------------------------------------------------------------
# Percentage function 
#----------------------------------------------------------------
def show_percentage():

    try:

        expression = Display.get()

        for op in ["+", "-","*","/"]:

            if op in expression:

                num1, num2 = expression.split(op, 1)

                num1 = float(num1)

                num2 = float(num2.replace("%", ""))

                percentage = num1 * num2 / 100

                if op == "+":

                    result = num1 + percentage

                elif op == "-":

                    result = num1 - percentage

                elif op == "*":

                    result =  percentage

                elif op == "/":

                    result = num1 / (num2/ 100)     

                Display.delete(0 , END)

                Display.insert(END , result)   

                return 

    except Exception:

        Display.delete(0, END)

        Display.insert(END, "Error")                                


#----------------------------------------------------------------
# Equal function 
#----------------------------------------------------------------
def show_equal():
    try:
        result = Display.get()
        if not result:
            return
        
        answer = eval(result)
        
        Display.delete(0 , END)
        Display.insert(0 , answer)
        
    except ZeroDivisionError:
        Display.delete(0, END)
        Display.insert(0, "Can not divide by 0")
    
    except Exception:
        Display.delete(0, END)
        Display.insert(0, "Error")   
                
    
#------------------------------------------------------------------------------------------------
  #Buttons  7,8,9,⌫
#------------------------------------------------------------------------------------------------



btn_frame1 = Frame(root, bg="White")

btn_frame1.pack(pady=1)



btn7 = Button(btn_frame1,command=show7,text="7",font=("Arial" , 15, "bold"),
              bg="black",fg="white",bd=5,width=6,height=1)

btn7.pack(padx=2 , side="left")



btn8 = Button(btn_frame1,command=show8,text="8",font=("Arial" , 15, "bold"),
              bg="black",fg="white",bd=5,width=6,height=1)

btn8.pack(padx=2 , side="left")



btn9 = Button(btn_frame1,command=show9,text="9",font=("Arial" , 15, "bold"),
              bg="black",fg="white",bd=5,width=6,height=1)

btn9.pack(padx=2 , side="left")



btn_backspace = Button(btn_frame1, command=show_backspace, text="⌫",font=("Arial" , 15, "bold"),
              bg="#FFA500",fg="white",bd=5,width=6,height=1)

btn_backspace.pack(padx=2, side="left")


#------------------------------------------------------------------------------------------------
# Buttons 4,5,6 , +
#------------------------------------------------------------------------------------------------


btn_frame1 = Frame(root, bg="White")
btn_frame1.pack(pady=1)

btn4 = Button(btn_frame1,command=show4,text="4",font=("Arial" , 15, "bold"),
              bg="black",fg="white",bd=5,width=6,height=1)

btn4.pack(padx=2 , side="left")


btn5 = Button(btn_frame1, command=show5,text="5" ,font=("Arial" , 15, "bold"),
              bg="black",fg="white",bd=5,width=6,height=1)

btn5.pack(padx=2 , side="left")


btn6 = Button(btn_frame1, command=show6,text="6",font=("Arial" , 15, "bold"),
              bg="black",fg="white",bd=5,width=6,height=1)

btn6.pack(padx=2 , side="left")


btn_add = Button(btn_frame1,command=show_add,text="+",font=("Arial" , 15, "bold"),
              bg="#9400D3",fg="white",bd=5,width=6,height=1)

btn_add.pack(padx=2 , side="left")

#----------------------------------------------------------------------------------
# Buttons 1,2,3,-
#----------------------------------------------------------------------------------

btn_frame3 = Frame(root, bg="White")
btn_frame3.pack(pady=1)


btn1 = Button(btn_frame3, command=show1, text="1",font=("Arial" , 15, "bold"),
              bg="black",fg="white",bd=5,width=6,height=1)

btn1.pack(padx=2 , side="left")


btn2 = Button(btn_frame3,command=show2,text="2" ,font=("Arial" , 15, "bold"),
              bg="black",fg="white",bd=5,width=6,height=1)

btn2.pack(padx=2 , side="left")


btn3 = Button(btn_frame3,command=show3,text="3",font=("Arial" , 15, "bold"),
              bg="black",fg="white",bd=5,width=6,height=1)

btn3.pack(padx=2 , side="left")


btn_sub = Button(btn_frame3,command=show_sub, text="-" ,font=("Arial" , 15, "bold"),
              bg="#9400D3",fg="white",bd=5,width=6,height=1)

btn_sub.pack(padx=2 , side="left")

#------------------------------------------------------------------------------------------------
# Operators (0, ., *, ÷)
#------------------------------------------------------------------------------------------------

operator_frame4 = Frame(root , bg="white")
operator_frame4.pack(pady=1)


btn_zero = Button(operator_frame4,command=show0,text="0" ,font=("Arial" , 15, "bold"),
              bg="black",fg="white",bd=5,width=6,height=1)

btn_zero.pack(padx=2, side="left")


btn_decimal = Button(operator_frame4,command=show_dot,text="." ,font=("Arial" , 15, "bold"),
              bg="black",fg="white",bd=5,width=6,height=1)

btn_decimal.pack(padx=2, side="left")


btn_equal = Button(operator_frame4, command=show_equal,text="=" ,font=("Arial" , 15, "bold"),
              bg="black",fg="white",bd=5,width=6,height=1)

btn_equal.pack(padx=2, side="left")


btn_multi = Button(operator_frame4,command=show_multi,text="*" ,font=("Arial" , 15, "bold"),
              bg="#9400D3",fg="white",bd=5,width=6,height=1)

btn_multi.pack(padx=2, side="left")


#------------------------------------------------------------------------------------------------
 # Button (÷, 00, %, Clear(C) )
#------------------------------------------------------------------------------------------------

operator_frame5 = Frame(root , bg="white")
operator_frame5.pack(pady=1)


btn_division = Button(operator_frame5, command=show_division, text="÷" ,font=("Arial" , 15, "bold"),
              bg="black",fg="white",bd=5,width=6,height=1)

btn_division.pack(padx=2 , side="left")


btn_Double_zero = Button(operator_frame5,command=show_double_zero,text="00" ,font=("Arial" , 15, "bold"),
              bg="#FFD700",fg="white",bd=5,width=6,height=1)

btn_Double_zero.pack(padx=2, side="left")


btn_percentage = Button(operator_frame5,command=show_percentage,text="%",
                    font=("Arial" , 15, "bold"),bg="#A09933",fg="white",bd=5,width=6,height=1)

btn_percentage.pack(padx=2 , side="left")


btn_clear = Button(operator_frame5, command=show_clear,text="C" ,
                font=("Arial" , 15, "bold"),bg="#BDB76B", fg="white",bd=5,width=6,height=1)

btn_clear.pack(padx=2, side="bottom")


#===================================
#  Run Application
#===================================
root.mainloop()








