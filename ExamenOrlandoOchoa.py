import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mBox
from tkinter import scrolledtext
from tkinter import Menu

ventana=tk.Tk()
barra_menu=Menu(ventana)
ventana.title("")
ventana.configure(menu=barra_menu)
tabControl=ttk.Notebook(ventana)

tab1=ttk.Frame(tabControl)
tabControl.add(tab1,text='')
tabControl.pack(expand=1,fill="both")


preg1=ttk.Label(tab1,text='Menciona las razones de la caida del imperio Romano:')
preg1.grid(column=0,row=0)
pregu1=tk.StringVar()
res1=ttk.Entry(tab1,width=20,textvariable=pregu1)
res1.grid(column=1,row=0)

preg2=ttk.Label(tab1,text='Nombra a 1 emperador romano')
preg2.grid(column=0,row=2)
pregu2=tk.StringVar()
res2=ttk.Entry(tab1,width=20,textvariable=pregu2)
res2.grid(column=1,row=2)

opcion4=tk.IntVar()
opcion5=tk.IntVar()
opcion6=tk.IntVar()
preg3=ttk.Label(tab1,text='Emperadora Romana del siglo XV a.C.:')
preg3.grid(column=0,row=3)
radio1=ttk.Radiobutton(tab1,text='Cleopatra',variable=opcion4,value="Cleopatra")
radio1.grid(column=0,row=4,sticky=tk.W)
radio2=ttk.Radiobutton(tab1,text='Margarita de Calderon',variable=opcion4,value="Margarita de Calderon")
radio2.grid(column=1,row=4,sticky=tk.W)
radio3=ttk.Radiobutton(tab1,text='Athenea',variable=opcion4,value="Athenea")
radio3.grid(column=2,row=4,sticky=tk.W)

opcion7=tk.IntVar()
opcion8=tk.IntVar()
opcion9=tk.IntVar()
preg4=ttk.Label(tab1,text='Filosofo griego creador de "La Odisea" :')
preg4.grid(column=0,row=5)
radio4=ttk.Radiobutton(tab1,text='Aristoteles',variable=opcion5,value="Aristoteles")
radio4.grid(column=0,row=6,sticky=tk.W)
radio5=ttk.Radiobutton(tab1,text='Platon',variable=opcion5,value="Platon")
radio5.grid(column=1,row=6,sticky=tk.W)
radio6=ttk.Radiobutton(tab1,text='Edipo',variable=opcion5,value="Edipo")
radio6.grid(column=2,row=6,sticky=tk.W)
opcion10=tk.IntVar()
preg5=ttk.Label(tab1,text='Dios(es) de la mitologia griega mas poderoso(s)')
preg5.grid(column=0,row=8)
cb1=ttk.Checkbutton(tab1,text='Zeus',variable=opcion6)
cb2=ttk.Checkbutton(tab1,text='Morfeo',variable=opcion7)
cb3=ttk.Checkbutton(tab1,text='Hades',variable=opcion8)
cb4=ttk.Checkbutton(tab1,text='Athenea',variable=opcion9)
cb5=ttk.Checkbutton(tab1,text='Afrodita',variable=opcion10)

cb1.grid(column=0,row=9)
cb2.grid(column=1,row=9)
cb3.grid(column=2,row=9)
cb4.grid(column=3,row=9)
cb5.grid(column=4,row=9)

def fun4():
    ventana.quit()
    ventana.destroy()
    exit()



def fun6():
    i=2

    if(opcion4=="Athenea"):
        i=i+1
    if(opcion5=="Edipo"):
        i=i+1
    if(opcion6.get()!=0 and opcion8.get()!=0):
      i=i+1
    sum=i*20
    mBox.showinfo('Tu Calificacion =',sum)

   
    
    

    

    
  

cf=ttk.Button(tab1,text='Calificar',command=fun6)
cf.grid(column=4,row=11)
ventana.configure(menu=barra_menu)
menua=Menu(barra_menu,tearoff=0)

barra_menu.add_cascade(label="Ayuda",menu=menua)


menub=Menu(barra_menu,tearoff=0)
menub.add_command(label="Salir",command=fun4)
menub.add_command(label="Imprimir Respuestas",command=fun6)
barra_menu.add_cascade(label="Opciones",menu=menub)

ventana.mainloop()