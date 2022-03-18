import tkinter as tk
from tkinter import ttk

class Kanal(tk.LabelFrame):
    def __init__(self, parent,*args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.Czcionka = ('Tahoma',12)
        self.Wynik = tk.StringVar()
        self.Nazwa = tk.StringVar()
        self.Aktywny = tk.BooleanVar()
        self.Opcja = tk.IntVar()
        self.PoleAktywny = tk.Checkbutton(self,variable=self.Aktywny).grid(row=0,column=0)
        self.PoleNazwa = tk.Entry(self,textvariable=self.Nazwa,font=self.Czcionka).grid(row=0,column=1)
        self.PoleOpcja = ttk.Combobox(self,values=[' ','min','max','min/max'],variable=self.Opcja,font=self.Czcionka,width=7).grid(row=0,column=2)
        tk.Entry(self, textvariable=self.Wynik, font=self.Czcionka,width=8).grid(row=0, column=3)
    def druk(self):
        #print(str(int(self.Aktywny.get()))+'-'+str(self.Nazwa.get()))
        print(self.PoleOpcja.current)

class App(tk.Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title('Analiza danych')
        self.geometry('500x300')
        def PDS():
            pass
        def AW():
            pass
        def AS():
            pass
        self.Belka = tk.Menu(self)
        self.Belka.add_command(label='Przetwarzanie danych surowych', command=PDS)
        self.Belka.add_command(label='Analiza wykresów', command=AW)
        self.Belka.add_command(label='Analiza statyczna', command=AS)
        self.Belka.add_command(label='Zamknij', command=self.quit)

        self.config(menu=self.Belka)
        Kanaly = []
        for i in range(5):
           Kanaly.append(Kanal(self))
        for e in Kanaly:
            e.grid()

        def Raport():
            for e in Kanaly:
                e.druk()
        tk.Button(self,text='Raport',command=Raport).grid()




if __name__ == '__main__':
    root = App()
    root.mainloop()
