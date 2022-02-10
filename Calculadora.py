from tkinter import *
from constante import LOGO_ICON


# -------- funciones de la calculadora ------------
i=0

def ingreso_boton (num):
    global i
    display.insert (i, num)
    i+=1

# ***** limpiamos la pantalla de la calculadora ******
def clear ():
    display.delete (0, END)
    i=0

# ****** se realiza la operación matematica ********
def operation ():
    try:
        result=eval(display.get ())
        clear ()
        display.insert (0, result)
    except ZeroDivisionError as ad:
        clear ()
        display.insert (0, "Error")
    except SyntaxError as st:
        clear ()
        display.insert (0, "Error")

"""
    CONSTRUIMOS LA INTERFAZ DE LA CALCULADORA
"""
root=Tk ()
root.title ("Calculadora")
root.iconbitmap (LOGO_ICON)
root.resizable (False, False)
root.geometry ("260x325")

# --------- Creamos el contendor ---------
contenedor_calc=Frame (root)
contenedor_calc.pack ()

# ------ Pantalla de calculadora
display=Entry (contenedor_calc, font=("Forte 17"))
display.grid (row=0, column=0, padx=6, pady=4, columnspan=4)
display.config (background="black", fg="red")

# ---- Botones de la calculadora -----

borar=Button (contenedor_calc, text="AC", width=5, height=2, font=("Cambria 12"), command=lambda: clear ())
borar.grid (row=1, column=0, padx=2, pady=2)
borar.config (bg="brown")
parentesis1=Button (contenedor_calc, text="(", width=5, height=2, font=("Cambria 12"), command=lambda: ingreso_boton ("("))
parentesis1.grid (row=1, column=1, padx=2, pady=2)
parentesis1.config (bg="grey")
parentesis2=Button (contenedor_calc, text=")", width=5, height=2, font=("Cambria 12"), command=lambda: ingreso_boton (")"))
parentesis2.grid (row=1, column=2, padx=2, pady=2)
parentesis2.config (bg="grey")
div=Button (contenedor_calc, text="/", width=5, height=2, font=("Cambria 12"), command=lambda: ingreso_boton ("/"))
div.grid (row=1, column=3, padx=2, pady=2)
div.config (bg="grey")

boton9=Button (contenedor_calc, text="9", width=5, height=2, font=("Cambria 12 bold"), command=lambda: ingreso_boton ("9"))
boton9.grid (row=2, column=0, padx=2, pady=2)
boton9.config (background="#1976D2")
boton8=Button (contenedor_calc, text="8", width=5, height=2, font=("Cambria 12 bold"), command=lambda: ingreso_boton ("8"))
boton8.grid (row=2, column=1, padx=2, pady=2)
boton8.config (background="#1976D2")
boton7=Button (contenedor_calc, text="7", width=5, height=2, font=("Cambria 12 bold"), command=lambda: ingreso_boton ("7"))
boton7.grid (row=2, column=2, padx=2, pady=2)
boton7.config (background="#1976D2")
multi=Button (contenedor_calc, text="x", width=5, height=2, font=("Cambria 12"), command=lambda: ingreso_boton ("*"))
multi.grid (row=2, column=3, padx=2, pady=2)
multi.config (bg="grey")

boton6=Button (contenedor_calc, text="6", width=5, height=2, font=("Cambria 12 bold"), command=lambda: ingreso_boton ("6"))
boton6.grid (row=3, column=0, padx=2, pady=2)
boton6.config (background="#1976D2")
boton5=Button (contenedor_calc, text="5", width=5, height=2, font=("Cambria 12 bold"), command=lambda: ingreso_boton ("5"))
boton5.grid (row=3, column=1, padx=2, pady=2)
boton5.config (background="#1976D2")
boton4=Button (contenedor_calc, text="4", width=5, height=2, font=("Cambria 12 bold"), command=lambda: ingreso_boton ("4"))
boton4.grid (row=3, column=2, padx=2, pady=2)
boton4.config (background="#1976D2")
suma=Button (contenedor_calc, text="+", width=5, height=2, font=("Cambria 12"), command=lambda: ingreso_boton ("+"))
suma.grid (row=3, column=3, padx=2, pady=2)
suma.config (bg="grey")

boton3=Button (contenedor_calc, text="3", width=5, height=2, font=("Cambria 12 bold"), command=lambda: ingreso_boton ("3"))
boton3.grid (row=4, column=0, padx=2, pady=2)
boton3.config (background="#1976D2")
boton2=Button (contenedor_calc, text="2", width=5, height=2, font=("Cambria 12 bold"), command=lambda: ingreso_boton ("2"))
boton2.grid (row=4, column=1, padx=2, pady=2)
boton2.config (background="#1976D2")
boton1=Button (contenedor_calc, text="1", width=5, height=2, font=("Cambria 12 bold"), command=lambda: ingreso_boton ("1"))
boton1.grid (row=4, column=2, padx=2, pady=2)
boton1.config (background="#1976D2")
resta=Button (contenedor_calc, text="-", width=5, height=2, font=("Cambria 12"), command=lambda: ingreso_boton ("-"))
resta.grid (row=4, column=3, padx=2, pady=2)
resta.config (bg="grey")

boton0=Button (contenedor_calc, text="0", width=5, height=2, font=("Cambria 12 bold"), command=lambda: ingreso_boton ("0"))
boton0.grid (row=5, column=0, padx=2, pady=2)
boton0.config (background="#1976D2")
punto=Button (contenedor_calc, text=".", width=5, height=2, font=("Cambria 12"), command=lambda: ingreso_boton ("."))
punto.grid (row=5, column=1, padx=2, pady=2)
punto.config (bg="green")
igual=Button (contenedor_calc, text="=", width=12, height=2, font=("Cambria 12"), command=lambda: operation ())
igual.grid (row=5, column=2, columnspan=2, padx=2, pady=2, sticky=W+E)
igual.config (background="orange")

root.mainloop ()