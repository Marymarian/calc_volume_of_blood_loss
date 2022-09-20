from tkinter import *
from tkinter import messagebox 
from tkinter import Frame
import tkinter
from turtle import width
import math

#Главное окно.
window = Tk()
window.title('V - Калькулятор')
mycolor = '#%02x%02x%02x' % (199, 199, 199)
color_v = '#%02x%02x%02x' % (200, 66, 69)
color_trhb = '#%02x%02x%02x' % (85, 170, 255)
# первая метка в строке 0, столбце 0 (0 по умолчанию)
# парамет sticky  означает выравнивание. W, E,N,S — запад, восток, север, юг
Label(window, text='m =').grid(row=0, sticky=E)

# вторая метка в строке 1
Label(window, text='k1 =').grid(row=1, sticky=E)
Label(window, text='preHb =').grid(row=2, sticky=E)
Label(window, text='TrHb =').grid(row=3, sticky=E)
Label(window, text='postHb =').grid(row=4, sticky=E)
Label(window, text='preHct =').grid(row=5, sticky=E)
Label(window, text='postHct =').grid(row=6, sticky=E)


# создаем виджеты текстовых полей
Entry_m = Entry(window, width=10, font='Arial 16', bg=mycolor)
Entry_k1 = Entry(window, width=10, font='Arial 16', bg=mycolor)
Entry_preHb = Entry(window, width=10, font='Arial 16', bg=mycolor)
Entry_TrHb = Entry(window, width=10, font='Arial 16', bg=mycolor)
Entry_postHb = Entry(window, width=10, font='Arial 16', bg=mycolor)
Entry_preHct = Entry(window, width=10, font='Arial 16', bg=mycolor)
Entry_postHct = Entry(window, width=10, font='Arial 16', bg=mycolor)
EntryRes = Entry(window, width=20, font='Arial 16', bg=mycolor)

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
def get_volume():

    m = Entry_m.get() # берем текст из первого поля
    m = int(m) # преобразуем в число целого типа

    k1 = Entry_k1.get() 
    k1 = int(k1)
    
    preHb = Entry_preHb.get() 
    preHb = float(preHb)

    TrHb = Entry_TrHb.get() 
    TrHb = float(TrHb)

    postHb = Entry_postHb.get() 
    postHb = float(postHb)

    preHct = Entry_preHct.get() 
    preHct = float(preHct)
    
    postHct = Entry_postHct.get() 
    postHct = float(postHct)
    
    result_vol = str(int(m * k1 * ((preHb + TrHb - (postHb * math.sqrt(preHct / postHct))) / preHb))) # результат переведем в строку для дальнейшего вывода
    
    EntryRes.delete(0, END) # очищаем текстовое поле полностью
    EntryRes.insert(0, result_vol) # вставляем результат в начало 


# размещаем кнопку в строке 10 во втором столбце 
but = Button(window, text='   Рассчитать V   ', bg=color_v, command=get_volume)
but.grid(row=10, column=0, sticky=W)


# обработчик для кнопки Рассчитать TrHb
def open_TrHb():
    TrHb_window = Toplevel(window)
    TrHb_window.title('TrHb')
    
    Label(TrHb_window, text='Vtr =').grid(row=0, sticky=E)
    Label(TrHb_window, text='k2 =').grid(row=1, sticky=E)
    Label(TrHb_window, text='m =').grid(row=2, sticky=E)
    Label(TrHb_window, text='k1 =').grid(row=3, sticky=E)
    Label(TrHb_window, text='preHct =').grid(row=4, sticky=E)
    Label(TrHb_window, text='postHct =').grid(row=5, sticky=E)

    Entry_Vtr = Entry(TrHb_window, width=10, font='Arial 16', bg=mycolor)
    Entry_k2 = Entry(TrHb_window, width=10, font='Arial 16', bg=mycolor)
    Entry_m = Entry(TrHb_window, width=10, font='Arial 16', bg=mycolor)
    Entry_k1 = Entry(TrHb_window, width=10, font='Arial 16', bg=mycolor)
    Entry_preHct = Entry(TrHb_window, width=10, font='Arial 16', bg=mycolor)
    Entry_postHct = Entry(TrHb_window, width=10, font='Arial 16', bg=mycolor)
    EntryResTrHb = Entry(TrHb_window, width=20, font='Arial 16', bg=mycolor)

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
        Vtr = float(Vtr)

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

    def clean_TrHb():
            Entry_Vtr.delete(0, END)
            Entry_k2.delete(0, END)
            Entry_m.delete(0, END)
            Entry_k1.delete(0, END)
            Entry_preHct.delete(0, END)
            Entry_postHct.delete(0, END)    

    but = Button(TrHb_window, text='  Рассчитать TrHb  ',  bg=color_trhb, command=get_TrHb)
    but.grid(row=9, column=0, sticky=W)

    but = Button(TrHb_window, text='   Очистить   ', command=clean_TrHb)
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


but = Button(window, text='Рассчитать TrHb', bg=color_trhb, command=open_TrHb)
but.grid(row=3, column=2, sticky=W)

but = Button(window, text='  Очистить  ', command=clean)
but.grid(row=10, column=1, sticky=E)

but = Button(window, text='doc', command=open_TrHb)
but.grid(row=10, column=2, sticky=W)


window.mainloop()