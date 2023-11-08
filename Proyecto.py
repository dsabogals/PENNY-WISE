from tkinter import *
import math

def root(): #Ventana principal
    global root, root_active
    root=Tk() 
    root.title("Calculadora de ahorros")
    root.resizable(0,0)
    root.geometry("650x650")
    root.iconbitmap("logo.ico")
    root.config(bg="#F0F0F0")
    root_active=None #No hay ventana activa

    frame1 = Frame(root, bg="#F0F0F0").grid(row=0, column=0, sticky="n", padx=20, pady=30)
    logo=PhotoImage(file="logo.png")
    Label(frame1, image=logo, bg="#F0F0F0").grid(row=1, column=1, rowspan=2, pady=30)
    Label(frame1, text="PENNY-WISE", font=("Lato", 50), bg="#F0F0F0", fg="#000000").grid(row=1, column=2, pady=5, padx=10, sticky='s')
    Label(frame1, text="Calculadora de Ahorros", font=("Lato", 20), bg="#F0F0F0", fg="#000000").grid(row=2, column=2, pady=5, sticky='n')
    Button(frame1, text="Método 50/30/20", font=("Lato", 20), bg="#D4AF37", width=20, height=2, bd=4, command=root2).grid(row=3, column=1, columnspan=2, pady=30)
    Button(frame1, text="Método Harv Eker", font=("Lato", 20), bg="#D4AF37", width=20, height=2, bd=4, command=root3).grid(row=4, column=1, columnspan=2, pady=5)
    root.mainloop()

def root2():
    global root2, root_active, ingresos, meta
    if root_active:
        root_active.destroy()
    root2=Toplevel(root) #Crear una segunda ventana luego de la principal
    root2.title("Metodo 50/30/20")
    root2.resizable(0,0)
    root2.geometry("650x650")
    root2.iconbitmap("logo.ico")
    root2.config(bg="#F0F0F0")
    root_active=root2

    frame2=Frame(root2, width=650, height=300, bg="#F0F0F0")
    frame2.grid(row=0, column=0, sticky="n", padx=20, pady=5)
    Label(frame2, text="Metodo 50/30/20", font=("Lato", 40), bg="#F0F0F0").grid(row=1, column=1, pady=10, columnspan=2)
    Label(frame2, text="Este método consiste en dividir los gastos en tres categorías diferentes:", font=("Lato", 10), bg="#F0F0F0",wraplength=600).grid(row=2, column=1, pady=2, sticky='w', columnspan=2)
    Label(frame2, text="-Gastos básicos: Se llevan como máximo el 50%  los ingresos. En este grupo entra la alimentación, el transporte, la hipoteca, los gastos de la vivienda, etc.", font=("Lato", 10), bg="#F0F0F0", wraplength=600, justify='left').grid(row=3, column=1, pady=2, sticky='w', columnspan=2)
    Label(frame2, text="-Costes personales: Se emplea un 30% para el ocio o algún capricho.", font=("Lato", 10), bg="#F0F0F0", wraplength=600).grid(row=4, column=1, pady=2, sticky='w', columnspan=2)
    Label(frame2, text="-Ahorro: El 20% de los ingresos se guardaran. De esta manera, se convierte en un ahorro obligatorio, como si fuese un gasto más.", font=("Lato", 10), bg="#F0F0F0", wraplength=600, justify='left').grid(row=5, column=1, pady=2, sticky='w', columnspan=2)

    ingresos=Entry(frame2)
    ingresos.grid(row=6, column=2, padx=10, pady=10, sticky='n')
    Label(frame2, text="Ingresos mensuales:", font=("Lato", 15), bg="#F0F0F0").grid(row=6, column=1, padx=20, pady=10, sticky='n')
    meta=Entry(frame2)
    meta.grid(row=7, column=2, padx=10, pady=10, sticky='n')
    Label(frame2, text="Meta de ahorro:", font=("Lato", 15), bg="#F0F0F0").grid(row=7, column=1, padx=20, pady=5, sticky='n')
    Button(frame2, text="Calcular", font=("Lato", 15), bg="#D4AF37", width=10, height=1, bd=2, command=calculos1).grid(row=8, column=1, padx=20, pady=5, sticky='ne')
    Button(frame2, text="Volver", font=("Lato", 10), bg="#D4AF37", width=10, height=1, bd=2, command=volver).grid(row=8, column=2, padx=20, pady=5, sticky='w')
    if root2:
        root.withdraw() #La ventana se oculta infinitamente
    root2.mainloop()

