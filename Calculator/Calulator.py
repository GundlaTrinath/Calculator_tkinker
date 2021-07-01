from tkinter import *

def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_Input.set(operator)

def btnClear():
    global operator
    operator=""
    text_Input.set("")

def btnClickeql():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ''

def btnBack():
    global operator
    lenth=len(operator)-1
    operator=operator[0:lenth]
    text_Input.set(operator)

cal=Tk()
cal.title('calculator')
operator=''
text_Input=StringVar()
txtDisplay=Entry(cal,font=('arial',15,'bold'),textvariable=text_Input,bd=30,insertwidth=4,bg='grey',justify='right').grid(columnspan=4)

btnlb=Button(cal,padx=13,bd=8,bg='grey',font=('arial',20,'bold'),text='(',command=lambda:btnClick('(')).grid(row=1,column=0)
btnrb=Button(cal,padx=13,bd=8,bg='grey',font=('arial',20,'bold'),text=')',command=lambda:btnClick(')')).grid(row=1,column=1)
cut=Button(cal,padx=7,bd=8,bg='red',font=('arial',20,'bold'),text='C',command=btnClear).grid(row=1,column=2)
back=Button(cal,padx=7,bd=8,bg='violet',font=('arial',20,'bold'),text='←',command=btnBack).grid(row=1,column=3)

btn7=Button(cal,padx=10,bd=8,bg='grey',font=('arial',20,'bold'),text='7',command=lambda:btnClick(7)).grid(row=2,column=0)
btn8=Button(cal,padx=10,bd=8,bg='grey',font=('arial',20,'bold'),text='8',command=lambda:btnClick(8)).grid(row=2,column=1)
btn9=Button(cal,padx=10,bd=8,bg='grey',font=('arial',20,'bold'),text='9',command=lambda:btnClick(9)).grid(row=2,column=2)
div=Button(cal,padx=10,bd=8,bg='blue',font=('arial',20,'bold'),text='÷',command=lambda:btnClick('÷')).grid(row=2,column=3)



btn4=Button(cal,padx=10,bd=8,bg='grey',font=('arial',20,'bold'),text='4',command=lambda:btnClick(4)).grid(row=3,column=0)
btn5=Button(cal,padx=10,bd=8,bg='grey',font=('arial',20,'bold'),text='5',command=lambda:btnClick(5)).grid(row=3,column=1)
btn6=Button(cal,padx=10,bd=8,bg='grey',font=('arial',20,'bold'),text='6',command=lambda:btnClick(6)).grid(row=3,column=2)
mul=Button(cal,padx=10,bd=8,bg='blue',font=('arial',20,'bold'),text='x',command=lambda:btnClick('*')).grid(row=3,column=3)


btn1=Button(cal,padx=10,bd=8,bg='grey',font=('arial',20,'bold'),text='1',command=lambda:btnClick(1)).grid(row=4,column=0)
btn2=Button(cal,padx=10,bd=8,bg='grey',font=('arial',20,'bold'),text='2',command=lambda:btnClick(2)).grid(row=4,column=1)
btn3=Button(cal,padx=10,bd=8,bg='grey',font=('arial',20,'bold'),text='3',command=lambda:btnClick(3)).grid(row=4,column=2)
sub=Button(cal,padx=13,bd=8,bg='blue',font=('arial',20,'bold'),text='-',command=lambda:btnClick('-')).grid(row=4,column=3)


btn0=Button(cal,padx=10,bd=8,bg='grey',font=('arial',20,'bold'),text='0',command=lambda:btnClick(0)).grid(row=5,column=0)
btndot=Button(cal,padx=13,bd=8,bg='grey',font=('arial',20,'bold'),text='.',command=lambda:btnClick('.')).grid(row=5,column=1)
btneql=Button(cal,padx=10,bd=8,bg='green',font=('arial',20,'bold'),text='=',command=btnClickeql).grid(row=5,column=2)
sum=Button(cal,padx=10,bd=8,bg='blue',font=('arial',20,'bold'),text='+',command=lambda:btnClick('+')).grid(row=5,column=3)



cal.mainloop()