import tkinter as tk
from tkinter import ttk
import  mysql.connector

conn=mysql.connector.connect(user='root' , password='' ,host='localhost' ,database='test')

window=tk.Tk()
window.title('Combo Box')
window.geometry('600x600')

ttk.Label(window,text="GFG Combo Box Widget",
          background='green',foreground='white',
          font=('Times New Roman',15)).grid(row=0,column=1)

ttk.Label(window,text="Select Month :",
          font=("Times New Roman",10)).grid(column=0,
                                            row=5,padx=10,pady=25)

n=tk.StringVar()
Select_stmt=("Select country from mstcountry")
cursor=conn.cursor()
cursor.execute(Select_stmt)
Countries=cursor.fetchall()
getCountries=ttk.Combobox(window,width=27,textvariable=n,values=Countries)

#getCountries['values']=('India','Usa','China','South Africa')




getCountries.grid(column=1,row=5)
getCountries.current()
window.mainloop()
