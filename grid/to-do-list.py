
import tkinter 
from tkinter import messagebox
import random
#from ttkthemes import themed_tk as tk
from sys import exit
import sqlite3 as sq 

#root
#root = tkinter.Tk()
root = tkinter.Tk()
#root.get_themes()                 # Returns a list of all themes that can be set
#root.set_theme("clearlooks")         # Sets an available theme

#Change root background color
root.configure(bg="#f0f0f0")

#change the title
root.title("To-Do List App")
#change the root size
root.geometry("250x250")

#global list for storing tasks
tasks = []

#sqlite setup
conn = sq.connect('todo.db')
cur = conn.cursor()
#create a table
cur.execute('CREATE TABLE IF NOT EXISTS tasks (task text)')


#for testing
#tasks = ["a","b","c","f","e"]

#Functions
def update_listbox():
    """
    Clears the list and then updates the listbox
    """
    clear_listbox()
    for task in tasks:
        lb_list_box.insert("end",task)

def clear_listbox():
   '''Clears the listbox'''
   lb_list_box.delete(0,"end")
   
def on_return(event):
    add_task()

def add_task():
    """Adds a task entered from the input to the listbox.
        Shows a warning if the input box is empty"""
     
    task = txt_input.get() 
    
     #append to the list if input field is not empty
    if task !="":
        tasks.append(task)
        cur.execute('INSERT INTO tasks values(?)',(task,))
        conn.commit()
        update_listbox()
    else:
        messagebox.showwarning("Warning","You need to enter a task")

    #clear the input field
    txt_input.delete(0,"end")

def del_all():
    """
    Deletes all listbox entries
    """
    #global as we are changing the list
    #the tasks list has to be updated globally
    global tasks
    
    if tasks != []:
        confirm = messagebox.askyesno("Confirm: Delete all","Do you want to delete all?")
        if confirm:
            tasks = []

            cur.execute("DELETE FROM tasks")
            conn.commit()
            update_listbox()
        
    else:
        messagebox.showwarning("Warning","The list is empty!!")

def del_one():
    """
    Deletes selcted task from the list box.
    If no task is selected, the tasks are
    deleted in a First In First Out order
    """
    
    task = lb_list_box.get("active")
    if tasks != []:
        confirm = messagebox.askyesno("Confirm: Delete ","Do you want to delete?")
        if task in tasks and confirm:
            tasks.remove(task)
            cur.execute('DELETE FROM tasks where task is (?)',(task,))
            conn.commit()
            update_listbox()
    else:
        messagebox.showwarning("Warning","The list is empty!!")


def choose_random():
    """
    Chooses a task at random and displays it on the label
    """
    task = random.choice(tasks)
    lbl_display["text"] = task

def show_number_tasks():
	tasks_number = len(tasks)
	msg = f"Number of Tasks: {tasks_number}"
	lbl_display["text"] = msg

def ex():
    confirm = messagebox.askyesno("Exit","Do you want to exit")
    if confirm:
        exit()
    
def reload_data():
    global tasks
    tasks = []
    for data in cur.execute('SELECT task from tasks'):
        tasks.append(data)


#setup
lbl_title = tkinter.Label(root,text="To-Do List",bg="white")
lbl_title.grid(row=0,column=0)

lbl_display = tkinter.Label(root,text="",bg="white")
lbl_display.grid(row=0,column=1)

txt_input = tkinter.Entry(root,width = 15)
txt_input.bind("<Return>",on_return)
txt_input.grid(row=1,column=1)

btn_add_task = tkinter.Button(root,text="Add Task",fg="#0000ff",bg="white",command=add_task)
btn_add_task.grid(row=1,column=0)

btn_del_all = tkinter.Button(root,text="Delete All",fg="red",bg="white",command=del_all)
btn_del_all.grid(row=2,column=0)

btn_del_one = tkinter.Button(root,text="Delete",fg="red",bg="white",width=7,command=del_one)
btn_del_one.grid(row=3,column=0)

btn_choose_random = tkinter.Button(root,text="Choose random",fg="#0f0f0f",bg="white",command = choose_random)
btn_choose_random.grid(row=5,column=0)

btn_show_number_tasks = tkinter.Button(root,text="Number of Tasks",fg="#0f0f0f",bg="white",command=show_number_tasks)
btn_show_number_tasks.grid(row=6,column=0)

btn_exit = tkinter.Button(root,text="Exit",fg="green",bg="white",command=ex)
btn_exit.grid(row=7,column=0)

lb_list_box = tkinter.Listbox(root)
lb_list_box.grid(row=2,column=1,rowspan=7)

#retrieve data from database 
#and update the listbox
reload_data()
update_listbox()

root.mainloop()


#close connection
cur.close()