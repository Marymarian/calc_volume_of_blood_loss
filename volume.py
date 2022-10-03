from tkinter import *
from tkinter import messagebox 
from tkinter import Frame
import tkinter
from turtle import width
from textwrap import wrap
import math

#Главное окно.
window = Tk()
window.title('V - Калькулятор')
window.iconbitmap('icons/blood_drop2.ico')
mycolor = '#%02x%02x%02x' % (199, 199, 199)
color_v = '#%02x%02x%02x' % (200, 66, 69)
color_v_foc = '#%02x%02x%02x' % (236, 78, 83)
color_trhb = '#%02x%02x%02x' % (85, 170, 255)

# Парамет sticky  означает выравнивание. W, E,N,S — запад, восток, север, юг.
Label(window, text='m(кг.) =', font='Arial 14').grid(row=0, sticky=E)
Label(window, text='k1(мл.) =', font='Arial 14').grid(row=1, sticky=E)
Label(window, text='preHb(г/л.) =', font='Arial 14').grid(row=2, sticky=E)
Label(window, text='TrHb(г/л.) =', font='Arial 14').grid(row=3, sticky=E)
Label(window, text='postHb(г/л.) =', font='Arial 14').grid(row=4, sticky=E)
Label(window, text='preHct(%) =', font='Arial 14').grid(row=5, sticky=E)
Label(window, text='postHct(%) =', font='Arial 14').grid(row=6, sticky=E)

# Виджеты текстовых полей.
Entry_m = Entry(window, width=10, font='Arial 16', bg=mycolor)
Entry_k1 = Entry(window, width=10, font='Arial 16', bg=mycolor)
Entry_preHb = Entry(window, width=10, font='Arial 16', bg=mycolor)
Entry_TrHb = Entry(window, width=10, font='Arial 16', bg=mycolor)
Entry_postHb = Entry(window, width=10, font='Arial 16', bg=mycolor)
Entry_preHct = Entry(window, width=10, font='Arial 16', bg=mycolor)
Entry_postHct = Entry(window, width=10, font='Arial 16', bg=mycolor)
EntryRes = Entry(window, width=25, font='Arial 16', bg=mycolor)

# Выравнивание по сетке.
Entry_m.grid(row=0, column=1, sticky=E)
Entry_k1.grid(row=1, column=1, sticky=E)
Entry_preHb.grid(row=2, column=1, sticky=E)
Entry_TrHb.grid(row=3, column=1, sticky=E)
Entry_postHb.grid(row=4, column=1, sticky=E)
Entry_preHct.grid(row=5, column=1, sticky=E)
Entry_postHct.grid(row=6, column=1, sticky=E)

# columnspan — объединение ячеек по столбцам; rowspan — по строкам
EntryRes.grid(row=9, columnspan=2)

# Обработчик события для кнопки Рассчитать V.
def get_volume():
    m = int(Entry_m.get()) # Преобразуем текст из первого поля в число.
    k1 = int(Entry_k1.get()) 
    preHb = float(Entry_preHb.get()) 
    TrHb = float(Entry_TrHb.get()) 
    postHb = float(Entry_postHb.get()) 
    preHct = float(Entry_preHct.get()) 
    postHct = float(Entry_postHct.get()) 
    result_vol = str(int(m * k1 * ((preHb + TrHb - (postHb * math.sqrt(preHct / postHct))) / preHb))) # результат переведем в строку для дальнейшего вывода
    
    EntryRes.delete(0, END) # Оищаем текстовое поле полностью.
    EntryRes.insert(0, result_vol) # Вставляем результат в начало.

