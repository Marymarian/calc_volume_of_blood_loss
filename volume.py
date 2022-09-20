from tkinter import *
from tkinter import messagebox 
from tkinter import Frame
import tkinter
from turtle import width
import math

#Главное окно.
window = Tk()
window.title('V - Калькулятор')

# первая метка в строке 0, столбце 0 (0 по умолчанию)
# парамет sticky  означает выравнивание. W, E,N,S — запад, восток, север, юг
Label(window, text='Значение m = ').grid(row=0, sticky=E)

# вторая метка в строке 1
Label(window, text='Значение k1 = ').grid(row=1, sticky=E)
Label(window, text='Значение preHb = ').grid(row=2, sticky=E)
Label(window, text='Значение TrHb = ').grid(row=3, sticky=E)
Label(window, text='Значение postHb = ').grid(row=4, sticky=E)
Label(window, text='Значение preHct = ').grid(row=5, sticky=E)
Label(window, text='Значение postHct = ').grid(row=6, sticky=E)


# создаем виджеты текстовых полей
Entry_m = Entry(window, width=10, font='Arial 16')
Entry_k1 = Entry(window, width=10, font='Arial 16')
Entry_preHb = Entry(window, width=10, font='Arial 16')
Entry_TrHb = Entry(window, width=10, font='Arial 16')
Entry_postHb = Entry(window, width=10, font='Arial 16')
Entry_preHct = Entry(window, width=10, font='Arial 16')
Entry_postHct = Entry(window, width=10, font='Arial 16')
EntryRes = Entry(window, width=20, font='Arial 16')

# размещаем первые два поля справа от меток, второй столбец (отсчет от нуля)
Entry_m.grid(row=0, column=1, sticky=E)
Entry_k1.grid(row=1, column=1, sticky=E)
Entry_preHb.grid(row=2, column=1, sticky=E)
Entry_TrHb.grid(row=3, column=1, sticky=E)
Entry_postHb.grid(row=4, column=1, sticky=E)
Entry_preHct.grid(row=5, column=1, sticky=E)
Entry_postHct.grid(row=6, column=1, sticky=E)

# третье текстовое поле ввода занимает всю ширину строки 2
# columnspan — объединение ячеек по столбцам; rowspan — по строкам
EntryRes.grid(row=9, columnspan=2)

# обработчик события для кнопки Рассчитать V
def proizv():
    KML: float = 0.001 

    m = Entry_m.get() # берем текст из первого поля
    m = int(m) # преобразуем в число целого типа

    k1 = Entry_k1.get() 
    k1 = int(k1)
    
    preHb = Entry_preHb.get() 
    preHb = float(preHb)

    TrHb = Entry_TrHb.get() 
    TrHb = float(TrHb) # тут нужна проверка if Entry_TrHb.get() = "" or "0": TrHb = 0 else: TrHb = метод

    postHb = Entry_postHb.get() 
    postHb = float(postHb)

    preHct = Entry_preHct.get() 
    preHct = float(preHct)
    
    postHct = Entry_postHct.get() 
    postHct = float(postHct)

    result_hb = (postHb * math.sqrt(preHct / postHct)) / preHb # Получить дробь Hb
    result_vol = str(int(m * k1 * KML * preHb + TrHb - result_hb)) # результат переведем в строку для дальнейшего вывода
    
    EntryRes.delete(0, END) # очищаем текстовое поле полностью
    EntryRes.insert(0, result_vol) # вставляем результат в начало 


# размещаем кнопку в строке 10 во втором столбце 
but = Button(window, text='Рассчитать V', command=proizv)
but.grid(row=10, column=0, sticky=W)


# обработчик для кнопки Рассчитать TrHb
def open_TrHb():
    TrHb_window = Toplevel(window)
    TrHb_window.title('TrHb')
    
    Label(TrHb_window, text='Значение Vtr = ').grid(row=0, sticky=E)
    Label(TrHb_window, text='Значение k2 = ').grid(row=1, sticky=E)
    Label(TrHb_window, text='Значение m = ').grid(row=2, sticky=E)
    Label(TrHb_window, text='Значение k1 = ').grid(row=3, sticky=E)
    Label(TrHb_window, text='Значение preHct = ').grid(row=4, sticky=E)
    Label(TrHb_window, text='Значение postHct = ').grid(row=5, sticky=E)

    Entry_Vtr = Entry(TrHb_window, width=10, font='Arial 16')
    Entry_k2 = Entry(TrHb_window, width=10, font='Arial 16')
    Entry_m = Entry(TrHb_window, width=10, font='Arial 16')
    Entry_k1 = Entry(TrHb_window, width=10, font='Arial 16')
    Entry_preHct = Entry(TrHb_window, width=10, font='Arial 16')
    Entry_postHct = Entry(TrHb_window, width=10, font='Arial 16')
    EntryResTrHb = Entry(TrHb_window, width=20, font='Arial 16')

    Entry_Vtr.grid(row=0, column=1, sticky=E)
    Entry_k2.grid(row=1, column=1, sticky=E)
    Entry_m.grid(row=2, column=1, sticky=E)
    Entry_k1.grid(row=3, column=1, sticky=E)
    Entry_preHct.grid(row=4, column=1, sticky=E)
    Entry_postHct.grid(row=5, column=1, sticky=E)

    EntryResTrHb.grid(row=8, columnspan=2)

    def get_TrHb():
        KML: float = 0.001 
        AVER_HB: int = 340

        Vtr = Entry_Vtr.get()
        Vtr = int(Vtr)

        k2 = Entry_k2.get() 
        k2 = float(k2)
        
        m = Entry_m.get() 
        m = int(m)

        k1 = Entry_k1.get() 
        k1 = int(k1)

        preHct = Entry_preHct.get() 
        preHct = float(preHct)
        
        postHct = Entry_postHct.get() 
        postHct = float(postHct)
        
        result_TrHb = round((Vtr * AVER_HB * k2) / (m * KML * k1 * math.sqrt(preHct / postHct)), 1)

        EntryResTrHb.delete(0, END) # очищаем поле полностью
        EntryResTrHb.insert(0, result_TrHb) # вставляем результат в начало
        Entry_TrHb.insert(0, result_TrHb) # вставляем результат в поле TrHb 

    but = Button(TrHb_window, text='Рассчитать TrHb', command=get_TrHb)
    but.grid(row=9, column=0, sticky=W)

    but = Button(TrHb_window, text='Очистить')
    but.grid(row=9, column=1, sticky=E)

    TrHb_window.mainloop()

def clean():
    Entry_m.delete(0, END)
    Entry_k1.delete(0, END)
    Entry_preHb.delete(0, END)
    Entry_TrHb.delete(0, END)
    Entry_postHb.delete(0, END)
    Entry_preHct.delete(0, END)
    Entry_postHct.delete(0, END)


but = Button(window, text='Рассчитать TrHb', command=open_TrHb)
but.grid(row=3, column=2, sticky=W)

but = Button(window, text='Очистить', command=clean)
but.grid(row=10, column=1, sticky=E)


window.mainloop()