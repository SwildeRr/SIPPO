from tkinter import *
import sqlite3

class Krazha:
    bd = sqlite3.connect('База данных.db')
    cursor = bd.cursor()
    cursor.execute("SELECT * FROM Кража")
    otveti = []

    def Next(event):
        Delete()
        rd1.pack(anchor=CENTER)
        rd2.pack(anchor=CENTER)
        rd3.pack(anchor=CENTER)
        but7.pack(anchor=S, expand=1, pady=100)
        mass = Krazha.cursor.fetchone()
        lb_1["text"] = mass[0]
        rd1["text"] = mass[1]
        rd2["text"] = mass[2]
        rd3["text"] = mass[3]

    def Zapolnenie(event):
        Krazha.otveti.append(lang.get())
        mass = Krazha.cursor.fetchone()
        if (mass != None):
            lb_1["text"] = mass[0]
            rd1["text"] = mass[1]
            rd2["text"] = mass[2]
            rd3["text"] = mass[3]
        else:
            rd1.destroy()
            rd2.destroy()
            rd3.destroy()
            but7.destroy()
            lb_1["text"] = "По данным дела был проведен анализ и вынесен вердикт:"
            lb_2["text"] = Verdict1(Krazha.otveti)
            lb_2.pack(anchor=N)


def Verdict1(otveti):
    if (otveti[0]==1):
        return "Так как подозреваемый имеет возраст младше 14 лет, он не отвечает за свои деяния. \n Подозреваемого поставят на учет в комиссию по делам несовершеннолетних."
    elif (otveti[1]==1):
        return "Штраф в пятикратном размере от суммы похищенных денежных средств, но не менее 1000 рублей; \n либо арест продолжительностью до 15 суток; \nлибо работы обязательного характера на период до 50 часов."
    elif (otveti[1]==2):
        return "Штраф в пятикратном размере (но не менее 3000 рублей); \n арест от 10 до 15 суток; работы обязательного характера до 120 часов."
    elif (otveti[2]==1 or otveti[3]==1 or (otveti[3]==2 and otveti[4]==2)):
        return "Тюремное заключение продолжительностью от 3 до 5 лет или штраф до миллиона рублей, \n если подозреваемый совершил кражу не превышающую 1млн. рублей;\n если размер похищенных средств превысил один миллион рублей (особо крупный размер) \n тюремное заключение сроком до 10 лет."
    else: return "Штраф в пятикратном размере от суммы похищенных денежных средств; \n работы обязательного характера – их продолжительность составит до 360 часов; \n исправительные работы до одного года; ограничение свободы \n или принудительные работы продолжительностью до двух лет."

class Ubiystvo:

    bd = sqlite3.connect('База данных.db')
    cursor = bd.cursor()
    cursor.execute("SELECT * FROM Убийство")
    otveti = []

    def Next(event):
        Delete()
        rd1.pack(anchor=CENTER)
        rd2.pack(anchor=CENTER)
        rd3.pack(anchor=CENTER)
        but8.pack(anchor=S, expand=1, pady=100)
        mass = Ubiystvo.cursor.fetchone()
        lb_1["text"] = mass[0]
        rd1["text"] = mass[1]
        rd2["text"] = mass[2]
        rd3["text"] = mass[3]

    def Zapolnenie(event):
        Ubiystvo.otveti.append(lang.get())
        mass = Ubiystvo.cursor.fetchone()
        if (mass != None):
            lb_1["text"] = mass[0]
            rd1["text"] = mass[1]
            rd2["text"] = mass[2]
            rd3["text"] = mass[3]
        else:
            rd1.destroy()
            rd2.destroy()
            rd3.destroy()
            but8.destroy()
            lb_1["text"] = "По данным дела был проведен анализ и вынесен вердикт:"
            lb_2["text"] = Verdict2(Ubiystvo.otveti)
            lb_2.pack(anchor=N)

def Verdict2(otveti):
    if (otveti[0]==1):
        return "Так как подозреваемый имеет возраст младше 14 лет, он не отвечает за свои деяния. \n Подозреваемого поставят на учет в комиссию по делам несовершеннолетних."
    elif (otveti[1]==3) or (otveti[3]==2 and otveti[4]==2) or otveti[3]==3:
        return "Наказывается лишением свободы на срок от 20 лет; либо пожизненным лишением свободы."
    elif (otveti[4]==1):
        return "Если доказан факт самозащиты, либо выполнение служебного долга,\n подозреваемый признается невыновным."
    elif (otveti[4]==3):
        return "Наказывается лишением свободы до 6 лет; либо с ограничением свободы до 2х лет."
    else: return "Лишение свободы на срок от 6 до 15 лет с запретом на выезд из страны на срок до 6 лет."