def root3():
    global root3, root_active, ingresos2, meta2
    if root_active:
        root_active.destroy()
    root3 =Toplevel(root) #Crear una segunda ventana luego de la principal
    root3.title("Metodo Harv Eker")
    root3.resizable(0,0)
    root3.geometry("660x650")
    root3.iconbitmap("logo.ico")
    root3.config(bg="#F0F0F0")
    root_active=root3

    frame3=Frame(root3, width=650, height=300, bg="#F0F0F0")
    frame3.grid(row=0, column=0, sticky="n", padx=20, pady=5)
    Label(frame3, text="Metodo Harv Eker", font=("Lato", 40), bg="#F0F0F0").grid(row=1, column=1, pady=10, columnspan=2)
    Label(frame3, text="Este modelo también implica dividir los gastos en diferentes categorías y les otorga un porcentaje concreto a cada una de ellas. ", font=("Lato", 10), bg="#F0F0F0", wraplength=600, justify='left').grid(row=2, column=1, pady=2, sticky='w', columnspan=2)
    Label(frame3, text="-55 % destinado a necesidades básicas: casa, agua, alimentos, etc.", font=("Lato", 10), bg="#F0F0F0", wraplength=600).grid(row=3, column=1, pady=2, columnspan=2, sticky='w')
    Label(frame3, text="-10 % para formación: libros, material de oficina, cursos, exposiciones, etc.", font=("Lato", 10), bg="#F0F0F0", wraplength=600).grid(row=4, column=1, pady=2, sticky='w', columnspan=2)
    Label(frame3, text="-10 % para inversiones a largo plazo: gastos más grandes que harás en el futuro.", font=("Lato", 10), bg="#F0F0F0", wraplength=600).grid(row=5, column=1, pady=2, sticky='w', columnspan=2)
    Label(frame3, text="-10 % para invertir en ocio o algún capricho.", font=("Lato", 10), bg="#F0F0F0", wraplength=600).grid(row=6, column=1, pady=2, sticky='w', columnspan=2)
    Label(frame3, text="-5 % para donativos.", font=("Lato", 10), bg="#F0F0F0", wraplength=600).grid(row=7, column=1, pady=2, sticky='w', columnspan=2)
    Label(frame3, text="-10 % para ahorro: este dinero no se puede tocar para nada.", font=("Lato", 10), bg="#F0F0F0", wraplength=600).grid(row=8, column=1, pady=2, sticky='w', columnspan=2)

    ingresos2=Entry(frame3)
    ingresos2.grid(row=9, column=2, padx=10, pady=10, sticky='n')
    Label(frame3, text="Ingresos mensuales:", font=("Lato", 15), bg="#F0F0F0").grid(row=9, column=1, padx=20, pady=10, sticky='n')
    meta2=Entry(frame3)
    meta2.grid(row=10, column=2, padx=10, pady=10, sticky='n')
    Label(frame3, text="Meta de ahorro:", font=("Lato", 15), bg="#F0F0F0").grid(row=10, column=1, padx=20, pady=5, sticky='n')
    Button(frame3, text="Calcular", font=("Lato", 15), bg="#D4AF37", width=10, height=1, bd=2, command=calculos2).grid(row=11, column=1, padx=20, pady=5, sticky='ne')
    Button(frame3, text="Volver", font=("Lato", 10), bg="#D4AF37", width=10, height=1, bd=2, command=volver).grid(row=11, column=2, padx=20, pady=5, sticky='w')
    if root3:
        root.withdraw() #La ventana se oculta infinitamente
    root3.mainloop()

def volver(): 
    global root_active
    if root_active:
        root_active.destroy()  # Destruye la ventana activa actual
    root.deiconify()  # Devolver la ventana principal en la misma posición

