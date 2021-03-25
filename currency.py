from tkinter import *

import mysql.connector

conn = mysql.connector.connect(
    user='root', password='', host='localhost', database='test')


def addCurrency():
    name1 = name.get()
    rate1 = rate.get()

    if name1 == '' or rate1 == '':
        message.set("null")
    else:
        cursor = conn.cursor()
        insert_stmt = ("INSERT INTO `mstcurrency`(`currency_name`,`currency_rate`)"
                       "VALUES(%s,%s)")
        data = (name1, rate1)

        cursor.execute(insert_stmt, data)
        conn.commit()
        # except:
        #   conn.rollback()
        message.set("Stored successfully")


def currency_Form():
    global window
    window = Tk()
    window.title("Currency")
    window.geometry('500x500')
    window.configure(background="grey")

    global name
    global rate
    global message

    name = StringVar()
    rate = IntVar()
    message = StringVar()

    # Creating layout of Registration form
    Label(window, width="300", text="Please enter details below", bg="orange", fg="white").pack()

    # name Label
    Label(window, text="Name * ").place(x=20, y=40)
    # name textbox
    Entry(window, textvariable=name).place(x=90, y=42)
    # contact Label
    Label(window, text="rate * ").place(x=20, y=80)
    # contact textbox
    Entry(window, textvariable=rate).place(x=90, y=82)
    # Label for displaying login status[success/failed]
    Label(window, text="", textvariable=message).place(x=95, y=264)
    # Login button
    Button(window, text="Register", width=10, height=1, bg="orange", command=addCurrency).place(x=105, y=300)
    window.mainloop()


currency_Form()