class Narkotiki:

    bd = sqlite3.connect('База данных.db')
    cursor = bd.cursor()
    cursor.execute("SELECT * FROM Наркотики")
    otveti = []

    def Next(event):
        Delete()
        rd1.pack(anchor=CENTER)
        rd2.pack(anchor=CENTER)
        rd3.pack(anchor=CENTER)
        but9.pack(anchor=S, expand=1, pady=100)
        mass = Narkotiki.cursor.fetchone()
        lb_1["text"] = mass[0]
        rd1["text"] = mass[1]
        rd2["text"] = mass[2]
        rd3["text"] = mass[3]

    def Zapolnenie(event):
        Narkotiki.otveti.append(lang.get())
        mass = Narkotiki.cursor.fetchone()
        if (mass != None):
            lb_1["text"] = mass[0]
            rd1["text"] = mass[1]
            rd2["text"] = mass[2]
            rd3["text"] = mass[3]
        else:
            rd1.destroy()
            rd2.destroy()
            rd3.destroy()
            but9.destroy()
            lb_1["text"] = "По данным дела был проведен анализ и вынесен вердикт:"
            lb_2["text"] = Verdict3(Narkotiki.otveti)
            lb_2.pack(anchor=N)

def Verdict3(otveti):
    if (otveti[0]==1):
        return "Так как подозреваемый имеет возраст младше 14 лет, он не отвечает за свои деяния. \n Подозреваемого поставят на учет в комиссию по делам несовершеннолетних."
    elif ((otveti[1]==1 and otveti[3]==2) or (otveti[1]==2 and otveti[2]==1 and otveti[3]==2)):
        return "Количество изъятого вещества соответствует нормам законодательства\n и может применяться для собсвенного пользования."
    elif (otveti[3]==1):
        return "Наказывается лишением свободы от 4 до 8 лет."
    elif (otveti[3]==3):
        return "Если факт подброса будет доказан в судебном полядке,\n никаких мер пресечения за этим не последует."
    else: return "Лишение свободы на срок от 5 до 12 лет со штрафом в размере до 500000 рублей."

class Moshennichestvo:

    bd = sqlite3.connect('База данных.db')
    cursor = bd.cursor()
    cursor.execute("SELECT * FROM Мошенничество")
    otveti = []

    def Next(event):
        Delete()
        rd1.pack(anchor=CENTER)
        rd2.pack(anchor=CENTER)
        rd3.pack(anchor=CENTER)
        but10.pack(anchor=S, expand=1, pady=100)
        mass = Moshennichestvo.cursor.fetchone()
        lb_1["text"] = mass[0]
        rd1["text"] = mass[1]
        rd2["text"] = mass[2]
        rd3["text"] = mass[3]

    def Zapolnenie(event):
        Moshennichestvo.otveti.append(lang.get())
        mass = Moshennichestvo.cursor.fetchone()
        if (mass != None):
            lb_1["text"] = mass[0]
            rd1["text"] = mass[1]
            rd2["text"] = mass[2]
            rd3["text"] = mass[3]
        else:
            rd1.destroy()
            rd2.destroy()
            rd3.destroy()
            but10.destroy()
            lb_1["text"] = "По данным дела был проведен анализ и вынесен вердикт:"
            lb_2["text"] = Verdict4(Moshennichestvo.otveti)
            lb_2.pack(anchor=N)

def Verdict4(otveti):
    if (otveti[0]==1):
        return "Так как подозреваемый имеет возраст младше 14 лет, он не отвечает за свои деяния. \n Подозреваемого поставят на учет в комиссию по делам несовершеннолетних."
    elif (otveti[1]==3 and otveti[2]==2 and otveti[4]==1):
        return "Наказывается штрафом в размере до 120 тыс рублей, \n либо обязательными работами на срок до 360 часов."
    elif ((otveti[2]==1 and otveti[4]==1) or (otveti[2]==1 and otveti[4]==2)):
        return "Наказывается штрафом в размере до 300 тыc рублей, \n либо обязательными работами на срок до 480 часов."
    elif (otveti[1]==1 and (otveti[4]==2 or otveti[4]==3)):
        return "Наказывается штрафом в размере от ста тысяч до пятисот тысяч рублей; \n либо принудительными работами на срок до пяти лет \n с ограничением свободы на срок до двух лет или без такового."
    elif (otveti[2]==1 and otveti[4]==3):
        return "Наказывается лишением свободы на срок до десяти лет со штрафом в размере до одного миллиона рублей."
    else: return "Hаказывается штрафом в размере до трехсот тысяч рублей или в размере заработной платы \n или иного дохода осужденного за период до двух лет, либо обязательными работами \n на срок до четырехсот восьмидесяти часов, либо исправительными работами на срок до двух лет."

