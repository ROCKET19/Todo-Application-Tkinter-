from tkinter import *
from sqlite3 import Error
import mysql.connector


def addTask():
    try:
            
       mydb = mysql.connector.connect(
           host = 'localhost',
           user = 'root',
           password = 'root',
           database = 'todo_tkinter'
       )

       cur = mydb.cursor()

       sql = 'INSERT INTO todo_tkinter.todo(Task) values("' + task.get() + '")'
       #val = task.get()
       #val = tuple(val)
       cur.execute(sql)
       
                   
       mydb.commit()
       cur.execute("SELECT * FROM todo")
       result = cur.fetchall()
       for r in result:
           print(r)
        
    except Error as e:
        print(e)
    finally:
        mydb.close()
        task.delete(0, END)


def delTask():
    try:
        
       mydb = mysql.connector.connect(
           host = 'localhost',
           user = 'root',
           password = 'root',
           database = 'todo_tkinter'
       )

       cur = mydb.cursor()
       
       sql = "DELETE FROM todo_tkinter.todo WHERE Id = " + delId.get()
       #val = task.get()
       #val = tuple(val)
       cur.execute(sql)
       
                   
       mydb.commit()
       cur.execute("SELECT * FROM todo")
       result = cur.fetchall()
       for r in result:
           print(r)
        
    except Error as e:
        print(e)
    finally:
        mydb.close()
        task.delete(0, END)


def refresh():
    try:
       td1 = Tk()
       td1.title("Customized Todo List")
       td1.geometry("500x500")
        
       mydb = mysql.connector.connect(
           host = 'localhost',
           user = 'root',
           password = 'root',
           database = 'todo_tkinter'
       )

       cur = mydb.cursor()
       cur.execute("SELECT * from todo_tkinter.todo")

       i = 0
       
       for x in cur:
           for j in range(len(x)):
               ex = Entry(td1, width=30, fg='blue')
               ex.grid(row=i+4, column=j)
               ex.insert(END, x[j])              
           i += 1
           
    except Error as er:
        print(er)
    finally:
        mydb.close()


td = Tk()
td.title("Customized Todo List")
td.geometry("500x500")

l1 = Label(td, text = "Task")
l2 = Label(td, text = "Enter the id to delete")

task = Entry(td, width=20, fg="black", borderwidth=5)
delId = Entry(td, width=20, fg="black", borderwidth=5)


AddTask = Button(td,text="Add Task",padx=10,pady=10,fg="black",bg="white",command=addTask)
DelTask = Button(td,text="Delete Task",padx=10,pady=10,fg="black",bg="white",command=delTask)
Refresh = Button(td,text="Refresh Table",padx=10,pady=10,fg="black",bg="white",command=refresh)

l1.grid(row=0,column=0)
task.grid(row=0,column=1)
l2.grid(row=1, column=0)
delId.grid(row = 1, column = 1)
Refresh.grid(row=2, column=0)
AddTask.grid(row=2, column = 1)
DelTask.grid(row=2, column = 2)

tk2 = Tk()

td.mainloop()