def calculos1():
    global ingresos, meta # Hacer referencia a la variable global
    ingreso = float(ingresos.get())
    meta_ahorro = float(meta.get())
    gastos_basicos = ingreso * 0.50
    costes_personales = ingreso * 0.30
    ahorro = ingreso * 0.20
    meses = math.ceil(meta_ahorro/ahorro)
    años = meses // 12
    meses_restantes = meses % 12

    años_str = "1 año" if años == 1 else f"{años} años" #Cambiar el str en el label de año a años
    meses_str = "1 mes" if meses_restantes == 1 else f"{meses_restantes} meses"

    frame4=Frame(root2, width=650, height=300, bg="#F0F0F0")
    frame4.grid(row=1, column=0, sticky="n", padx=20, pady=5)
    Label(frame4, text="Gastos por categorias:", font=("Lato", 15), bg="#F0F0F0", wraplength=600).grid(row=1, column=1, pady=2, sticky='w', columnspan=2)
    Label(frame4, text=f"Gastos Básicos (50%): ${gastos_basicos:.2f}", font=("Lato", 12), bg="#F0F0F0").grid(row=2, column=1, pady=2, sticky='w', columnspan=2)
    Label(frame4, text=f"Costes Personales (30%): ${costes_personales:.2f}", font=("Lato", 12), bg="#F0F0F0").grid(row=3, column=1, pady=2, sticky='w', columnspan=2)
    Label(frame4, text=f"Ahorro (20%): ${ahorro:.2f}", font=("Lato", 12), bg="#F0F0F0").grid(row=4, column=1, pady=2, sticky='w', columnspan=2)
    Label(frame4, text="Tiempo en lograr la meta de ahorro:", font=("Lato", 15), bg="#F0F0F0", wraplength=600).grid(row=5, column=1, pady=2, sticky='e')
    Label(frame4, text=f"{años_str} y {meses_str}", font=("Lato", 12), bg="#F0F0F0").grid(row=5, column=2, pady=2, sticky='w')

def calculos2():
    global ingresos2, meta2 # Hacer referencia a la variable global
    ingreso = float(ingresos2.get())
    meta_ahorro = float(meta2.get())
    gastos_basicos = ingreso * 0.55
    ahorro = ingreso * 0.10
    formacion = ingreso * 0.10
    inversiones = ingreso * 0.10
    ocio = ingreso * 0.10
    donativos = ingreso * 0.05
    meses = math.ceil(meta_ahorro/ahorro)
    años = meses // 12
    meses_restantes = meses % 12

    años_str = "1 año" if años == 1 else f"{años} años" #Cambiar el str en el label de año a años
    meses_str = "1 mes" if meses_restantes == 1 else f"{meses_restantes} meses"

    frame5=Frame(root3, width=650, height=300, bg="#F0F0F0")
    frame5.grid(row=1, column=0, sticky="n", padx=20, pady=5)
    Label(frame5, text="Gastos por categorias:", font=("Lato", 15), bg="#F0F0F0", wraplength=600).grid(row=1, column=1, pady=2, columnspan=2, sticky='w')
    Label(frame5, text=f"Gastos Básicos (55%): ${gastos_basicos:.2f}", font=("Lato", 12), bg="#F0F0F0", wraplength=600).grid(row=2, column=1, pady=2, sticky='w')
    Label(frame5, text=f"Ahorro (10%): ${ahorro:.2f}", font=("Lato", 12), bg="#F0F0F0", wraplength=600).grid(row=2, column=2, pady=2, sticky='w')
    Label(frame5, text=f"Formación (10%): ${formacion:.2f}", font=("Lato", 12), bg="#F0F0F0", wraplength=600).grid(row=3, column=1, pady=2, sticky='w')
    Label(frame5, text=f"Inversiones a Largo Plazo (10%): ${inversiones:.2f}", font=("Lato", 12), bg="#F0F0F0", wraplength=600).grid(row=3, column=2, pady=2, sticky='w')
    Label(frame5, text=f"Ocio (10%): ${ocio:.2f}", font=("Lato", 12), bg="#F0F0F0", wraplength=600).grid(row=4, column=1, pady=2, sticky='w')
    Label(frame5, text=f"Donativos (5%): ${donativos:.2f}", font=("Lato", 12), bg="#F0F0F0", wraplength=600).grid(row=4, column=2, pady=2, sticky='w')
    Label(frame5, text="Tiempo en lograr la meta de ahorro:", font=("Lato", 15), bg="#F0F0F0", wraplength=600).grid(row=5, column=1, pady=2, sticky='e')
    Label(frame5, text=f"{años_str} y {meses_str}", font=("Lato", 12), bg="#F0F0F0").grid(row=5, column=2, pady=2, sticky='w')

root()