class Nasiliye:

    bd = sqlite3.connect('База данных.db')
    cursor = bd.cursor()
    cursor.execute("SELECT * FROM Насилие")
    otveti = []

    def Next(event):
        Delete()
        rd1.pack(anchor=CENTER)
        rd2.pack(anchor=CENTER)
        rd3.pack(anchor=CENTER)
        but11.pack(anchor=S, expand=1, pady=100)
        mass = Nasiliye.cursor.fetchone()
        lb_1["text"] = mass[0]
        rd1["text"] = mass[1]
        rd2["text"] = mass[2]
        rd3["text"] = mass[3]

    def Zapolnenie(event):
        Nasiliye.otveti.append(lang.get())
        mass = Nasiliye.cursor.fetchone()
        if (mass != None):
            lb_1["text"] = mass[0]
            rd1["text"] = mass[1]
            rd2["text"] = mass[2]
            rd3["text"] = mass[3]
        else:
            rd1.destroy()
            rd2.destroy()
            rd3.destroy()
            but11.destroy()
            lb_1["text"] = "По данным дела был проведен анализ и вынесен вердикт:"
            lb_2["text"] = Verdict5(Nasiliye.otveti)
            lb_2.pack(anchor=N)

def Verdict5(otveti):
    if (otveti[0]==1):
        return "Так как подозреваемый имеет возраст младше 14 лет, он не отвечает за свои деяния. \n Подозреваемого поставят на учет в комиссию по делам несовершеннолетних."
    elif (otveti[4]==1):
        return "Если доказан факт самозащиты, либо выполнение служебного долга,\n подозреваемый признается невыновным."
    elif (otveti[2]==3):
        return "Наказание в виде штрафа в размере от ста тысяч до трехсот тысяч рублей;\n либо лишения свободы на срок от трех до пяти лет."
    elif (otveti[3]==1):
        return "Наказываются обязательными работами на срок до трехсот шестидесяти часов;\n либо ограничением свободы на срок до двух лет."
    elif (otveti[2]==1):
        return "Наказывается лишением свободы на срок от трех до шести лет."
    elif (otveti[2]==2):
        return "Hаказывается лишением свободы на срок от восьми до пятнадцати лет\n с лишением права занимать определенные должности или заниматься \n определенной деятельностью на срок до двадцати лет или без такового \n и с ограничением свободы на срок до двух лет."
    else: return "Лишение свободы на срок от 6 до 18 месяцев с запретом на выезд из страны на срок до 6 лет."

class PDD:

    bd = sqlite3.connect('База данных.db')
    cursor = bd.cursor()
    cursor.execute("SELECT * FROM ПДД")
    otveti = []

    def Next(event):
        Delete()
        rd1.pack(anchor=CENTER)
        rd2.pack(anchor=CENTER)
        rd3.pack(anchor=CENTER)
        but12.pack(anchor=S, expand=1, pady=100)
        mass = PDD.cursor.fetchone()
        lb_1["text"] = mass[0]
        rd1["text"] = mass[1]
        rd2["text"] = mass[2]
        rd3["text"] = mass[3]

    def Zapolnenie(event):
        PDD.otveti.append(lang.get())
        mass = PDD.cursor.fetchone()
        if (mass != None):
            lb_1["text"] = mass[0]
            rd1["text"] = mass[1]
            rd2["text"] = mass[2]
            rd3["text"] = mass[3]
        else:
            rd1.destroy()
            rd2.destroy()
            rd3.destroy()
            but12.destroy()
            lb_1["text"] = "По данным дела был проведен анализ и вынесен вердикт:"
            lb_2["text"] = Verdict6(PDD.otveti)
            lb_2.pack(anchor=N)