# обработчик для кнопки Рассчитать TrHb
def open_TrHb():
    TrHb_window = Toplevel(window)
    TrHb_window.title('TrHb')
    TrHb_window.iconbitmap('icons/transfusion2.ico')
    
    Label(TrHb_window, text='Vtr(мл.) =', font='Arial 14').grid(row=0, sticky=E)
    Label(TrHb_window, text='k2 =', font='Arial 14').grid(row=1, sticky=E)
    Label(TrHb_window, text='m(кг.) =', font='Arial 14').grid(row=2, sticky=E)
    Label(TrHb_window, text='k1(мл.) =', font='Arial 14').grid(row=3, sticky=E)
    Label(TrHb_window, text='preHct(%) =', font='Arial 14').grid(row=4, sticky=E)
    Label(TrHb_window, text='postHct(%) =', font='Arial 14').grid(row=5, sticky=E)

    Entry_Vtr = Entry(TrHb_window, width=10, font='Arial 16', bg=mycolor)
    Entry_k2 = Entry(TrHb_window, width=10, font='Arial 16', bg=mycolor)
    Entry_m = Entry(TrHb_window, width=10, font='Arial 16', bg=mycolor)
    Entry_k1 = Entry(TrHb_window, width=10, font='Arial 16', bg=mycolor)
    Entry_preHct = Entry(TrHb_window, width=10, font='Arial 16', bg=mycolor)
    Entry_postHct = Entry(TrHb_window, width=10, font='Arial 16', bg=mycolor)
    EntryResTrHb = Entry(TrHb_window, width=23, font='Arial 16', bg=mycolor)

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

        Vtr = float(Entry_Vtr.get())
        k2 = float(Entry_k2.get()) 
        m = int(Entry_m.get()) 
        k1 = int(Entry_k1.get()) 
        preHct = float(Entry_preHct.get()) 
        postHct = float(Entry_postHct.get()) 
        
        result_TrHb = round(((Vtr * KML) * AVER_HB * k2) / (m * KML * k1 * math.sqrt(preHct / postHct)), 1)

        EntryResTrHb.delete(0, END)
        EntryResTrHb.insert(0, result_TrHb)
        Entry_TrHb.insert(0, result_TrHb) # Вставляем результат в поле TrHb. 

    def clean_TrHb():
            Entry_Vtr.delete(0, END)
            Entry_k2.delete(0, END)
            Entry_m.delete(0, END)
            Entry_k1.delete(0, END)
            Entry_preHct.delete(0, END)
            Entry_postHct.delete(0, END)    

    but = Button(TrHb_window, text='Рассчитать TrHb', font='Arial 11 bold',  bg=color_trhb, command=get_TrHb)
    but.grid(row=9, column=0, sticky=W)

    but = Button(TrHb_window, text='Очистить', font='Arial 10', command=clean_TrHb)
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

def doc():
    doc_window = Toplevel(window)
    doc_window.title('Документация')
    doc_window.iconbitmap('icons/info_information.ico')
    doc_window.geometry('500x300')
    doc = (
        'V – объем интраоперационной кровопотери в мл.\n'
        'm – масса тела в кг.\n'
        'k1 – коэффициент, соответствующий правилу Гилчера.\n'
        '(у атлетичных мужчин на 1 килограмм веса приходится 75 мл крови,\n' 
        'у нормостеничных – 70 мл, у астеничных – 65 мл, у мужчин с ожирением – 60 мл.\n' 
        'У женщин используются несколько другие данные:\n'
        'при атлетичном телосложении – 70 мл на килограмм веса,\n'
        'при нормостеничном – 65 мл,\n'
        'у астеничных – 60 мл, у женщин с ожирением – 55 мл).\n'
        'preHb – концентрация гемоглобина в крови за 6-12 часов до операции в г/л.\n'
        'TrHb – гемоглобин перелитой трансфузионной среды.\n'
        'postHb – концентрация гемоглобина в крови через 24 часа после операции в г/л.\n'
        'Vtr – объем трансфузии в л.\n'
        'k2 – гематокрит трансфузионной среды.\n'
        '(У эритроцитарной массы гематокрит составляет 0,7,n' 
        'у эритроцитарной взвеси – 0,6, размороженные отмытые эритроциты – 0,5).\n'
        'preHct – гематокрит крови за 6-12 часов до операции в %.\n'
        'postHct – гематокрит крови через 24 часа после операции в %.\n'
    )
    Message(doc_window, text=doc).grid(row=0, sticky=W)
    doc_window.mainloop()

# Кнопки главного окна.
but = Button(window, text='Рассчитать V (мл.)', font='Arial 11 bold', bg=color_v, command=get_volume)
but.grid(row=10, column=0, sticky=W)

but = Button(window, text='Рассчитать TrHb', font='Arial 10 bold', bg=color_trhb, command=open_TrHb)
but.grid(row=3, column=2, sticky=W)

but = Button(window, text='Очистить', font='Arial 10', command=clean)
but.grid(row=10, column=1, sticky=E)

but = Button(window, text='doc', font='Arial 10', command=doc)
but.grid(row=10, column=2, sticky=W)


window.mainloop()