def Verdict6(otveti):
    if (otveti[0]==1):
        return "Так как подозреваемый имеет возраст младше 14 лет, он не отвечает за свои деяния. \n Подозреваемого поставят на учет в комиссию по делам несовершеннолетних."
    elif ((otveti[1]==3 and otveti[2]==3 and otveti[3]==2) or (otveti[1]==3 and otveti[2]==3 and otveti[3]==3)):
        return "Штраф до 30 тыс руб, за повторное нарушение 200-300 тыс руб\n и лишение прав на срок от полутора до двух лет."
    elif (otveti[1]==3 and otveti[2]==3 and otveti[3]==1):
        return "Cумма штрафа составляет 3-30 тысяч рублей."
    elif (otveti[1]!=3 and otveti[3]==1):
        return "Принудительные работы сроком до 5 лет или лишение свободы.\n Также лишение прав на трёхлетний срок."
    elif (otveti[1]!=3 and otveti[3]!=1):
        return "Лишение свободы на срок до 9 лет."
    else: return "Штраф в размере от 500 рублей до 3 тысяч рублей."

def Delete():
    but1.destroy()
    but2.destroy()
    but3.destroy()
    but4.destroy()
    but5.destroy()
    but6.destroy()

def Start(event):
    but.destroy()
    lb_1["text"] = "Выберите вид преступления"
    but1.place(x=100, y=200)
    but2.place(x=330, y=200)
    but3.place(x=560, y=200)
    but4.place(x=100, y=400)
    but5.place(x=330, y=400)
    but6.place(x=560, y=400)

root = Tk()
root.title("Электронные весы правосудия")  # Название окна
root.geometry('800x600')  # Размер окна
root.resizable(width=False, height=False)

lb_1 = Label(root)
lb_1["text"] = "Электронные весы правосудия"
lb_1["font"] = "Arial 16"
lb_1["height"]=5
lb_1["width"]=60
lb_1.pack(anchor=N, expand=1)

lb_2 = Label(root)
lb_2["font"] = "Arial 12"
lb_2["height"]=40
lb_2["width"]=120

but = Button(root)  # Создание первой кнопки
but["text"] = "Начать проверку"
but["height"]=5
but["width"]=20
but.bind("<Button-1>", Start)
but.pack(anchor=N, expand=1)

but1 = Button(root)  # Создание первой кнопки
but1["text"] = "Кража"
but1["height"]=5
but1["width"]=20
but1.bind("<Button-1>", Krazha.Next)

but2 = Button(root)  # Создание первой кнопки
but2["text"] = "Убийство"
but2["height"]=5
but2["width"]=20
but2.bind("<Button-1>", Ubiystvo.Next)

but3 = Button(root)  # Создание первой кнопки
but3["text"] = "Наркотики"
but3["height"]=5
but3["width"]=20
but3.bind("<Button-1>", Narkotiki.Next)

but4 = Button(root)  # Создание первой кнопки
but4["text"] = "Мошенничество"
but4["height"]=5
but4["width"]=20
but4.bind("<Button-1>", Moshennichestvo.Next)

but5 = Button(root)  # Создание первой кнопки
but5["text"] = "Физическое насилие"
but5["height"]=5
but5["width"]=20
but5.bind("<Button-1>", Nasiliye.Next)

but6 = Button(root)  # Создание первой кнопки
but6["text"] = "ПДД"
but6["height"]=5
but6["width"]=20
but6.bind("<Button-1>", PDD.Next)

but7 = Button(root)
but7["text"] = "Далее"
but7["height"]=5
but7["width"]=20
but7.bind("<Button-1>", Krazha.Zapolnenie)

but8 = Button(root)
but8["text"] = "Далее"
but8["height"]=5
but8["width"]=20
but8.bind("<Button-1>", Ubiystvo.Zapolnenie)

but9 = Button(root)
but9["text"] = "Далее"
but9["height"]=5
but9["width"]=20
but9.bind("<Button-1>", Narkotiki.Zapolnenie)

but10 = Button(root)
but10["text"] = "Далее"
but10["height"]=5
but10["width"]=20
but10.bind("<Button-1>", Moshennichestvo.Zapolnenie)

but11 = Button(root)
but11["text"] = "Далее"
but11["height"]=5
but11["width"]=20
but11.bind("<Button-1>", Nasiliye.Zapolnenie)

but12 = Button(root)
but12["text"] = "Далее"
but12["height"]=5
but12["width"]=20
but12.bind("<Button-1>", PDD.Zapolnenie)

lang = IntVar()
rd1 = Radiobutton(text="Python", value=1, variable=lang, padx=15, pady=10)
rd2 = Radiobutton(text="Python", value=2, variable=lang, padx=15, pady=10)
rd3 = Radiobutton(text="Python", value=3, variable=lang, padx=15, pady=10)


root.mainloop()